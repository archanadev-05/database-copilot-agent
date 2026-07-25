from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from database_config import get_db
from db_models import User
from resp_models import UserCreate
from user_repository import UserRepository

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate, db: AsyncSession = Depends(get_db())): #dependency injection
    repo = UserRepository(db)
    user = await repo.create(user_data)
    return user
