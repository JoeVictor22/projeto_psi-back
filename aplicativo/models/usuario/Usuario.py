from sqlalchemy import Column, BigInteger, Integer, String
from pydantic import BaseModel, constr
from aplicativo.database import Base

# https://docs.sqlalchemy.org/en/14/core/type_basics.html
# https://pydantic-docs.helpmanual.io/usage/types/


class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(BigInteger, primary_key=True, nullable=False)
    nome = Column(String(255))
    email = Column(String(255), unique=True)
    senha = Column(String(50))
    grupo_id = Column(Integer)  # FK enum GRUPO

    _fields = ["nome", "email", "senha", "grupo_id"]

    @staticmethod
    def from_dict(dicionario):
        return Usuario(
            nome=dicionario["nome"],
            email=dicionario["email"],
            senha=dicionario["senha"],
            grupo_id=dicionario["grupo_id"],
        )

    def to_dict(self):
        return dict(
            nome=self.nome, email=self.email, senha=self.senha, grupo_id=self.grupo_id
        )

    @staticmethod
    def to_update(dicionario):
        fields_to_edit = {
            nome_campo: dicionario[nome_campo]
            for nome_campo in Usuario._fields
            if nome_campo in dicionario
        }
        return fields_to_edit

    @property
    def schema(self):
        return UsuarioModel


class UsuarioModel(BaseModel):
    nome: constr(max_length=255)
    email: constr(max_length=255)
    senha: constr(max_length=50)
    grupo_id: int

    class Config:
        orm_mode = True
