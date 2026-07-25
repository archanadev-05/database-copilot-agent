from fastapi import FastAPI

from user_routes import router as user_router

app = FastAPI(title="ORM Implementation")
app.include_router(user_router)