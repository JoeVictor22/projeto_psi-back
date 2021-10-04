from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()


class Pedido(Base):
    __tablename__ = "pedido"
    id = Column(Integer, primary_key=True, nullable=False)


class PedidoModel(BaseModel):
    id: int
