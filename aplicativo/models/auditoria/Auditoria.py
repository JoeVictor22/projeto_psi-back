from sqlalchemy import Column, Integer
from pydantic import BaseModel, constr
from aplicativo import db


class Auditoria(db.Model):
    __tablename__ = "auditoria"
    id = Column(Integer, primary_key=True, nullable=False)


class AuditoriaModel(BaseModel):
    id: int
    public_key: constr(max_length=20)
    name: constr(max_length=63)
