from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Funcionamento(Base):
    __tablename__ = 'funcionamento'
    id = Column(Integer, primary_key=True, nullable=False)

class FuncionamentoModel(BaseModel):
    id: int