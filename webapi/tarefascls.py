from webapi.utils import Utils
import json
class Tarefa:
    def __init__(self,id=0,descricao="",estado=0,url=""):
        self.Id=id
        self.Descricao = descricao
        self.Estado = estado
        self.Url = url

    def Imprimir(self):
        print(self.Id, self.Descricao,self.Estado)

class TarefaOps:
    @staticmethod
    def Inserir(obj):
        sql="INSERT INTO Tarefa (TarefaId,Descricao,Estado,Url) VALUES ({0},'{1}',{2},'{3}')"
        sql = sql.format(obj.Id,obj.Descricao,obj.Estado, obj.Url)
       
        #return Utils.ExecutaComandoSQL(sql)
        return Utils.ExecutaComandoMySQL(sql)
    @staticmethod
    def Update(obj):
        sql="UPDATE Tarefa set Descricao='{1}',Estado={2},Url='{3}' WHERE TarefaId={0}"
        sql = sql.format(obj.Id,obj.Descricao,obj.Estado,obj.Url)
        #return Utils.ExecutaComandoSQL(sql)
        return Utils.ExecutaComandoMySQL(sql)
    @staticmethod
    def Delete(id):
        sql="DELETE FROM Tarefa WHERE TarefaId={0}"
        sql = sql.format(id)
      
        #return Utils.ExecutaComandoSQL(sql)
        return Utils.ExecutaComandoMySQL(sql)
    @staticmethod
    def GetAll():
        lst = []
        sql="SELECT * FROM Tarefa"
        
        for obj in Utils.ExecutaConsultaMySQL(sql):
            tarefa = Tarefa(obj["TarefaId"],obj["Descricao"],obj["Estado"],obj["Url"])
            lst.append(tarefa)
        
        return lst
    @staticmethod
    def Get(id):
        
        result = Tarefa()    

        sql="SELECT * FROM Tarefa WHERE TarefaId={0}"
        sql = sql.format(id)
        
        try:
            for obj in Utils.ExecutaConsultaMySQL(sql):
                result.Id = obj["TarefaId"]
                result.Descricao= obj["Descricao"]
                result.Estado = obj["Estado"]
                result.Url = obj["Url"]
        except:
            print("not found")
 
        return result