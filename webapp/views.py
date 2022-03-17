"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,redirect,request,url_for
from webapp import app, utils
from webapp.tarefascls import Tarefa
from webapp.azureutilscls import AzureUtils
import requests

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/teste')
def teste1():
    """Renders the about page."""
    return render_template(
        'teste.html',
        titulo='Pagina de teste',
        ano=datetime.now().year,
        mensagem='um exemplo muito simples.'
    )

@app.route("/tarefas")
def listatarefas():
    x = requests.get('http://192.168.1.94:8092/tarefas')
    jsonResponse = x.json()
    print("=",jsonResponse)

    lista = utils.Utils.ListFromJson(jsonResponse)
    print(type(lista))
    print("=",lista)

    return render_template(
        "tarefas.html",
        titulo = "Tarefas",
        tarefas = lista
        )

@app.route("/inserir")
def inserir():
    return render_template(
        "inserir.html",
        titulo = "Nova Tarefa"
        )


@app.route("/inserirtarefa",methods=["POST"])
def inserirtarefa():

    if request.method == "POST":
        result = request.form

        codigo= result["txtcodigo"]
        descricao= result["txtdescricao"]
        estado= result["txtestado"]
        
        t = Tarefa(codigo,descricao,estado)

        r = requests.post('http://192.168.1.94:8092/inserirtarefa', json=utils.Utils.ObjectToJson(t))

    return redirect(url_for('listatarefas'))


@app.route("/eliminar/<id>")
def eliminar(id):

    Tarefa.Delete(id)
    return redirect(url_for('listatarefas'))


@app.route("/detalhe/<id>")
def detalhe(id):

    t = Tarefa()
    t.Get(id)
    return render_template(
        "detalhe.html",
        titulo = "Tarefa",
        tarefa = t
        )


@app.route("/editar/<id>")
def editar(id):

    t = Tarefa()
    t.Get(id)
    return render_template(
        "editar.html",
        titulo = "Tarefa",
        tarefa = t
        )


@app.route("/atualizartarefa",methods=["POST"])
def atualizartarefa():

    if request.method == "POST":
        result = request.form

        codigo= result["txtcodigo"]
        descricao= result["txtdescricao"]
        estado= result["txtestado"]
        
        t = Tarefa(codigo,descricao,estado)
        t.Update()
    return redirect(url_for('listatarefas'))

@app.route("/upload/<id>",methods=["POST"])
def upload(id):
    if request.method =="POST":
        result =request.files['file']
        result.save("C:/Temp/python/" + result.filename );

        t = Tarefa()
        t.Get(id)
        with open("C:/Temp/python/" + result.filename ,"rb") as data:
            AzureUtils.BlobUpload(result.filename,data,id)
            t.Url = "https://ac2020storage.blob.core.windows.net/python-sergio/" + result.filename
            t.Update()
    return redirect(url_for('listatarefas'))