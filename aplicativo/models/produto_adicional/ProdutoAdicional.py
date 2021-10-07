from sqlalchemy import Column, Integer, Enum, ForeignKey
from pydantic import BaseModel
from aplicativo.database import Base
from aplicativo.enumerators.tipo_produto.tipo_produto import TipoProduto


class ProdutoAdicional(Base):
    __tablename__ = "produto_adicional"
    produto_pai = Column(ForeignKey("produto.id"), primary_key=True, nullable=False)
    produto_filho = Column(ForeignKey("produto.id"), primary_key=True, nullable=False)
    tipo_produto_id = Column(Enum(TipoProduto))


class ProdutoAdicionalModel(BaseModel):
    produto_pai: int
    produto_filho: int
    tipo_produto_id: TipoProduto
