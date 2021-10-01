from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, constr

Base = declarative_base()

class Auditoria(Base):
    __tablename__ = 'auditoria'
    id = Column(Integer, primary_key=True, nullable=False)

class AuditoriaModel(BaseModel):
    id: int
    public_key: constr(max_length=20)
    name: constr(max_length=63)

