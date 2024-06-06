import pymysql
from db_config import connect_db
from flask import jsonify, request, Blueprint

vendedor_bp = Blueprint("vendedor", __name__)

@vendedor_bp.route("/vendedor")
def user():
    try:
            conn = connect_db()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("SELECT * FROM vendedor")
            rows = cur.fetchall()
            conn.close()
            resp = jsonify(rows)
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)
        return e

@vendedor_bp.route("/vendedor/<id>")
def getbyid_vendedor(id):
    try:
            conn = connect_db()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("""SELECT * FROM vendedor
                        WHERE idvendedor = %s""",
                        (id))
            rows = cur.fetchone()
            conn.close()
            resp = jsonify(rows)
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)
        return e

@vendedor_bp.route("/vendedor", methods=["POST"])
def novo_vendedor():
    try:
        vendedor = request.json
        conn = connect_db()
        cursor = conn.cursor()

        #pegar os dados do JSON
        nome = vendedor["nome"]
        cpf = vendedor["cpf"]
        logradouro = vendedor["logradouro"]
        numero = vendedor["numero"]
        bairro = vendedor["bairro"]
        cep = vendedor["cep"]
        telefone = vendedor["telefone"]
        perc_comissao = vendedor["perc_comissao"]
        idcidade = vendedor["idcidade"]

        #insere no BD
        cursor.execute("""
                        INSERT INTO vendedor
                       (nome, cpf, logradouro, numero, bairro, cep, telefone, perc_comissao, idcidade)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                       """, 
                       (nome, cpf, logradouro, numero, bairro, cep, telefone, perc_comissao, idcidade)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "inserido!!"})
    except Exception as e:
        print(e)
        return e


@vendedor_bp.route("/vendedor/<id>", methods=["PUT"])
def alterar_vendedor(id):
    try:
        vendedor = request.json
        conn = connect_db()
        cursor = conn.cursor()

        #pegar os dados do JSON
        nome = vendedor["nome"]
        cpf = vendedor["cpf"]
        logradouro = vendedor["logradouro"]
        numero = vendedor["numero"]
        bairro = vendedor["bairro"]
        cep = vendedor["cep"]
        telefone = vendedor["telefone"]
        perc_comissao = vendedor["perc_comissao"]
        idcidade = vendedor["idcidade"]

        #insere no BD
        cursor.execute("""
                        UPDATE vendedor
                       SET nome = %s, cpf = %s, 
                       logradouro = %s, numero = %s,
                       bairro = %s, cep = %s,
                       telefone = %s, perc_comissao = %s,
                       idcidade = %s
                       WHERE idvendedor = %s
                       """, 
                       (nome, cpf, logradouro, numero, bairro, cep, telefone, perc_comissao, idcidade, id)
                       )
        conn.commit()
        conn.close()

        return jsonify({"message" : "alterado!!"})
    except Exception as e:
        print(e)
        return e
    


@vendedor_bp.route("/vendedor/<id>", methods=["DELETE"])
def excluir_vendedor(id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        #insere no BD
        cursor.execute("""
                        DELETE FROM vendedor
                       WHERE idvendedor = %s
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
from vendedor import vendedor_bp
import os

app = Flask(__name__,   
static_url_path='', 
            static_folder='static')
app.register_blueprint(usuario_bp)
app.register_blueprint(vendedor_bp)


@app.route("/")
def home():
    return send_from_directory(os.path.join(app.root_path,'static'), 'index.html')

if __name__ == "__main__":
    app.run()       

