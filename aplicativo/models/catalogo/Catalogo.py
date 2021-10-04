from sqlalchemy import Column, Integer
from pydantic import BaseModel
from aplicativo.database import Base


class Catalogo(Base):
    __tablename__ = "catalogo"
    id = Column(Integer, primary_key=True, nullable=False)


class CatalogoModel(BaseModel):
    id: int
