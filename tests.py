# test_app.py
import pytest
from flask import Flask
from app import app 

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Bem vindo a pagina inicial. Verificando mudancas." in response.data

def test_admin(client):
    response = client.get('/admin')
    assert response.status_code == 200
    assert b"Bem-Vindo ao Admin!!! :)" in response.data

def test_soma(client):
    response = client.get('/soma/2/3')
    assert response.status_code == 200
    assert b"O valor da soma de 2 + 3 = 5" in response.data

def test_numero(client):
    response = client.get('/numero/Joao/123')
    assert response.status_code == 200
    assert b"Ola Joao, seu numero passado na URL foi: 123" in response.data

def test_perfil(client):
    response = client.get('/perfil/Joao')
    assert response.status_code == 200
    assert b"Esse e o perfil de: Joao" in response.data

def test_perfil_email(client):
    response = client.post('/perfil/email', json={"email": "test@example.com", "senha": "123456"})
    assert response.status_code == 200
    assert b"Email: test@example.com Senha: 123455" in response.data

def test_ver_cep(client):
    response = client.get('/ver-cep/maranguape')
    assert response.status_code == 200
    

def test_login(client):
    response = client.post('/login', json={"email": "test@example.com", "senha": "123456"})
    assert response.status_code == 200
    
