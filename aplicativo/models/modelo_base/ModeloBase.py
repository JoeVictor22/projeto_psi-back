from sqlalchemy import Column, Integer
from pydantic import BaseModel
from aplicativo.database import Base


class ModeloBase(Base):
    __tablename__ = "modelo_base"
    id = Column(Integer, primary_key=True, nullable=False)


class ModeloBaseModel(BaseModel):
    id: int
