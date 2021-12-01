from typing import Dict
from dataclasses import dataclass

import ujson

SUCCESS = "Operação realizada com sucesso"
ERROR = "Ocorreu um erro"


@dataclass
class Respostas:
    resposta: Dict
    codigo: int = 400

    @staticmethod
    def retorno_generico(dicionario: dict, codigo=200):
        return Respostas(resposta=dicionario, codigo=codigo)

    @staticmethod
    def mensagem_generica(mensagem: str = SUCCESS, codigo=200):
        return Respostas(resposta={"message": mensagem}, codigo=codigo)

    @staticmethod
    def erro_generico(mensagem: str = ERROR, codigo=400):
        return Respostas(resposta={"error": mensagem}, codigo=codigo)

    @property
    def json(self):
        return ujson.dumps(self.resposta), self.codigo
