from main import app
from flask import Flask, request, jsonify
from data import cursor, cnx
from datetime import date
import json

@app.route("/divida/cadastrar")
def CadastrarDivida():

    # if True:
    #     return "teste"

    data = request.json

    produto = data['Produto']
    dataVencimento = data['DataVencimento']
    idExterno = data['IdExterno']
    valor = data['Valor']
    devedorId = data['DevedorId']

    if VerificaUsuario(devedorId) == False:
        return "Usuario não existe"

    if VerificaIdExterno(idExterno):
        return "Id externo já existe."

    # if True:
    #     return str(type(valor))


    sql = "INSERT INTO Divida (Produto, DataVencimento, IdExterno, Valor, DevedorId, DataCriacao) VALUES (%s, %s, %s, %s, %s, %s);"
    val = (produto, dataVencimento, idExterno, valor, devedorId, date.today())

    # if True:
    #     return str(val)

    cursor.execute(sql, val)

    cnx.commit()

    return "Cadastrado"

@app.route("/divida/listar")
def ListarDivida():

    cursor.execute("SELECT * FROM Divida")
    myresult = cursor.fetchall()

    for x in myresult:
        print(x)

    # re = json.dumps(myresult)
    return jsonify(myresult)

@app.route("/divida/editar")
def EditarDivida():

    data = request.json

    dividaId = data['DividaId']
    produto = data['Produto']
    dataVencimento = data['DataVencimento']
    valor = data['Valor']

    sql = '''UPDATE Divida 
    SET Produto = %s, DataVencimento = %s, Valor = %s, DataAtualizacao = %s
    WHERE DividaId = %s
    '''
    val = (produto, dataVencimento, valor, date.today(), dividaId )

    cursor.execute(sql, val)

    cnx.commit()

    return "Editado"

def VerificaUsuario(id):

    cursor.execute("SELECT * FROM Usuario WHERE UsuarioId = " + str(id))
    myresult = cursor.fetchall()

    return len(myresult) > 0

def VerificaIdExterno(id):
    
    cursor.execute("SELECT * FROM Divida WHERE IdExterno = " + str(id))
    myresult = cursor.fetchall()

    return len(myresult) > 0
