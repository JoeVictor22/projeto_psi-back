from sqlalchemy import Column, BigInteger, String, ForeignKey
from pydantic import BaseModel, constr
from aplicativo.database import Base
from aplicativo.models.utils.ClasseBase import ClasseBase


class Catalogo(Base, ClasseBase):
    __tablename__ = "catalogo"
    id = Column(BigInteger, primary_key=True, nullable=False)
    nome = Column(String(255))
    perfil_id = Column(ForeignKey("perfil.id"), nullable=False)
    descricao = Column(String(255), nullable=False)
    _fields = ["nome", "perfil_id", "descricao"]


class CatalogoModel(BaseModel):
    id: int
    nome: constr(max_length=255)
    perfil_id: int
    descricao: constr(max_length=255)
