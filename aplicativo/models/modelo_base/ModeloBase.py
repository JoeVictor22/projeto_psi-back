from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()


class ModeloBase(Base):
    __tablename__ = "modelo_base"
    id = Column(Integer, primary_key=True, nullable=False)


class ModeloBaseModel(BaseModel):
    id: int
