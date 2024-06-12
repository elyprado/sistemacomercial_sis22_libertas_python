import pymysql
from db_config import connect_db
from flask import jsonify, request, Blueprint

contaspagar_bp = Blueprint("contasapagar", __name__)


@contaspagar_bp.route("/contasapagar")
def user():
    try:
        conn = connect_db()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM conta_pagar")
        rows = cur.fetchall()
        conn.close()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return e


@contaspagar_bp.route("/contasapagar/<id>")
def getbyid_usuario(id):
    try:
        conn = connect_db()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("""SELECT * FROM conta_pagar 
                        WHERE idpagar = %s""",
                    (id))
        rows = cur.fetchone()
        conn.close()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return e


@contaspagar_bp.route("/contasapagar", methods=["POST"])
def novo_usuario():
    try:
        usuario = request.json
        conn = connect_db()
        cursor = conn.cursor()

        # pegar os dados do JSON
        nome = usuario["nome"]
        email = usuario["email"]
        senha = usuario["senha"]
        telefone = usuario["telefone"]

        # insere no BD
        cursor.execute("""
                        INSERT INTO 
                       (nome, email, senha, telefone)
                       VALUES (%s, %s, %s, %s)
                       """,
                       (nome, email, senha, telefone)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message": "inserido!!"})
    except Exception as e:
        print(e)
        return e


@contaspagar_bp.route("/contasapagar/<id>", methods=["PUT"])
def alterar_usuario(id):
    try:
        usuario = request.json
        conn = connect_db()
        cursor = conn.cursor()

        # pegar os dados do JSON
        nome = usuario["nome"]
        email = usuario["email"]
        senha = usuario["senha"]
        telefone = usuario["telefone"]

        # insere no BD
        cursor.execute("""
                        UPDATE usuario
                       SET nome = %s, email = %s, 
                       senha = %s, telefone = %s
                       WHERE idusuario = %s
                       """,
                       (nome, email, senha, telefone, id)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message": "alterado!!"})
    except Exception as e:
        print(e)
        return e


@contaspagar_bp.route("/contasapagar/<id>", methods=["DELETE"])
def excluir_usuario(id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # insere no BD
        cursor.execute("""
                        DELETE FROM usuario
                       WHERE idusuario = %s
                       """,
                       (id)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message": "excluido!!"})
    except Exception as e:
        print(e)
        return e
