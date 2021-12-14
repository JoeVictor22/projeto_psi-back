from sqlalchemy import insert
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash
from aplicativo.models.perfil import Perfil
from aplicativo.models.usuario import Usuario
from aplicativo.models.produto import Produto

from aplicativo import app

usuarios = [
    {
        "nome": "Benjamin Mcleod",
        "email": "benjamin@mail.com",
        "senha": "senha",
        "grupo_id": 2,
    },
    {
        "nome": "Callen Ball",
        "email": "callen@mail.com",
        "senha": "senha",
        "grupo_id": 2,
    },
    {"nome": "Saffa Stone", "email": "saffa@mail.com", "senha": "senha", "grupo_id": 2},
    {"nome": "Efe Hirst", "email": "efe@mail.com", "senha": "senha", "grupo_id": 2},
    {
        "nome": "Curtis Guzman",
        "email": "curtis@mail.com",
        "senha": "senha",
        "grupo_id": 2,
    },
]

perfils = [
    {
        "usuario_id": 1,
        "nome": "Mcleod's",
        "endereco": "Rua 2",
        "cidade_id": "fortaleza",
        "geolocalizacao": 0,
        "email": "mcleods@mail.com",
        "cnpj_cpf": 0,
        "telefone": "85986826485",
    },
    {
        "usuario_id": 2,
        "nome": "Ball's",
        "endereco": "Rua 3",
        "cidade_id": "camocim",
        "geolocalizacao": 0,
        "email": "balls@mail.com",
        "cnpj_cpf": 0,
        "telefone": "85986826485",
    },
    {
        "usuario_id": 3,
        "nome": "Stone's",
        "endereco": "Rua 4",
        "cidade_id": "camocim",
        "geolocalizacao": 0,
        "email": "stones@mail.com",
        "cnpj_cpf": 0,
        "telefone": "85986826485",
    },
    {
        "usuario_id": 4,
        "nome": "Hirst's",
        "endereco": "Rua 5",
        "cidade_id": "fortaleza",
        "geolocalizacao": 0,
        "email": "hirsts@mail.com",
        "cnpj_cpf": 0,
        "telefone": "85986826485",
    },
    {
        "usuario_id": 5,
        "nome": "Guzman's",
        "endereco": "Rua 6",
        "cidade_id": "fortaleza",
        "geolocalizacao": 0,
        "email": "guzmans@mail.com",
        "cnpj_cpf": 0,
        "telefone": "85986826485",
    },
]

produto = [
    {
        "nome": "Hotdog",
        "preco": 2.50,
        "descricao": "O famoso cachorro quente com tudo no capricho.",
        "imagem": "http://4.bp.blogspot.com/-bNRqwCGEBd0/UOyZV0fQQ2I/AAAAAAAAA8g/6wsvYsbwF1A/s1600/2013-01-08+18.46.10.jpg",
    },
    {
        "nome": "Cheeseburguer Duplo",
        "preco": 4.5,
        "descricao": "Um sanduiche no capricho com duas carnes e queijo derretendo.",
        "imagem": "https://i.pinimg.com/736x/9f/15/bb/9f15bb33b2638b424caaa453a6af115b.jpg",
    },
    {
        "nome": "Tampico",
        "preco": 4.0,
        "descricao": "Suco de laranja Tampico geladinho 1L.",
        "imagem": "https://santahelenacenter.com.br/wp-content/uploads/fotos-produtos/59597.jpg",
    },
    {
        "nome": "Sorvete Chocolate",
        "preco": 3.0,
        "descricao": "Sorvete sabor chocolate marca Pardal.",
        "imagem": "https://gironacidade.com.br/wp-content/uploads/2021/07/IMG_4176fi-768x512.png",
    },
    {
        "nome": "Pastel",
        "preco": 3.0,
        "descricao": "Pastel de camarão receita do grande Abelardo.",
        "imagem": "https://pbs.twimg.com/media/CZPeZhIW0AAYwCY.jpg",
    },
]


def add_users():
    for dic in usuarios:
        novo_registro = dict(
            nome=dic["nome"],
            email=dic["email"],
            senha=generate_password_hash(dic["senha"], method="sha256"),
            grupo_id=dic["grupo_id"],
        )
        stmt = insert(Usuario).values(novo_registro)
        try:
            app.session.execute(stmt)
            app.session.commit()

        except SQLAlchemyError as e:
            raise e


def add_perfils():
    for dic in perfils:
        novo_registro = dict(
            usuario_id=dic["usuario_id"],
            nome=dic["nome"],
            endereco=dic["endereco"],
            cidade_id=dic["cidade_id"],
            geolocalizacao=dic["geolocalizacao"],
            email=dic["email"],
            cnpj_cpf=dic["cnpj_cpf"],
            telefone=dic["telefone"],
        )

        stmt = insert(Perfil).values(novo_registro)
        try:
            app.session.execute(stmt)
            app.session.commit()

        except SQLAlchemyError as e:
            raise e


def add_produtos():
    for i in range(len(usuarios)):
        for dic in produto:
            novo_registro = dict(
                nome=dic["nome"],
                preco=dic["preco"],
                imagem=dic["imagem"],
                descricao=dic["descricao"],
                perfil_id=i + 1,
            )

            stmt = insert(Produto).values(novo_registro)
            try:
                app.session.execute(stmt)
                app.session.commit()

            except SQLAlchemyError as e:
                raise e


with app.app_context():

    add_users()
    add_perfils()
    add_produtos()
