from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Rota(Base):
    __tablename__ = 'rota'
    id = Column(Integer, primary_key=True, nullable=False)

class RotaModel(BaseModel):
    id: int