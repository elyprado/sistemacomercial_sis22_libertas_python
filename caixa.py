import pymysql
from db_config import connect_db
from flask import jsonify, request, Blueprint

caixa_bp = Blueprint("caixa", __name__)

@caixa_bp.route("/caixa")
def user():
    try:
            conn = connect_db()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("SELECT * FROM caixa")
            rows = cur.fetchall()
            conn.close()
            resp = jsonify(rows)
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)
        return e

@caixa_bp.route("/caixa/<id>")
def getbyid_caixa(id):
    try:
            conn = connect_db()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("""SELECT * FROM caixa 
                        WHERE idcaixa = %s""",
                        (id))
            rows = cur.fetchone()
            conn.close()
            resp = jsonify(rows)
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)
        return e

@caixa_bp.route("/caixa", methods=["POST"])
def novo_caixa():
    try:
        caixa = request.json
        conn = connect_db()
        cursor = conn.cursor()

        #pegar os dados do JSON
        data = caixa["data"]
        descricao = caixa["descricao"]
        valor = caixa["valor"]
        debitocredito = caixa["debitocredito"]

        #insere no BD
        cursor.execute("""
                        INSERT INTO caixa
                       (data, descricao, valor, debitocredito)
                       VALUES (%s, %s, %s, %s)
                       """, 
                       (data, descricao, valor, debitocredito)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "inserido!!"})
    except Exception as e:
        print(e)
        return e


@caixa_bp.route("/caixa/<id>", methods=["PUT"])
def alterar_caixa(id):
    try:
        caixa = request.json
        conn = connect_db()
        cursor = conn.cursor()

        #pegar os dados do JSON
        data = caixa["data"]
        descricao = caixa["descricao"]
        valor = caixa["valor"]
        debitocredito = caixa["debitocredito"]

        #insere no BD
        cursor.execute("""
                        UPDATE caixa
                       SET data = %s, descricao = %s, 
                       valor = %s, debitocredito = %s
                       WHERE idcaixa = %s
                       """, 
                       (data, descricao, valor, debitocredito, id)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "alterado!!"})
    except Exception as e:
        print(e)
        return e
    


@caixa_bp.route("/caixa/<id>", methods=["DELETE"])
def excluir_caixa(id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        #insere no BD
        cursor.execute("""
                        DELETE FROM caixa
                       WHERE idcaixa = %s
                       """, 
                       (id)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "excluido!!"})
    except Exception as e:
        print(e)
        return e    
