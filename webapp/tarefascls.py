from webapp.utils import Utils
import json
class Tarefa:
    def __init__(self,id=0,descricao="",estado=0,url=""):
        self.Id=id
        self.Descricao = descricao
        self.Estado = estado
        self.Url = url

    def Imprimir(self):
        print(self.Id, self.Descricao,self.Estado)
 