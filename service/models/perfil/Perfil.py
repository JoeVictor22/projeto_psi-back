from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Perfil(Base):
    __tablename__ = 'perfil'
    id = Column(Integer, primary_key=True, nullable=False)

class PerfilModel(BaseModel):
    id: int