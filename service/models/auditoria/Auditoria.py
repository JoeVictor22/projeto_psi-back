from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, constr

Base = declarative_base()


class Tabela(Base):
    __tablename__ = 'nome_da_tabela'
    id = Column(Integer, primary_key=True, nullable=False)
    public_key = Column(String(20), index=True, nullable=False, unique=True)
    name = Column(String(63), unique=True)


class TabelaModel(BaseModel):
    id: int
    public_key: constr(max_length=20)
    name: constr(max_length=63)

