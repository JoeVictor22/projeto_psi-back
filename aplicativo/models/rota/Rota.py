from sqlalchemy import Column, Integer
from pydantic import BaseModel
from aplicativo.database import Base


class Rota(Base):
    __tablename__ = "rota"
    id = Column(Integer, primary_key=True, nullable=False)


class RotaModel(BaseModel):
    id: int
