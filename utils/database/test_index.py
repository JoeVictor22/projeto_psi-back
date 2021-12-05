from aplicativo import app


def usuario_add():
    stm = "INSERT INTO usuario(nome, email, senha, grupo_id) SELECT 'Nome' || RANDOM()::TEXT, 'Email@'|| RANDOM()::TEXT,  md5(RANDOM()::TEXT), CASE WHEN RANDOM() < 0.5 THEN 1 ELSE 2 END FROM generate_series(1, 10000) i;"

    try:
        app.session.excute(stm)
        print("ok")
    except Exception:
        print("bad")
