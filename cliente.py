import pymysql
from db_config import connect_db
from flask import jsonify, request, Blueprint

cliente_bp = Blueprint("cliente", __name__)

@cliente_bp.route("/cliente")
def user():
    try:
            conn = connect_db()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("SELECT * FROM cliente")
            rows = cur.fetchall()
            conn.close()
            resp = jsonify(rows)
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)
        return e

@cliente_bp.route("/cliente/<id>")
def getbyid_cliente(id):
    try:
            conn = connect_db()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("""SELECT * FROM cliente 
                        WHERE idcliente = %s""",
                        (id))
            rows = cur.fetchone()
            conn.close()
            resp = jsonify(rows)
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)
        return e

@cliente_bp.route("/cliente", methods=["POST"])
def novo_cliente():
    try:
        cliente = request.json
        conn = connect_db()
        cursor = conn.cursor()

        #pegar os dados do JSON
        nome = cliente["nome"]
        cpf = cliente["cpf"]
        logradouro = cliente["logradouro"]
        numero = cliente["numero"]
        bairro = cliente["bairro"]
        cep = cliente["cep"]
        telefone = cliente["telefone"]
        idcidade = cliente["idcidade"]

        #insere no BD
        cursor.execute("""
                        INSERT INTO cliente
                       (nome, cpf, logradouro, numero, bairro, cep, telefone, idcidade)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                       """, 
                       (nome, cpf, logradouro, numero, bairro, cep, telefone, idcidade)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "inserido!!"})
    except Exception as e:
        print(e)
        return e


@cliente_bp.route("/cliente/<id>", methods=["PUT"])
def alterar_cliente(id):
    try:
        cliente = request.json
        conn = connect_db()
        cursor = conn.cursor()

        #pegar os dados do JSON
        nome = cliente["nome"]
        cpf = cliente["cpf"]
        logradouro = cliente["logradouro"]
        numero = cliente["numero"]
        bairro = cliente["bairro"]
        cep = cliente["cep"]
        telefone = cliente["telefone"]
        idcidade = cliente["idcidade"]

        #insere no BD
        cursor.execute("""
                        UPDATE cliente
                       SET nome = %s, cpf = %s, 
                       logradouro = %s, numero = %s, bairro = %s, cep = %s, idcidade = %s
                       WHERE idcliente = %s
                       """, 
                       (nome, cpf, logradouro, numero, bairro, cep, telefone, idcidade)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "alterado!!"})
    except Exception as e:
        print(e)
        return e
    


@cliente_bp.route("/cliente/<id>", methods=["DELETE"])
def excluir_cliente(id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        #insere no BD
        cursor.execute("""
                        DELETE FROM cliente
                       WHERE idcliente = %s
                       """, 
                       (id)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "excluido!!"})
    except Exception as e:
        print(e)
        return e    
