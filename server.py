from flask import Flask, send_from_directory
from cidade import cidade_bp
from vendedor import vendedor_bp
from usuario import usuario_bp
from marca import marca_bp
from produto import produto_bp
from compra import compra_bp
from contasareceber import conta_receber_bp
from contasapagar import contaspagar_bp
import os

app = Flask(__name__,   
static_url_path='', 
            static_folder='static')
app.register_blueprint(cidade_bp)
app.register_blueprint(vendedor_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(marca_bp)
app.register_blueprint(produto_bp)
app.register_blueprint(compra_bp)
app.register_blueprint(conta_receber_bp)
app.register_blueprint(contaspagar_bp)


@app.route("/")
def home():
    return send_from_directory(os.path.join(app.root_path,'static'), 'index.html')

if __name__ == "__main__":
    app.run()       
