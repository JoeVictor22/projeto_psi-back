from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Catalogo(Base):
    __tablename__ = 'catalogo'
    id = Column(Integer, primary_key=True, nullable=False)

class CatalogoModel(BaseModel):
    id: int