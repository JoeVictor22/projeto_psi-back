from sqlalchemy import Column, Integer
from pydantic import BaseModel
from aplicativo.database import Base


class Categoria(Base):
    __tablename__ = "categoria"
    id = Column(Integer, primary_key=True, nullable=False)


class CategoriaModel(BaseModel):
    id: int
