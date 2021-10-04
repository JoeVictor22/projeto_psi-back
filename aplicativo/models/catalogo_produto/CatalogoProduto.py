from sqlalchemy import Column, Integer
from pydantic import BaseModel
from aplicativo.database import Base


class CatalogoProduto(Base):
    __tablename__ = "catalogo_produto"
    id = Column(Integer, primary_key=True, nullable=False)


class CatalogoProdutoModel(BaseModel):
    id: int
