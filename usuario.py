import pymysql
from db_config import connect_db
from flask import jsonify, request, Blueprint

usuario_bp = Blueprint("usuario", __name__)

@usuario_bp.route("/usuario")
def user():
    try:
            conn = connect_db()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("SELECT * FROM usuario")
            rows = cur.fetchall()
            conn.close()
            resp = jsonify(rows)
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)
        return e

@usuario_bp.route("/usuario/<id>")
def getbyid_usuario(id):
    try:
            conn = connect_db()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("""SELECT * FROM usuario 
                        WHERE idusuario = %s""",
                        (id))
            rows = cur.fetchone()
            conn.close()
            resp = jsonify(rows)
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)
        return e

@usuario_bp.route("/usuario", methods=["POST"])
def novo_usuario():
    try:
        usuario = request.json
        conn = connect_db()
        cursor = conn.cursor()

        #pegar os dados do JSON
        nome = usuario["nome"]
        email = usuario["email"]
        senha = usuario["senha"]
        telefone = usuario["telefone"]

        #insere no BD
        cursor.execute("""
                        INSERT INTO usuario
                       (nome, email, senha, telefone)
                       VALUES (%s, %s, %s, %s)
                       """, 
                       (nome, email, senha, telefone)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "inserido!!"})
    except Exception as e:
        print(e)
        return e


@usuario_bp.route("/usuario/<id>", methods=["PUT"])
def alterar_usuario(id):
    try:
        usuario = request.json
        conn = connect_db()
        cursor = conn.cursor()

        #pegar os dados do JSON
        nome = usuario["nome"]
        email = usuario["email"]
        senha = usuario["senha"]
        telefone = usuario["telefone"]

        #insere no BD
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

        return jsonify({"message" : "alterado!!"})
    except Exception as e:
        print(e)
        return e
    


@usuario_bp.route("/usuario/<id>", methods=["DELETE"])
def excluir_usuario(id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        #insere no BD
        cursor.execute("""
                        DELETE FROM usuario
                       WHERE idusuario = %s
                       """, 
                       (id)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "excluido!!"})
    except Exception as e:
        print(e)
        return e    
