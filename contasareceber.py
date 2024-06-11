import pymysql
from db_config import connect_db
from flask import jsonify, request, Blueprint

conta_receber_bp = Blueprint("conta_receber", __name__)

@conta_receber_bp.route("/conta_receber", methods=["GET"])
def listar_contas():
    try:
        pesquisa = request.args.get('pesquisa', default='', type=str)
        conn = connect_db()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        if pesquisa:
            cur.execute("SELECT * FROM conta_receber WHERE data LIKE %s OR valor LIKE %s OR vencimento LIKE %s OR pagamento LIKE %s OR valorpago LIKE %s OR idcliente LIKE %s",
                        ('%' + pesquisa + '%', '%' + pesquisa + '%', '%' + pesquisa + '%', '%' + pesquisa + '%', '%' + pesquisa + '%', '%' + pesquisa + '%'))
        else:
            cur.execute("SELECT * FROM conta_receber")
        rows = cur.fetchall()
        conn.close()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


@conta_receber_bp.route("/conta_receber/<int:id>", methods=["GET"])
def obter_conta_por_id(id):
    try:
        conn = connect_db()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM conta_receber WHERE idreceber = %s", (id,))
        row = cur.fetchone()
        conn.close()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500

@conta_receber_bp.route("/conta_receber", methods=["POST"])
def nova_conta():
    try:
        conta = request.json
        conn = connect_db()
        cursor = conn.cursor()

        data = conta["data"]
        valor = conta["valor"]
        vencimento = conta["vencimento"]
        pagamento = conta["pagamento"]
        valorpago = conta["valorpago"]
        idcliente = conta["idcliente"]

        cursor.execute("""
            INSERT INTO conta_receber
            (data, valor, vencimento, pagamento, valorpago, idcliente)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (data, valor, vencimento, pagamento, valorpago, idcliente))
        conn.commit()
        conn.close()

        return jsonify({"message": "inserido!!"}), 201
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500

@conta_receber_bp.route("/conta_receber/<int:id>", methods=["PUT"])
def alterar_conta(id):
    try:
        conta = request.json
        conn = connect_db()
        cursor = conn.cursor()

        data = conta["data"]
        valor = conta["valor"]
        vencimento = conta["vencimento"]
        pagamento = conta["pagamento"]
        valorpago = conta["valorpago"]
        idcliente = conta["idcliente"]

        cursor.execute("""
            UPDATE conta_receber
            SET data = %s, valor = %s, vencimento = %s, pagamento = %s, valorpago = %s, idcliente = %s
            WHERE idreceber = %s
        """, (data, valor, vencimento, pagamento, valorpago, idcliente, id))
        conn.commit()
        conn.close()

        return jsonify({"message": "alterado!!"}), 200
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500

@conta_receber_bp.route("/conta_receber/<int:id>", methods=["DELETE"])
def excluir_conta(id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM conta_receber WHERE idreceber = %s", (id,))
        conn.commit()
        conn.close()

        return jsonify({"message": "excluido!!"}), 200
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500
