# Intelligent Database Agent 🤖

An AI-powered database assistant built with **FastAPI, SQLAlchemy ORM, PostgreSQL, LangChain, and LangGraph** that enables intelligent interaction with databases using natural language.

The system combines traditional backend architecture with modern AI agent workflows to understand user requests, reason through tasks, generate database operations, and provide meaningful insights.

---

## 🚀 Features

### 🗄️ Database Management
- PostgreSQL database integration
- SQLAlchemy ORM-based architecture
- Repository pattern implementation
- CRUD operations
- Database session management
- Data validation using Pydantic

### 🤖 AI Agent Capabilities
- Natural language database interaction
- LLM-powered reasoning
- Intelligent query understanding
- Automated SQL generation
- Database insights generation
- Multi-step AI workflows using LangGraph

### ⚡ Backend Features
- FastAPI REST API
- Asynchronous API support
- Dependency injection
- Modular architecture
- Scalable service-layer design

---

# 🏗️ System Architecture


```
                    User
                     |
                     |
              Natural Language Query
                     |
                     |
                 FastAPI
                     |
          -----------------------
          |                     |
     API Routers            AI Agent
                                |
                           LangGraph
                                |
              --------------------------------
              |              |               |
        Query Analyzer   SQL Generator   Response Agent
              |
              |
        LangChain + LLM
              |
              |
        SQLAlchemy ORM
              |
              |
          PostgreSQL
```

---

# 🧠 LangGraph Agent Workflow


The AI agent uses LangGraph to create a structured reasoning workflow.

```
User Question

      |
      v

Input Understanding Node

      |
      v

Database Context Retrieval

      |
      v

SQL Generation Node

      |
      v

Query Execution Node

      |
      v

Response Generation Node

      |
      v

Final Answer
```

LangGraph provides:
- Stateful agent execution
- Multiple AI processing steps
- Agent decision flow
- Better control compared to simple LLM chains

---

# 🛠️ Tech Stack

## Backend

| Technology | Purpose |
|-|-|
| Python | Core programming language |
| FastAPI | Backend API framework |
| SQLAlchemy | ORM database layer |
| Pydantic | Data validation |
| PostgreSQL | Relational database |


## AI Stack

| Technology | Purpose |
|-|-|
| LangChain | LLM application framework |
| LangGraph | Agent workflow orchestration |
| OpenAI / OpenRouter | Large Language Models |
| Prompt Engineering | Agent reasoning |


## Development Tools

- Git
- Docker
- Pytest
- Uvicorn
- Alembic

---

# 📂 Project Structure

```
intelligent-database-agent/

│
├── app/
│   │
│   ├── main.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   ├── session.py
│   │   └── base.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── invoice.py
│   │
│   ├── schemas/
│   │   ├── user_schema.py
│   │   └── invoice_schema.py
│   │
│   ├── repositories/
│   │   ├── user_repository.py
│   │   └── invoice_repository.py
│   │
│   ├── services/
│   │   ├── user_service.py
│   │   └── ai_service.py
│   │
│   ├── routers/
│   │   ├── user_routes.py
│   │   ├── invoice_routes.py
│   │   └── agent_routes.py
│   │
│   ├── agents/
│   │   ├── graph.py
│   │   ├── nodes.py
│   │   └── prompts.py
│   │
│   └── config.py
│
├── tests/
│
├── .env.example
├── requirements.txt
├── README.md
└── Dockerfile
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/intelligent-database-agent.git
```

Move into project:

```bash
cd intelligent-database-agent
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

### Mac/Linux

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

Create a `.env` file:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/database_name

OPENAI_API_KEY=your_api_key

MODEL_NAME=gpt-4.1-mini
```

Example:

```
.env.example
```

should contain:

```env
DATABASE_URL=

OPENAI_API_KEY=

MODEL_NAME=
```

---

# 🗄️ Database Setup

Create PostgreSQL database:

```sql
CREATE DATABASE intelligent_agent;
```

Run migrations:

```bash
alembic upgrade head
```

---

# ▶️ Run Application

Start FastAPI server:

```bash
uvicorn app.main:app --reload
```

Application:

```
http://127.0.0.1:8000
```

API Documentation:

```
http://127.0.0.1:8000/docs
```

---

# 🔌 API Endpoints

## Users

```
POST    /users
GET     /users
GET     /users/{id}
DELETE  /users/{id}
```

## Invoices

```
POST    /invoices
GET     /invoices
GET     /invoices/{id}
```

## AI Agent

```
POST /agent/query
```

Example request:

```json
{
    "query": "Show total invoice amount for each customer"
}
```

Example response:

```json
{
    "answer": "Customer A has total invoices of $5000"
}
```

---

# 🏛️ ORM Architecture

This project follows a layered architecture:


```
Router Layer

      ↓

Service Layer

      ↓

Repository Layer

      ↓

SQLAlchemy ORM Models

      ↓

PostgreSQL Database
```

Benefits:

- Separation of concerns
- Easier testing
- Maintainable codebase
- Scalable backend design

---

# 🔄 AI Agent Architecture

The AI agent follows a graph-based workflow:


```
START

 ↓

User Intent Analysis

 ↓

Database Schema Understanding

 ↓

SQL Generation

 ↓

SQL Validation

 ↓

Database Execution

 ↓

Answer Generation

 ↓

END
```

---

# 🔮 Future Improvements

- JWT authentication
- Role-based access control
- Vector database integration
- RAG-based database knowledge retrieval
- Advanced analytics dashboard
- Docker deployment
- Kubernetes deployment
- Cloud hosting
- Multi-agent collaboration

---

# 👨‍💻 Author

**Archana Thanuwana**

AI Engineer | Backend Developer

GitHub:
https://github.com/archanadev-05

---

# 📜 License

This project is licensed under the MIT License.
