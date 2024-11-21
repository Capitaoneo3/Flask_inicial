from flask import Blueprint, Flask, jsonify, render_template, request, redirect, url_for
import mysql.connector
import utils
from werkzeug.security import generate_password_hash, check_password_hash

login_bp = Blueprint('login_bp',__name__)


@login_bp.route('/login', methods=['POST'])    
def login():
    try:
        nome = request.form['nome']
        senha_a_vericar = request.form['senha']
        
        # Connect to the database using a context manager (recommended)
        con = utils.connect_to_database()  # Assuming you have a function to get a valid connection
        if not con:
            return jsonify({'error': 'Failed to connect to database'}), 500
        with con as mydb:
               cursor = mydb.cursor()
        # Buscar usuário pelo nome
        cursor.execute('SELECT * FROM usuarios WHERE nome = %s', (nome,))
        usuario = cursor.fetchone()
        id_usuario = usuario[0]
        cursor.execute('SELECT senha FROM senhas WHERE id_usuario = %s', (id_usuario,))
        senha_no_banco = cursor.fetchone()
        
        if not usuario or not check_password_hash(senha_no_banco, senha_a_vericar):
            return jsonify({"message": "Nome de usuário ou senha inválidos"}), 401

        return jsonify({"message": "Login bem-sucedido"}), 200

    except mysql.connector.Error as e:
        return jsonify({"message": "Erro ao executar consulta no banco de dados", "error": str(e)}), 500

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            mydb.close()


    