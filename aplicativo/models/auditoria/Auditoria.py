from sqlalchemy import Column, Integer
from pydantic import BaseModel, constr

from aplicativo.database import Base


class Auditoria(Base):

    __tablename__ = "auditoria"
    id = Column(Integer, primary_key=True, nullable=False)


class AuditoriaModel(BaseModel):
    id: int
