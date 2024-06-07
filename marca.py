import pymysql
from db_config import connect_db
from flask import jsonify, request, Blueprint

marca_bp = Blueprint("marca", __name__)

@marca_bp.route("/marca")
def user():
    try:
            conn = connect_db()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("SELECT * FROM marca")
            rows = cur.fetchall()
            conn.close()
            resp = jsonify(rows)
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)
        return e

@marca_bp.route("/marca/<id>")
def getbyid_marca(id):
    try:
            conn = connect_db()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("""SELECT * FROM marca 
                        WHERE idmarca = %s""",
                        (id))
            rows = cur.fetchone()
            conn.close()
            resp = jsonify(rows)
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)
        return e

@marca_bp.route("/marca", methods=["POST"])
def nova_marca():
    try:
            marca = request.json
            conn = connect_db()
            cursor = conn.cursor()

            #pegar os dados do JSON
            nome_marca = marca["nomemarca"]
            logo = marca["logo"]
            pais_origem = marca["pais_origem"]
            telefone_sac = marca["telefone_sac"]

            #insere no BD
            cursor.execute("""
                            INSERT INTO marca
                        (nomemarca, logo, pais_origem, telefone_sac)
                        VALUES (%s, %s, %s, %s)
                        """, 
                        (nome_marca, logo, pais_origem, telefone_sac)
                        )
            conn.commit()
            conn.close()

            return jsonify({"message" : "inserido!!"})
    except Exception as e:
        print(e)
        return e


@marca_bp.route("/marca/<id>", methods=["PUT"])
def alterar_marca(id):
    try:
            marca = request.json
            conn = connect_db()
            cursor = conn.cursor()

            #pegar os dados do JSON
            nome_marca = marca["nomemarca"]
            logo = marca["logo"]
            pais_origem = marca["pais_origem"]
            telefone_sac = marca["telefone_sac"]

            #insere no BD
            cursor.execute("""
                            UPDATE marca
                        SET nomemarca = %s, logo = %s, 
                        pais_origem = %s, telefone_sac = %s
                        WHERE idmarca = %s
                        """, 
                        (nome_marca, logo, pais_origem, telefone_sac, id)
                        )
            conn.commit()
            conn.close()

            return jsonify({"message" : "alterado!!"})
    except Exception as e:
        print(e)
        return e
    


@marca_bp.route("/marca/<id>", methods=["DELETE"])
def excluir_marca(id):
    try:
            conn = connect_db()
            cursor = conn.cursor()

            #insere no BD
            cursor.execute("""
                            DELETE FROM marca
                        WHERE idmarca = %s
                        """, 
                        (id)
                        )
            conn.commit()
            conn.close()

            return jsonify({"message" : "excluido!!"})
    except Exception as e:
        print(e)
        return e    
