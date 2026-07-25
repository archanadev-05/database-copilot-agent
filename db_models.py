from datetime import datetime

from sqlalchemy import String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedColumn


class Base(DeclarativeBase): #DRY-Dont Repeat yourself
    pass

class User(Base):
    __tablename__ = 'users'
    id : Mapped[int] = MappedColumn(primary_key=True, index=True)
    name : Mapped[str] = MappedColumn(String(255), nullable=False)
    email : Mapped[str] = MappedColumn(String(255), unique=True, nullable=False)

class Invoice(Base):
    __tablename__ = 'invoices'
    id : Mapped[int] = MappedColumn(primary_key=True, index=True)
    user_id : Mapped[int] = MappedColumn(nullable=False)
    amount : Mapped[float]
    description : Mapped[str] = MappedColumn(String(255), nullable=False)
    created_at : Mapped[datetime] = MappedColumn(
        server_default= func.now(),
        default= datetime.now()
    )