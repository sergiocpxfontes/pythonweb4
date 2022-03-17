import pyodbc
import pymysql
import json
class Utils:
    @staticmethod
    def ListToJson(list):
        return json.dumps([ob.__dict__ for ob in list])

    @staticmethod
    def ObjectToJson(obj):
        return json.dumps(obj.__dict__)  

    @staticmethod
    def ListFromJson(value):
        #return list(json.loads('[{"Id": 1, "Descricao": "enviar email", "Estado": 0, "Url": "www.rumos.pt"}, {"Id": 2, "Descricao": "telefonar", "Estado": 0, "Url": "www.rumos.pt"}]'))
        return list(value)

    @staticmethod
    def ObjectFromJson(value):
        return json.load(value) 