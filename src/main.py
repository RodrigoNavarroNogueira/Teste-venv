import pandas as pd  
from flask import Flask, jsonify, request

app = Flask(__name__)   


@app.route('/', methods=["GET"])
def homepage():    
    return 'Olá Mundo'


@app.route('/cadastro/usuario', methods=["POST"])
def cadastra_usuario():
    body = request.get_json()
    print(body)
    return body


@app.route('/pegarvendas', methods=["GET"])
def pegar_vendas():
    table = pd.read_csv('Criando-API-no-Python.csv')  
    total_vendas = table['Vendas'].sum()  
    resposta = {'total de vendas': total_vendas}  
    return jsonify(resposta) 


@app.route('/pegarvendasum')
def pegar_tv():
    table = pd.read_csv('Criando-API-no-Python.csv')
    total_tv = table['TV'].sum()
    resposta = {'total de vendas da tv': total_tv}
    return jsonify(resposta)





app.run() 