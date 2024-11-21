from flask import Flask, jsonify, render_template, request, redirect, url_for
import mysql.connector
import utils

from usuarios import usuarios_bp
from hospedagens import hospedagens_bp
app = Flask(__name__)


app.register_blueprint(usuarios_bp)
app.register_blueprint(hospedagens_bp)

@app.route('/', methods=['GET'])
def inicial():
    return render_template('/cadastro_hotel.html')




# Rota para página de sucesso
@app.route('/sucesso')
def sucesso():
    return 'Dados inseridos com sucesso!'



if __name__ == '__main__':
    app.run(debug=True)
