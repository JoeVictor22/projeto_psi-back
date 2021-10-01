from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class ProdutoAdicional(Base):
    __tablename__ = 'produto_adicional'
    id = Column(Integer, primary_key=True, nullable=False)

class ProdutoAdicionalModel(BaseModel):
    id: int