from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()


class CatalogoProduto(Base):
    __tablename__ = "catalogo_produto"
    id = Column(Integer, primary_key=True, nullable=False)


class CatalogoProdutoModel(BaseModel):
    id: int
