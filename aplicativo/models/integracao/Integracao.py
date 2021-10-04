from sqlalchemy import Column, Integer
from pydantic import BaseModel
from aplicativo.database import Base


class Integracao(Base):
    __tablename__ = "integracao"
    id = Column(Integer, primary_key=True, nullable=False)


class IntegracaoModel(BaseModel):
    id: int
