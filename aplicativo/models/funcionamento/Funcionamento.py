from sqlalchemy import Column, BigInterger, Time, Enum, ForeignKey
from pydantic import BaseModel
from aplicativo.database import Base


class Funcionamento(Base):
    __tablename__ = "funcionamento"
    id = Column(BigInterger, primary_key=True, nullable=False)
    perfil_id = Column(ForeignKey("perfil.id"), nullable=False)
    horario_inicio = Column(Time)
    horario_fim = Column(Time)
    dia = Column(Enum(Dia))


class FuncionamentoModel(BaseModel):
    id: int
    perfil_id: int
    horario_inicio: Time
    horario_fim: Time
    dia: Dia
