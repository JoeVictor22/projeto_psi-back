from typing import Optional

from sqlalchemy import Column, BigInteger, String, ForeignKey
from pydantic import BaseModel, constr
from aplicativo.database import Base
from aplicativo.models.utils.ClasseBase import ClasseBase


class Produto(Base, ClasseBase):
    __tablename__ = "produto"
    id = Column(BigInteger, primary_key=True, nullable=False)
    nome = Column(String(255))
    categoria_id = Column(ForeignKey("categoria.id"), nullable=True)
    perfil_id = Column(ForeignKey("perfil.id"), nullable=False)
    _fields = ["nome", "categoria_id", "perfil_id"]

    def to_json(self):
        dicionario = {key: getattr(self, key) for key in self._fields}
        dicionario["id"] = self.id
        return dicionario

    @staticmethod
    def from_dict(dicionario):
        return ClasseBase.from_dict(dicionario, Produto)

    @staticmethod
    def to_update(dicionario):
        return ClasseBase.to_update(dicionario, Produto)


class ProdutoModel(BaseModel):
    id: Optional[int]
    nome: constr(max_length=255)
    categoria_id: Optional[int]
    perfil_id: int
