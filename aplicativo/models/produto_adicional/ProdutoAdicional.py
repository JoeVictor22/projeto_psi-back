from sqlalchemy import Column, Integer
from pydantic import BaseModel
from aplicativo.database import Base


class ProdutoAdicional(Base):
    __tablename__ = "produto_adicional"
    id = Column(Integer, primary_key=True, nullable=False)


class ProdutoAdicionalModel(BaseModel):
    id: int
