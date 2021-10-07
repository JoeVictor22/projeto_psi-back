from sqlalchemy import Column, ForeignKey
from pydantic import BaseModel
from aplicativo.database import Base


class CatalogoProduto(Base):
    __tablename__ = "catalogo_produto"
    catalogo_id = Column(ForeignKey("catalogo.id"), primary_key=True, nullable=False)
    produto_id = Column(ForeignKey("produto.id"), primary_key=True, nullable=False)


class CatalogoProdutoModel(BaseModel):
    catalogo_id: int
    produto_id: int
