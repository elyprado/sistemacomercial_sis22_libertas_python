import pymysql
from db_config import connect_db
from flask import jsonify, request, Blueprint

venda_bp = Blueprint("venda", __name__)

@venda_bp.route("/venda")
def getVendas():
    try:
            conn = connect_db()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("SELECT * FROM venda")
            rows = cur.fetchall()
            conn.close()
            resp = jsonify(rows)
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)
        return e

@venda_bp.route("/venda/<id>")
def getbyid_venda(id):
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    try:
            conn = connect_db()
            print("ID: ", id)
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("""SELECT * FROM venda 
                        WHERE idvenda = %s""",
                        (id))
            rows = cur.fetchone()
            conn.close()
            resp = jsonify(rows)
            resp.status_code=200
            print(resp)
            return resp
    except Exception as e:
        print(e)
        return e

@venda_bp.route("/venda", methods=["POST"])
def nova_venda():
    try:
        venda = request.json
        conn = connect_db()
        cursor = conn.cursor()

        #pegar os dados do JSON
        numeronf = venda["numeronf"]
        data = venda["data"]
        quantidade = venda["quantidade"]
        valor = venda["valor"]
        comissao = venda["comissao"]
        idcliente = venda["idcliente"]
        idproduto = venda["idproduto"]
        idvendedor = venda["idvendedor"]
        print("NF",numeronf)
        print("Venda: ", venda)

        #insere no BD
        cursor.execute("""
                        INSERT INTO venda
                       (numeronf, data, quantidade, valor, comissao, idcliente, idproduto, idvendedor)
                       VALUES (%s, %s, %s, %s,%s, %s, %s, %s)
                       """, 
                       (numeronf, data, quantidade, valor, comissao, idcliente, idproduto, idvendedor)
                       )


        conn.commit()
        conn.close()

        return jsonify({"message" : "inserido!!"})
    except Exception as e:
        print(e)
        return e


@venda_bp.route("/venda/<id>", methods=["PUT"])
def alterar_venda(id):
    try:
        venda = request.json
        conn = connect_db()
        cursor = conn.cursor()

        #pegar os dados do JSON
        numeronf = venda["numeronf"]
        data = venda["data"]
        quantidade = venda["quantidade"]
        valor = venda["valor"]
        comissao = venda["comissao"]
        idcliente = venda["idcliente"]
        idproduto = venda["idproduto"]
        idvendedor = venda["idvendedor"]
        #insere no BD
        cursor.execute("""
                        UPDATE venda SET numeronf=%s, data=%s, quantidade=%s ,valor=%s, comissao=%s, idcliente=%s, idproduto=%s, idvendedor=%s WHERE idvenda=%s
                       """, 
                       (numeronf, data, quantidade, valor, comissao, idcliente, idproduto, idvendedor, id)
                       )
        conn.commit()
        conn.close()
       
        return jsonify({"message" : "alterado!!"})
    except Exception as e:
        print(e)
        
        return e
    


@venda_bp.route("/venda/<id>", methods=["DELETE"])
def excluir_venda(id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        #insere no BD
        cursor.execute("""
                        DELETE FROM venda WHERE idvenda = %s
                       """, 
                       (id)
                       )
          
        conn.commit()
        conn.close()

        return jsonify({"message" : "excluido!!"})
    except Exception as e:
        print(e)
        return e    
