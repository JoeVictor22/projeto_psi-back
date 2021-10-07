from sqlalchemy import Column, BigInteger, ForeignKey, String, Float, Enum
from pydantic import BaseModel, constr
from aplicativo.database import Base
from aplicativo.enumerators.cidade.cidade import Cidade


class Perfil(Base):
    __tablename__ = "perfil"
    id = Column(BigInteger, primary_key=True, nullable=False)
    usuario_id = Column(ForeignKey("usuario.id"), nullable=False)
    nome = Column(String(255))
    endereco = Column(String(255))
    cidade_id = Column(Enum(Cidade), nullable=False)
    geolocalizacao = Column(Float, nullable=False)
    email = Column(String(255))
    cnpj_cpf = Column(String(255))


class PerfilModel(BaseModel):
    id: int
    usuario_id: int
    nome: constr(max_length=255)
    endereco: constr(max_length=255)
    cidade_id: Cidade
    geolocalizacao: float
    email: constr(max_length=255)
    cnpj_cpf: constr(max_length=255)
