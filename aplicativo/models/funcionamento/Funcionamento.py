from sqlalchemy import Column, BigInteger, Time, Enum, ForeignKey
from sqlalchemy.schema import UniqueConstraint
from pydantic import BaseModel
from aplicativo.database import Base
from aplicativo.enumerators.dia.dia import Dia
from datetime import time

class Funcionamento(Base):
    __tablename__ = "funcionamento"
    id = Column(BigInteger, primary_key=True, nullable=False)
    perfil_id = Column(ForeignKey("perfil.id"), nullable=False)
    horario_inicio = Column(Time)
    horario_fim = Column(Time)
    dia = Column(Enum(Dia))

    __table_args__ = (UniqueConstraint('dia', 'horario_inicio', 'horario_fim', name='_escala'),)
    # seg 10-00 13-00
    # ter 10-00 13-00

class FuncionamentoModel(BaseModel):
    id: int
    perfil_id: int
    horario_inicio: time
    horario_fim: time
    dia: Dia
