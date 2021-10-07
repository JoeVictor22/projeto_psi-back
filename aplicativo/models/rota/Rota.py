from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, constr
from aplicativo.database import Base


class Rota(Base):
    __tablename__ = "rota"
    id = Column(Integer, primary_key=True, nullable=False)
    url = Column(String(255), unique=True)


class RotaModel(BaseModel):
    id: int
    url: constr(max_length=255)
