from sqlalchemy import Column, Integer
from pydantic import BaseModel
from aplicativo.database import Base


class Funcionamento(Base):
    __tablename__ = "funcionamento"
    id = Column(Integer, primary_key=True, nullable=False)


class FuncionamentoModel(BaseModel):
    id: int
