from main import app
from flask import Flask, request, jsonify
from data import cursor, cnx
from datetime import date
import json
import jwt

# @app.route("/")
# def home():
#     return "home"

@app.route("/autenticacao")
def Autenticar():

    data = request.json

    cpf = data['Cpf']
    dataNascimento = data['DataNascimento']

    sql = '''SELECT * FROM Usuario 
    WHERE Cpf = %s and DataNascimento = %s
    '''
    val = (cpf, dataNascimento)

    cursor.execute(sql, val)

    myresult = cursor.fetchall()

    for x in myresult:
        print(x)

    if len(myresult) == 0:
        return "Usuario não encontrado"
    
    usuarioId = myresult[0][0]
    nome = myresult[0][2]

    payload_data = {
    "UsuarioId": usuarioId,
    "Nome": nome,
    }   
    my_secret = '53234356835838'

    token = jwt.encode(
    payload=payload_data,
    key=my_secret
    )

    return jsonify(token)