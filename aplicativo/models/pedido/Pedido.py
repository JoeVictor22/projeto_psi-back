from sqlalchemy import Column, BigInteger, Json, DateTime, Boolean, String, ForeignKey
from pydantic import BaseModel, constr
from aplicativo.database import Base


class Pedido(Base):
    __tablename__ = "pedido"
    id = Column(BigInteger, primary_key=True, nullable=False)
    resumo = Column(Json)
    telefone = Column(String(255))
    perfil_id = Column(ForeignKey('perfil.id'), nullable=False)
    data = Column(DateTime)
    confirmado = Column(Boolean)


class PedidoModel(BaseModel):
    id: int
    resumo: Json
    telefone: constr(max_length=255)
    data: DateTime
    confirmado: Boolean