from sqlalchemy import Column, Integer, String, ForeignKey
from pydantic import BaseModel, constr
from aplicativo.database import Base


class Categoria(Base):
    __tablename__ = "categoria"
    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(255))
    descricao = Column(String(255), nullable=False)
    perfil_id = Column(ForeignKey("perfil.id"), nullable=False)


class CategoriaModel(BaseModel):
    id: int
    nome: constr(max_length=255)
    descricao: constr(max_length=255)
    perfil_id: int
