import pymysql
from db_config import connect_db
from flask import jsonify, request, Blueprint

cidade_bp = Blueprint("cidade", __name__)

@cidade_bp.route("/cidade")
def cidade():
    try:
            conn = connect_db()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("SELECT * FROM cidade")
            rows = cur.fetchall()
            conn.close()
            resp = jsonify(rows)
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)
        return e

@cidade_bp.route("/cidade/<id>")
def getbyid_cidade(id):
    try:
            conn = connect_db()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("""SELECT * FROM cidade 
                        WHERE idcidade = %s""",
                        (id))
            rows = cur.fetchone()
            conn.close()
            resp = jsonify(rows)
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)
        return e

@cidade_bp.route("/cidade", methods=["POST"])
def novo_usuario():
    try:
        cidade = request.json
        conn = connect_db()
        cursor = conn.cursor()

        #pegar os dados do JSON
        nomecidade = cidade["nomecidade"]
        uf = cidade["uf"]
        codigo_ibge = cidade["codigo_ibge"]
        população = cidade["população"]
        latitude = cidade["latitude"]
        longitude = cidade["longitude"]


        #insere no BD
        cursor.execute("""
                        INSERT INTO cidade 
                       (nomecidade, uf, codigo_ibge, população, latitude, longitude)
                       VALUES (%s, %s, %s, %s, %s, %s)
                       """, 
                       (nomecidade, uf, codigo_ibge, população, latitude, longitude)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "inserido!!"})
    except Exception as e:
        print(e)
        return e


@cidade_bp.route("/cidade/<id>", methods=["PUT"])
def alterar_cidade(id):
    try:
        cidade = request.json
        conn = connect_db()
        cursor = conn.cursor()

        #pegar os dados do JSON
        nomecidade = cidade["nomecidade"]
        uf = cidade["uf"]
        codigo_ibge = cidade["codigo_ibge"]
        população = cidade["população"]
        latitude = cidade["latitude"]
        longitude = cidade["longitude"]

        #insere no BD
        cursor.execute("""
                        UPDATE cidade
                       SET nomecidade = %s, uf = %s , codigo_ibge = %s, 
                       população = %s, latitude = %s, longitude = %s
                       WHERE idcidade = %s
                       """, 
                       (nomecidade, uf, codigo_ibge, população, latitude, longitude, id)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "alterado!!"})
    except Exception as e:
        print(e)
        return e
    


@cidade_bp.route("/cidade/<id>", methods=["DELETE"])
def excluir_cidade(id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        #insere no BD
        cursor.execute("""
                        DELETE FROM cidade
                       WHERE idcidade = %s
                       """, 
                       (id)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "excluido!!"})
    except Exception as e:
        print(e)
        return e    