import pymysql
from db_config import connect_db
from flask import jsonify, request, Blueprint

compra_bp = Blueprint("compra", __name__)

@compra_bp.route("/compra")
def user():
    try:
            conn = connect_db()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("SELECT * FROM compra")
            rows = cur.fetchall()
            conn.close()
            resp = jsonify(rows)
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)
        return e

@compra_bp.route("/compra/<id>")
def getbyid_compra(id):
    try:
            conn = connect_db()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("""SELECT * FROM compra 
                        WHERE idcompra = %s""",
                        (id))
            rows = cur.fetchone()
            conn.close()
            resp = jsonify(rows)
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)
        return e

@compra_bp.route("/compra", methods=["POST"])
def nova_compra():
    try:
        compra = request.json
        conn = connect_db()
        cursor = conn.cursor()

        #pegar os dados do JSON
        numeronf = compra["numeronf"]
        data = compra["data"]
        quantidade = compra["quantidade"]
        valor = compra["valor"]
        idfornecedor = compra["idfornecedor"]
        idproduto = compra["idproduto"]

        #insere no BD
        cursor.execute("""
                        INSERT INTO compra
                       (numeronf, data, quantidade, valor, idfornecedor, idproduto)
                       VALUES (%s, %s, %s, %s, %s, %s)
                       """, 
                       (numeronf, data, quantidade, valor, idfornecedor, idproduto)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "inserido!!"})
    except Exception as e:
        print(e)
        return e


@compra_bp.route("/compra/<id>", methods=["PUT"])
def alterar_compra(id):
    try:
        compra = request.json
        conn = connect_db()
        cursor = conn.cursor()

        #pegar os dados do JSON
        numeronf = compra["numeronf"]
        data = compra["data"]
        quantidade = compra["quantidade"]
        valor = compra["valor"]
        idfornecedor = compra["idfornecedor"]
        idproduto = compra["idproduto"]

        #insere no BD
        cursor.execute("""
                        UPDATE compra
                       SET numeronf = %s, data = %s, 
                       quantidade = %s, valor = %s, idfornecedor = %s, idproduto = %s
                       WHERE idcompra = %s
                       """, 
                       (numeronf, data, quantidade, valor, idfornecedor, idproduto, id)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "alterado!!"})
    except Exception as e:
        print(e)
        return e
    


@compra_bp.route("/compra/<id>", methods=["DELETE"])
def excluir_compra(id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        #insere no BD
        cursor.execute("""
                        DELETE FROM compra
                       WHERE idcompra = %s
                       """, 
                       (id)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "excluido!!"})
    except Exception as e:
        print(e)
        return e   