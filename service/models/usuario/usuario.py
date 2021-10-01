from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Usario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, nullable=False)

class UsarioModel(BaseModel):
    id: int