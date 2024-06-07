
import pymysql
from db_config import connect_db
from flask import jsonify, request, Blueprint

produto_bp = Blueprint("produto", __name__)

@produto_bp.route("/produto")
def user():
    try:
            conn = connect_db()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("SELECT * FROM produto")
            rows = cur.fetchall()
            conn.close()
            resp = jsonify(rows)
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)
        return e

@produto_bp.route("/produto/<id>")
def getbyid_produto(id):
    try:
            conn = connect_db()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("""SELECT * FROM produto
                        WHERE idproduto = %s""",
                        (id))
            rows = cur.fetchone()
            conn.close()
            resp = jsonify(rows)
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)
        return e

@prodduto_bp.route("/produto", methods=["POST"])
def novo_produto():
    try:
        produto = request.json
        conn = connect_db()
        cursor = conn.cursor()

        #pegar os dados do JSON
        desricao = produto["descricao"]
        preco_custo = produto["precocusto"]
        preco_venda = produto["precovenda"]
        saldo_estoque = produto["saldoestoque"]
        codbarras = produto["codbarras"]
        idmarca = produto["idmarca"]

        #insere no BD
        cursor.execute("""
                        INSERT INTO produto
                       (descricao, precocusto, precovenda, saldoestoque, codbarras, idmarca)
                       VALUES (%s, %s, %s, %s, %s, %s)
                       """, 
                       (descricao, precocusto, precovenda, saldoestoque, codbarras, idmarca)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "inserido!!"})
    except Exception as e:
        print(e)
        return e


@produto_bp.route("/produto/<id>", methods=["PUT"])
def alterar_produto(id):
    try:
        produto = request.json
        conn = connect_db()
        cursor = conn.cursor()

        #pegar os dados do JSON
        desricao = produto["descricao"]
        preco_custo = produto["precocusto"]
        preco_venda = produto["precovenda"]
        saldo_estoque = produto["saldoestoque"]
        codbarras = produto["codbarras"]
        idmarca = produto["idmarca"]

        #insere no BD
        cursor.execute("""
                        UPDATE produto
                       SET descricao = %s, precocusto = %s, 
                       precovenda = %s, saldoestoque = %s,
                       codbarras = %s, idmarca = %s
                       WHERE idproduto = %s
                       """, 
                       (descrica, precocusto, precovenda, saldoestoque, codbarras, idmarca)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "alterado!!"})
    except Exception as e:
        print(e)
        return e
    


@produto_bp.route("/produto/<id>", methods=["DELETE"])
def excluir_produto(id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        #insere no BD
        cursor.execute("""
                        DELETE FROM produto
                       WHERE idproduto = %s
                       """, 
                       (id)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "excluido!!"})
    except Exception as e:
        print(e)
        return e    



from flask import Flask, send_from_directory
from usuario import usuario_bp
from produto import produto_bp
import os

app = Flask(__name__,   
static_url_path='', 
            static_folder='static')
app.register_blueprint(usuario_bp)
app.register_blueprint(produto_bp)


@app.route("/")
def home():
    return send_from_directory(os.path.join(app.root_path,'static'), 'index.html')

if __name__ == "__main__":
    app.run()       

