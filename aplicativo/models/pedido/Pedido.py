from sqlalchemy import Column, Integer
from pydantic import BaseModel
from aplicativo.database import Base


class Pedido(Base):
    __tablename__ = "pedido"

    id = Column(Integer, primary_key=True, nullable=False)


class PedidoModel(BaseModel):
    id: int
