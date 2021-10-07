from sqlalchemy import Column, BigInteger, String, ForeignKey
from pydantic import BaseModel, constr
from aplicativo.database import Base


class Produto(Base):
    __tablename__ = "produto"
    id = Column(BigInteger, primary_key=True, nullable=False)
    nome = Column(String(255))
    categoria_id = Column(ForeignKey("categoria.id"), nullable=False)
    perfil_id = Column(ForeignKey("perfil.id"), nullable=False)


class ProdutoModel(BaseModel):
    id: int
    nome: constr(max_length=255)
    categoria_id: int
    perfil_id: int
