from sqlalchemy import insert
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash
from aplicativo.models.perfil import Perfil
from aplicativo.models.usuario import Usuario
from aplicativo.models.produto import Produto
from aplicativo import app

usuario = {
    "nome": [
        "Benjamin Mcleod",
        "Callen Ball",
        "Saffa Stone",
        "Efe Hirst",
        "Curtis Guzman",
    ],
    "email": [
        "b2enjamin@mail.com",
        "c1allen@mail.com",
        "s14affa@mail.com",
        "ef4e@mail.com",
        "cu5rtis@mail.com",
    ],
    "senha": ["senha", "senha", "senha", "senha", "senha"],
    "grupo_id": [2, 2, 2, 2, 2],
}

perfil = {
    "usuario_id": [1, 2, 3, 4, 5],
    "nome": ["Mcleod's", "Ball's", "Stone's", "Hirst's", "Guzman's"],
    "endereco": [
        "Rua 2",
        "Rua 3",
        "Rua 4",
        "Rua 5",
        "Rua 6",
    ],
    "cidade_id": ["fortaleza", "camocim", "camocim", "fortaleza", "fortaleza"],
    "geolocalizacao": [0, 0, 0, 0, 0],
    "email": [
        "mcleods@mail.com",
        "balls@mail.com",
        "stones@mail.com",
        "hirsts@mail.com",
        "guzmans@mail.com",
    ],
    "cnpj_cpf": [0, 0, 0, 0, 0],
}

produto = {
    "nome": ["hotdog", "cheeseburguer", "tampico", "sorvete", "pastel"],
    "preco": [2.50, 4.5, 4.0, 3.0, 3.0],
    "perfil_id": [1, 2, 3, 4, 5],
}

with app.app_context():
    for idx in range(len(usuario["nome"])):
        novo_registro = dict(
            nome=usuario["nome"][idx],
            email=usuario["email"][idx],
            senha=generate_password_hash(usuario["senha"][idx], method="sha256"),
            grupo_id=usuario["grupo_id"][idx],
        )
        stmt = insert(Usuario).values(novo_registro)
        try:
            app.session.execute(stmt)
            app.session.commit()

        except SQLAlchemyError as e:
            raise e

    for idx in range(len(perfil["nome"])):
        novo_registro = dict(
            usuario_id=perfil["usuario_id"][idx],
            nome=perfil["nome"][idx],
            endereco=perfil["endereco"][idx],
            cidade_id=perfil["cidade_id"][idx],
            geolocalizacao=perfil["geolocalizacao"][idx],
            email=perfil["email"][idx],
            cnpj_cpf=perfil["cnpj_cpf"][idx],
        )

        stmt = insert(Perfil).values(novo_registro)
        try:
            app.session.execute(stmt)
            app.session.commit()

        except SQLAlchemyError as e:
            raise e
    for idx in range(len(produto["nome"])):
        novo_registro = dict(
            nome=produto["nome"][idx],
            preco=produto["preco"][idx],
            perfil_id=produto["perfil_id"][idx],
        )

        stmt = insert(Produto).values(novo_registro)
        try:
            app.session.execute(stmt)
            app.session.commit()

        except SQLAlchemyError as e:
            raise e
