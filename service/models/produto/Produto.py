from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produto'
    id = Column(Integer, primary_key=True, nullable=False)

class ProdutoModel(BaseModel):
    id: int