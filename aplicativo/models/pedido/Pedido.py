from sqlalchemy import Column, BigInteger, JSON, DateTime, Boolean, String, ForeignKey
from pydantic import BaseModel, constr, Json
from aplicativo.database import Base
from datetime import datetime


class Pedido(Base):
    __tablename__ = "pedido"
    id = Column(BigInteger, primary_key=True, nullable=False)
    resumo = Column(JSON)
    telefone = Column(String(255))
    perfil_id = Column(ForeignKey("perfil.id"), nullable=False)
    data = Column(DateTime)
    confirmado = Column(Boolean)


class PedidoModel(BaseModel):
    id: int
    resumo: Json
    telefone: constr(max_length=255)
    data: datetime
    confirmado: bool
