import pymysql
from db_config import connect_db
from flask import jsonify, request, Blueprint

fornecedor_bp = Blueprint("fornecedor", __name__)

@fornecedor_bp.route("/fornecedor")
def user():
    try:
            conn = connect_db()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("SELECT * FROM fornecedor")
            rows = cur.fetchall()
            conn.close()
            resp = jsonify(rows)
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)
        return e

@fornecedor_bp.route("/fornecedor/<id>")
def getbyid_fornecedor(id):
    try:
            conn = connect_db()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("""SELECT * FROM fornecedor 
                        WHERE idfornecedor = %s""",
                        (id))
            rows = cur.fetchone()
            conn.close()
            resp = jsonify(rows)
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)
        return e

@fornecedor_bp.route("/fornecedor", methods=["POST"])
def novo_fornecedor():
    try:
        fornecedor = request.json
        conn = connect_db()
        cursor = conn.cursor()

        #pegar os dados do JSON
        nome = fornecedor["nome"]
        cnpj = fornecedor["cnpj"]
        logradouro = fornecedor["logradouro"]
        numero = fornecedor["numero"]
        bairro = fornecedor["bairro"]
        cep = fornecedor["cep"]
        telefone = fornecedor["telefone"]
        idcidade = fornecedor["idcidade"]

        #insere no BD
        cursor.execute("""
                        INSERT INTO fornecedor
                       (nome, cnpj, logradouro, numero, bairro, cep, telefone, idcidade)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                       """, 
                       (nome, cnpj, logradouro, numero, bairro, cep, telefone, idcidade)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "inserido!!"})
    except Exception as e:
        print(e)
        return e


@fornecedor_bp.route("/fornecedor/<id>", methods=["PUT"])
def alterar_fornecedor(id):
    try:
        fornecedor = request.json
        conn = connect_db()
        cursor = conn.cursor()

        #pegar os dados do JSON
        nome = fornecedor["nome"]
        cnpj = fornecedor["cnpj"]
        logradouro = fornecedor["logradouro"]
        numero = fornecedor["numero"]
        bairro = fornecedor["bairro"]
        cep = fornecedor["cep"]
        telefone = fornecedor["telefone"]
        idcidade = fornecedor["idcidade"]

        #insere no BD
        cursor.execute("""
                       UPDATE
                        fornecedor
                       SET 
                        nome = %s, 
                        cnpj = %s, 
                        logradouro = %s,
                        numero = %s,
                        bairro = %s,
                        cep = %s,
                        telefone = %s,
                        idcidade = %s
                       WHERE
                        idfornecedor = %s
                       """, 
                       (nome, cnpj, logradouro, numero, bairro, cep, telefone, idcidade, id)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "alterado!!"})
    except Exception as e:
        print(e)
        return e
    


@fornecedor_bp.route("/fornecedor/<id>", methods=["DELETE"])
def excluir_fornecedor(id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        #insere no BD
        cursor.execute("""
                        DELETE FROM
                            fornecedor
                        WHERE
                            idfornecedor = %s
                       """, 
                       (id)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "excluido!!"})
    except Exception as e:
        print(e)
        return e    
