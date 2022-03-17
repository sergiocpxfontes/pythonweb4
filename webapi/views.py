"""
Routes and views for the flask application.
"""

from datetime import datetime
from urllib.request import Request
from xmlrpc.client import ResponseError
from flask import Response, render_template,redirect,request,url_for,json
from webapi import app, utils
from webapi.tarefascls import Tarefa,TarefaOps
from webapi.azureutilscls import AzureUtils
from webapi.utils import DictObj

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route("/tarefas")
def tarefas():
    return utils.Utils.ListToJson(TarefaOps.GetAll())

@app.route("/tarefas/<int:id>")
def tarefa(id):
    obj = TarefaOps.Get(id)
    return utils.Utils.ObjectToJson(obj)

@app.route("/inserirtarefa",methods=["POST"])
def inserirtarefa():
    
    the_response = Response()
    the_response.code = "error"
    the_response.error_type = "error"
    the_response.status_code = 400
   
    if request.method == "POST":
        result = request.json

        print("JSON",result)
        result = json.loads(result)
        
        the_response.code = "success"
        the_response.error_type = "success"
        the_response.status_code = 200
        the_response._content = result

        t = Tarefa()

        my_obj = dict(result)
        print(type(my_obj))

        t.Id = my_obj["Id"]
        t.Descricao = my_obj["Descricao"]
        t.Estado = my_obj["Estado"]
        t.Url = my_obj["Url"]
        TarefaOps.Inserir(t)

    the_response._content = result
    return the_response 