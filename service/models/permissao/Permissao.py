from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Permissao(Base):
    __tablename__ = 'permissao'
    id = Column(Integer, primary_key=True, nullable=False)

class PermissaoModel(BaseModel):
    id: int