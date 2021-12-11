import enum

from pydantic import BaseModel, constr


class Cidade(enum.Enum):
    fortaleza = 1
    camocim = 2


class CidadeModel(BaseModel):
    id: int
    nome: constr(max_length=255)
