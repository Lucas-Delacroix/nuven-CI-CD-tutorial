from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return "Bem vindo a pagina inicial. Verificando mudancas."


@app.route("/admin")
def admin():
    return "Bem-Vindo ao Admin!!! :)"


@app.route("/soma/<int:n1>/<int:n2>")
def soma(n1,n2):
    soma = n1 + n2
    return f"O valor da soma de {n1} + {n2} = {soma}"


@app.route("/numero/<string:nome>/<int:numero>")
def numero(nome, numero):
    return f"Ola {nome}, seu numero passado na URL foi: {numero}"


#Métodos HTTP
@app.route("/perfil/<nome>", methods=["GET"])
def perfil(nome):
    return f"Esse e o perfil de: {nome}"

@app.route("/perfil/email", methods=["POST"])
def perfil_email():
    data = request.get_json()
    email = data["email"]
    senha = data["senha"]
    return f"<h1>Email: {email} Senha: {senha}</h1>"


@app.route("/ver-cep/<cep>", methods=["GET"])
def ver_cep(cep):
    ifce_maracanau = '61939-140'
    ifce_fortaleza = '60040-531'
    ifce_maranguape = '61940-750'

    if cep == 'maranguape':
        endereço = requests.get(f"http://viacep.com.br/ws/{ifce_maranguape}/json")
    elif cep == 'maracanau':
        endereço = requests.get(f"http://viacep.com.br/ws/{ifce_maracanau}/json")
    else:
        endereço = requests.get(f"http://viacep.com.br/ws/{ifce_fortaleza}/json")
    
    return endereço.content



@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data["email"]
    senha = data["senha"]
    if senha == '123456':
        return 'Acesso autorizado'
    else:
        return 'Acesso nao autorizado!!!'        







if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)