from logging import config
import psycopg
from langgraph.checkpoint.postgres import PostgresSaver
import psycopg
import psycopg2
from anyio.lowlevel import checkpoint
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_classic.chains.sql_database import query
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.postgres import PostgresSaver

load_dotenv()


DB_URL = "postgresql://archana:admin@localhost:5432/SuperMarket"

db = SQLDatabase.from_uri(DB_URL)

model = ChatOpenAI(
    model="gpt-5.4"

)


toolkit = SQLDatabaseToolkit(db=db, llm=model)
tools = toolkit.get_tools()

system_prompt = """
You are an agent designed to interact with a SQL database.
Given an input question, create a syntactically correct {dialect} query to run,
then look at the results of the query and return the answer. Unless the user
specifies a specific number of examples they wish to obtain, always limit your
query to at most {top_k} results.

You can order the results by a relevant column to return the most interesting
examples in the database. Never query for all the columns from a specific table,
only ask for the relevant columns given the question.

You MUST double check your query before executing it. If you get an error while
executing a query, rewrite the query and try again.

DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the
database.

To start you should ALWAYS look at the tables in the database to see what you
can query. Do NOT skip this step.

Then you should query the schema of the most relevant tables.
""".format(
    dialect=db.dialect,
    top_k=5,
)




conn = psycopg.connect(
    DB_URL,
    autocommit=True

)

checkpointer = PostgresSaver(conn)

checkpointer.setup()



agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=system_prompt,
    checkpointer=checkpointer

)

def query_db_with_natural_language(user_input:str, thread_id:str = "1"):
    try:
        config = {"configurable": {"thread_id": thread_id}}
        output_result = None

        for step in agent.stream(
                {"messages": [{"role" : "user", "content" : user_input}]},
                config,
                stream_mode="values"
        ):
            if "messages" in step:
                last_message = step["messages"][-1]
                if hasattr(last_message, "content"):
                    output_result = last_message.content

        return output_result if output_result else "No content"
    except Exception as e:
        return f"Error Occurred - {str(e)}"


