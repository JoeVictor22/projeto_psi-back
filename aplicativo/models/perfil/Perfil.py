from typing import Optional

from sqlalchemy import Column, BigInteger, ForeignKey, String, Float, Enum
from pydantic import BaseModel, constr
from aplicativo.database import Base
from aplicativo.enumerators.cidade.Cidade import Cidade
from aplicativo.models.utils.ClasseBase import ClasseBase


class Perfil(Base, ClasseBase):
    __tablename__ = "perfil"
    id = Column(BigInteger, primary_key=True, nullable=False)
    usuario_id = Column(ForeignKey("usuario.id"), nullable=False)
    nome = Column(String(255))
    endereco = Column(String(255))
    cidade_id = Column(Enum(Cidade), nullable=False)
    geolocalizacao = Column(Float, nullable=False)
    email = Column(String(255))
    cnpj_cpf = Column(String(255))
    _fields = [
        "usuario_id",
        "nome",
        "endereco",
        "cidade_id",
        "geolocalizacao",
        "email",
        "cnpj_cpf",
    ]

    @staticmethod
    def from_dict(dicionario):
        dicionario["cidade_id"] = Cidade(dicionario["cidade_id"]).name
        return ClasseBase.from_dict(dicionario, Perfil)

    def to_dict(self):
        dicionario = {key: getattr(self, key) for key in self._fields}
        return dicionario

    def to_json(self):
        dicionario = {key: getattr(self, key) for key in self._fields}
        dicionario["cidade_id"] = dicionario["cidade_id"].value
        dicionario["id"] = self.id
        return dicionario

    @staticmethod
    def to_update(dicionario):
        return ClasseBase.to_update(dicionario, Perfil)

    @staticmethod
    def to_update(dicionario):
        fields_to_edit = {
            nome_campo: dicionario[nome_campo]
            for nome_campo in Perfil._fields
            if nome_campo in dicionario
        }
        if fields_to_edit.get("cidade_id"):
            fields_to_edit["cidade_id"] = Cidade(dicionario["cidade_id"]).name
        return fields_to_edit


class PerfilModel(BaseModel):
    id: Optional[int]
    usuario_id: int
    nome: constr(max_length=255)
    endereco: constr(max_length=255)
    cidade_id: int
    geolocalizacao: float
    email: constr(max_length=255)
    cnpj_cpf: constr(max_length=255)