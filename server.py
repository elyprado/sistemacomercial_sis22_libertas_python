from flask import Flask, send_from_directory
from usuario import usuario_bp
from cliente import cliente_bp
import os

app = Flask(__name__,   
static_url_path='', 
            static_folder='static')
app.register_blueprint(usuario_bp)
app.register_blueprint(cliente_bp)

@app.route("/")
def home():
    return send_from_directory(os.path.join(app.root_path,'static'), 'index.html')

if __name__ == "__main__":
    app.run()       