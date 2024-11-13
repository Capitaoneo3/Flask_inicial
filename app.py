from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configurações do banco de dados
db_host = 'localhost'
db_user = 'root'
db_password = ''
db_name = 'formulario_db'

@app.route('/usuario', methods=['POST'])
def submit_formulario():
    # Capture form data with proper validation
    nome = request.form['nome']  # ... validate and handle errors
    email = request.form['email']  # ... validate and handle errors
    idade = request.form['idade']  # ... validate and handle errors
    genero = request.form['genero']  # ... validate and handle errors
    mensagem = request.form['mensagem']  # ... validate and handle errors

    # Print variable values for inspection
    print(f"nome: {nome}, email: {email}, idade: {idade}, genero: {genero}, mensagem: {mensagem}")

    # Ensure data integrity before database interaction

    try:
        # Connect to the database using a context manager (recommended)
        with mysql.connector.connect(
            host=db_host, user=db_user, password=db_password, database=db_name,charset='utf8' 
        ) as mydb:
            mycursor = mydb.cursor()

            # Print the constructed SQL query for debugging
            sql = "INSERT INTO usuarios (nome, email, idade, genero, mensagem) VALUES (%s, %s, %s, %s, %s)"
            print(f"SQL Query: {sql}")

            mycursor.execute(sql, (nome, email, idade, genero, mensagem))
            mydb.commit()

        return redirect(url_for('sucesso'))

    except mysql.connector.Error as error:
        print(f"Failed to insert record: {error}")
        return "Ocorreu um erro ao inserir os dados.", 500


@app.route('/usuario', methods=['PUT'])
def submit_formulario():
    # Capture form data with proper validation
    id = request.form['id']
    nome = request.form['nome']  # ... validate and handle errors
    email = request.form['email']  # ... validate and handle errors
    idade = request.form['idade']  # ... validate and handle errors
    genero = request.form['genero']  # ... validate and handle errors
    mensagem = request.form['mensagem']  # ... validate and handle errors

    # Ensure data integrity before database interaction

    try:
        # Connect to the database using a context manager (recommended)
        with mysql.connector.connect(
            host=db_host, user=db_user, password=db_password, database=db_name,charset='utf8' 
        ) as mydb:
            mycursor = mydb.cursor()

            # Print the constructed SQL query for debugging
            sql = """
            UPDATE usuarios
            SET
                nome = CASE WHEN %s IS NOT NULL THEN %s ELSE nome END,
                email = CASE WHEN %s IS NOT NULL THEN %s ELSE email END,
                idade = CASE WHEN %s IS NOT NULL THEN %s ELSE idade END,
                genero = CASE WHEN %s IS NOT NULL THEN %s ELSE genero END,
                mensagem = CASE WHEN %s IS NOT NULL THEN %s ELSE mensagem END
            WHERE id = %s
            """
            params = (nome, nome, email, email, idade, idade, genero, genero, mensagem, id)
            mycursor.execute(sql, params)
            mydb.commit()

        return redirect(url_for('sucesso'))

    except mysql.connector.Error as error:
        print(f"Failed to insert record: {error}")
        return "Ocorreu um erro ao inserir os dados.", 500


# Rota para página de sucesso
@app.route('/sucesso')
def sucesso():
    return 'Dados inseridos com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
