from flask import Flask, request, jsonify
from data import cursor, cnx
from datetime import date
import json

app = Flask(__name__)

import divida
import usuario
import autenticacao

@app.route("/c")
def home():
    return "home"


app.run(debug=True)
