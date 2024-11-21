from flask import Blueprint, Flask, app, jsonify, render_template, request, redirect, url_for
import mysql.connector
import utils
hospedagens_bp = Blueprint('hospedagens_bp',__name__)

@hospedagens_bp.route('/register_hotel_costumer', methods=['POST'])
def register_hotel_costumer():
     # Capture form data with proper validation
    name = request.form['name']  # ... validate and handle errors
    cpf = request.form['cpf']  # ... validate and handle errors
    room = request.form['room']  # ... validate and handle errors
    check_in = request.form['check_in']  # ... validate and handle errors
    check_out = request.form['check_out']  # ... validate and handle errors

    try:
        # Connect to the database using a context manager (recommended)

        con = utils.connect_to_database()  # Assuming you have a function to get a valid connection
        if not con:
            return jsonify({'error': 'Failed to connect to database'}), 500
        with con as mydb:
            mycursor = mydb.cursor()

            # Print the constructed SQL query for debugging
            sql = "INSERT INTO hospedagens (nome, cpf, quarto, check_in, check_out) VALUES (%s, %s, %s, %s, %s)"
            print(f"SQL Query: {sql}")

            mycursor.execute(sql, (name, cpf, room, check_in, check_out))
            mydb.commit()

        return redirect(url_for('sucesso'))

    except mysql.connector.Error as error:
        print(f"Failed to insert record: {error}")
        return "Ocorreu um erro ao inserir os dados.", 500