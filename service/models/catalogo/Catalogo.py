from sqlalchemy import Column, Integer
from service import db
from pydantic import BaseModel

class Catalogo(db.model):
    __tablename__ = 'catalogo'
    id = Column(Integer, primary_key=True, nullable=False)

class CatalogoModel(BaseModel):
    id: int