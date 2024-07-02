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
        conta = request.json
        conn = connect_db()
        cursor = conn.cursor()

        # pegar os dados do JSON
        idpagar = conta["idpagar"]
        data = conta["data"]
        valor = conta["valor"]
        vencimento = conta["vencimento"]
        pagamento = conta["vencimento"]
        valorpago = conta["valorpago"]
        idfornecedor = conta["idfornecedor"]
        # insere no BD
        cursor.execute("""
                        INSERT INTO conta_pagar
                       (idpagar, data, valor, vencimento, pagamento, valorpago, idfornecedor)
                       VALUES (%s, %s, %s, %s, %s, %s, %s)
                       
                       """,
                       (idpagar, data, valor, vencimento, pagamento, valorpago, idfornecedor)
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
        print("PUT")
        conta = request.json
        print(conta)
        conn = connect_db()
        cursor = conn.cursor()

        # pegar os dados do JSON
        idpagar =id
        data = conta["data"]
        valor = conta["valor"]
        vencimento = conta["vencimento"]
        pagamento = conta["vencimento"]
        valorpago = conta["valorpago"]
        idfornecedor = conta["idfornecedor"]

        # insere no BD
        cursor.execute("""
                        UPDATE conta_pagar
                       SET  data = %s, 
                       vencimento = %s, pagamento = %s, valor = %s, valorpago = %s,
                        idfornecedor = %s
                       WHERE idpagar = %s
                       """,
                       (data, vencimento, pagamento, valor, valorpago, idfornecedor, id)
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
                        DELETE FROM conta_pagar
                       WHERE idpagar = %s
                       """,
                       (id)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message": "excluido!!"})
    except Exception as e:
        print(e)
        return e
