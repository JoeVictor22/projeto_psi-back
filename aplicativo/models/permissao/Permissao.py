from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Enum
from pydantic import BaseModel, constr
from aplicativo.database import Base
from aplicativo.enumerators.grupo.grupo import Grupo


class Permissao(Base):
    __tablename__ = "permissao"
    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(255))
    grupo_id = Column(Enum(Grupo), nullable=False)
    rota_id = Column(ForeignKey("rota.id"), nullable=False)
    permitir = Column(Boolean, nullable=False, default=False)

class PermissaoModel(BaseModel):
    id: int
    nome: constr(max_length=255)
    grupo_id: Grupo
    rota_id: int
    permitir: bool = False
