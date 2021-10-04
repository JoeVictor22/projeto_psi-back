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
    grupo_id = Column(Integer)


class UsuarioModel(BaseModel):
    id: int
    nome: constr(max_length=255)
    email: constr(max_length=255)
    senha: constr(max_length=50)
    grupo_id = int
