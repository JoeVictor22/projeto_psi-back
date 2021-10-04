from sqlalchemy import Column, Integer
from pydantic import BaseModel
from aplicativo.database import Base


class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, nullable=False)


class UsuarioModel(BaseModel):
    id: int
