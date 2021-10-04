from sqlalchemy import Column, Integer
from pydantic import BaseModel
from aplicativo.database import Base


class Perfil(Base):
    __tablename__ = "perfil"
    id = Column(Integer, primary_key=True, nullable=False)


class PerfilModel(BaseModel):
    id: int
