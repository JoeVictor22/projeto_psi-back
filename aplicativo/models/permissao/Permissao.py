from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from pydantic import BaseModel, constr
from aplicativo.database import Base


class Permissao(Base):
    __tablename__ = "permissao"
    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(255))
    grupo_id = Column(Enum(Grupo), nullable=False)
    rota_id = Column(ForeignKey('rota.id'), nullable=False)


class PermissaoModel(BaseModel):
    id: int
    nome: constr(max_length=255)
    grupo_id: Grupo
    rota_id: int
