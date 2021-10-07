from sqlalchemy import Column, Integer, Enum, ForeignKey
from pydantic import BaseModel, constr
from aplicativo.database import Base


class Integracao(Base):
    __tablename__ = "integracao"
    id = Column(Integer, primary_key=True, nullable=False)
    tipo_integracao_id = Column(Enum(TipoIntegracao), nullable=False)
    perfil_id = Column(ForeignKey('perfil.id'), nullable=False)


class IntegracaoModel(BaseModel):
    id: int
    tipo_integracao_id: TipoIntegracao
    perfil_id: int
