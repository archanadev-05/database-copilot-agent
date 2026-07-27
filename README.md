# 🗄️ Database Copilot Agent

An AI-powered database assistant that allows users to interact with PostgreSQL databases using natural language.

This project uses **LangGraph, LangChain, FastAPI, SQLAlchemy ORM, PostgreSQL, and Gradio** to build an intelligent SQL agent that understands user questions, generates SQL queries, executes them safely, and returns human-readable responses.

---

## 🚀 Features

- 🤖 Natural language database querying
- 🧠 LangGraph-powered AI agent workflow
- 🔗 LangChain SQL Database Toolkit integration
- 🗃️ PostgreSQL database integration
- 🏗️ SQLAlchemy ORM architecture
- ⚡ FastAPI backend API
- 💬 Gradio conversational user interface
- 🔐 Environment variable based configuration
- 🧵 Conversation memory using LangGraph checkpointer
- 🛡️ Safe database interaction with read-only SQL operations

---

# 🏗️ System Architecture

```
                    User
                     |
                     |
                     v
              Gradio Interface
                     |
                     |
                     v
                  FastAPI
                     |
                     |
                     v
           LangGraph Database Agent
                     |
                     |
                     v
            LangChain SQL Toolkit
                     |
                     |
                     v
               PostgreSQL Database
```

---

# 🧠 How It Works

1. User asks a question using natural language.

Example:

```
How many users are in my database?
```

2. The LangGraph agent processes the request.

3. The agent:
   - Inspects available database tables
   - Retrieves relevant schema information
   - Generates a SQL query
   - Executes the query safely

Example generated query:

```sql
SELECT COUNT(*) FROM users;
```

4. The result is converted into a natural language response.

Example:

```
There are 50 users in your database.
```

---

# 🛠️ Tech Stack

## Backend

- Python
- FastAPI
- SQLAlchemy ORM
- PostgreSQL

## AI Framework

- LangChain
- LangGraph
- OpenAI API

## Frontend

- Gradio

## Database

- PostgreSQL

---

# 📂 Project Structure

```
database-copilot-agent/

│
├── main.py                  # FastAPI application entry point
│
├── db_agent.py              # LangGraph SQL agent implementation
│
├── agent_routes.py          # AI agent API routes
│
├── user_routes.py           # User management APIs
│
├── invoice_routes.py        # Invoice management APIs
│
├── models/                  # SQLAlchemy ORM models
│
├── repositories/            # Database repository layer
│
├── database/                # Database configuration
│
├── .env                     # Environment variables
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/<username>/database-copilot-agent.git

cd database-copilot-agent
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### macOS/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Configuration

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/database_name

OPENAI_API_KEY=your_openai_api_key
```

Example:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/SuperMarket
```

---

# ▶️ Running the Application

Start FastAPI server:

```bash
uvicorn main:app --reload
```

Application will run at:

```
http://127.0.0.1:8000
```

---

# 💬 Using the AI Database Assistant

Open the Gradio interface:

```
http://127.0.0.1:8000/agent/ui
```

Example questions:

```
How many users are in my database?
```

```
Show all invoices.
```

```
Which user has the highest invoice amount?
```

```
How many invoices were created today?
```

---

# 🔒 Database Safety

The AI agent is configured to prevent destructive database operations.

Allowed:

```sql
SELECT
```

Blocked:

```sql
INSERT
UPDATE
DELETE
DROP
ALTER
```

The agent only performs safe read operations.

---

# 🧩 LangGraph Agent Workflow

```
User Question

      |
      v

Database Agent

      |
      v

Inspect Database Schema

      |
      v

Generate SQL Query

      |
      v

Execute Query

      |
      v

Generate Natural Language Answer
```

---

# 🔮 Future Improvements

- Add user authentication and authorization
- Support multiple database engines
- Add SQL query explanation
- Add database schema visualization
- Add streaming AI responses
- Add Docker deployment
- Add monitoring and logging
- Add RAG-based database documentation search

---

# 👨‍💻 Author

**Archana Thanuwana**

AI / Machine Learning Engineer

---

# ⭐ Acknowledgements

- LangChain
- LangGraph
- FastAPI
- SQLAlchemy
- PostgreSQL
- Gradio
