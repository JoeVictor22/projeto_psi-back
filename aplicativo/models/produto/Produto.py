from sqlalchemy import Column, Integer
from pydantic import BaseModel
from aplicativo.database import Base


class Produto(Base):
    __tablename__ = "produto"
    id = Column(Integer, primary_key=True, nullable=False)


class ProdutoModel(BaseModel):
    id: int
