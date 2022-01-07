from main import app
from flask import Flask, request, jsonify
from data import cursor, cnx
from datetime import date
import json

# @app.route("/")
# def home():
#     return "home"

@app.route("/teste")
def teste():
    # teste = json.dumps(myresult)

    #return json.dumps(myresult)

    return str(date.today())

@app.route("/cadastrar")
def Cadastrar():

    # teste = request.args.get('teste')

    # teste = request.args.get['teste']

    data = request.json

    cpf = data['Cpf']
    nome = data['Nome']
    dataNascimento = data['DataNascimento']

    if VerificaCpfExistente(cpf):
        return "Cpf já cadastrado."

    sql = "INSERT INTO Usuario (Cpf, Nome, DataNascimento, DataCriacao) VALUES (%s, %s, %s, %s);"
    val = (cpf, nome, dataNascimento, date.today())

    cursor.execute(sql, val)

    cnx.commit()

    return "Cadastrado"

    # if True:
    #     return data['teste']

    # return jsonify(data)

@app.route("/editar")
def Editar():

    data = request.json

    usuarioId = data['UsuarioId']
    cpf = data['Cpf']
    nome = data['Nome']
    dataNascimento = data['DataNascimento']


    if VerificaCpfExistente(cpf):
        return "Cpf já cadastrado."

    sql = '''UPDATE Usuario 
    SET Cpf = %s, Nome = %s, DataNascimento = %s, DataAtualizacao = %s
    WHERE UsuarioId = %s
    '''
    val = (cpf, nome, dataNascimento, date.today(), usuarioId )

    cursor.execute(sql, val)

    cnx.commit()

    return "Editado"

@app.route("/listar")
def Listar():

    cursor.execute("SELECT * FROM Usuario")
    myresult = cursor.fetchall()

    for x in myresult:
        print(x)

    # re = json.dumps(myresult)
    return jsonify(myresult)

@app.route("/excluir")
def Excluir():

    data = request.json

    usuarioId = data['UsuarioId']

    sql = "DELETE FROM Usuario WHERE UsuarioId = " + str(usuarioId)
    #val = (usuarioId)

    cursor.execute(sql)

    cnx.commit()

    return "Excluido"

def VerificaCpfExistente(cpf):

    cursor.execute("SELECT * FROM Usuario WHERE Cpf = " + str(cpf))
    myresult = cursor.fetchall()

    return len(myresult) > 0