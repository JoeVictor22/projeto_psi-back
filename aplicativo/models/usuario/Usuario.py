from sqlalchemy import Column, BigInteger, Integer, String
from pydantic import BaseModel, constr
from aplicativo.models.utils.ClasseBase import ClasseBase
from aplicativo.database import Base

# https://docs.sqlalchemy.org/en/14/core/type_basics.html
# https://pydantic-docs.helpmanual.io/usage/types/


class Usuario(Base, ClasseBase):
    __tablename__ = "usuario"
    id = Column(BigInteger, primary_key=True, nullable=False)
    nome = Column(String(255))
    email = Column(String(255), unique=True)
    senha = Column(String(255))
    grupo_id = Column(Integer)  # FK enum GRUPO
    _fields = ["nome", "email", "senha", "grupo_id"]

    @staticmethod
    def from_dict(dicionario):
        return ClasseBase.from_dict(dicionario, Usuario)

    def to_json(self):
        dicionario = {key: getattr(self, key) for key in self._fields}
        dicionario["id"] = self.id
        return dicionario

    @staticmethod
    def to_update(dicionario):
        del dicionario['senha']
        return ClasseBase.to_update(dicionario, Usuario)


class UsuarioModel(BaseModel):
    nome: constr(max_length=255)
    email: constr(max_length=255)
    senha: constr(max_length=255)
    grupo_id: int

    class Config:
        orm_mode = True
