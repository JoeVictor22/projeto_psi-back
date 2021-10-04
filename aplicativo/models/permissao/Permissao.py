from sqlalchemy import Column, Integer
from pydantic import BaseModel
from aplicativo.database import Base


class Permissao(Base):
    __tablename__ = "permissao"
    id = Column(Integer, primary_key=True, nullable=False)


class PermissaoModel(BaseModel):
    id: int
