from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()


class Integracao(Base):
    __tablename__ = "integracao"
    id = Column(Integer, primary_key=True, nullable=False)


class IntegracaoModel(BaseModel):
    id: int
