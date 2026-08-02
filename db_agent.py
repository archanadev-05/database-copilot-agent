from logging import config
from uuid import uuid4

import psycopg
from langchain_classic.agents.chat.prompt import HUMAN_MESSAGE
from langchain_core.messages import SystemMessage, HumanMessage
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
from sqlalchemy.ext.asyncio import AsyncSession

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




conn = psycopg.connect(DB_URL,autocommit=True)
checkpointer = PostgresSaver(conn)
checkpointer.setup()



agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=system_prompt,
    checkpointer=checkpointer
)



async def propose_dml_statement_for_human_approval(
        question: str,
        session: AsyncSession,
):
    schema_details = db.get_table_info()
    prompt = f"""
    You are SQL assistant, Generate Exactly INSERT,UPDATE,DELETE Statements
    Depending on the users requirements for {db.dialect}. User Provided Schema and DO NOT
    output anything except for the SQL statement. Do not Wrap it in code fences
    
    {schema_details}
    
    User Request - {query}
    
    """

    resp = model.invoke([
        SystemMessage(content="You only Return single SQL statement"),
        HumanMessage(content=prompt),
    ])

    sql = resp.content if hasattr(resp, "content") else str(resp)

    approval_id = str(uuid4())


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


