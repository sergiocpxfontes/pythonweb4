import pyodbc
import pymysql
import json

class DictObj:
    def __init__(self, in_dict:dict):
        assert isinstance(in_dict, dict)
        for key, val in in_dict.items():
            if isinstance(val, (list, tuple)):
                setattr(self, key, [DictObj(x) if isinstance(x, dict) else x for x in val])
            else:
                setattr(self, key, DictObj(val) if isinstance(val, dict) else val)

class Utils:

    @staticmethod
    def ListToJson(list):
        return json.dumps([ob.__dict__ for ob in list])

    @staticmethod
    def ObjectToJson(obj):
        return json.dumps(obj.__dict__)

    @staticmethod
    def ExecutaComandoSQL(sql):
        resultado=0
        cs="""DRIVER={MySQL ODBC 5.1 Driver};
        USER=root;PASSWORD=admins;
        SERVER=mysqldb;
        DATABASE=tarefasdb;
        PORT=3306"""
        try:
            conn= pyodbc.connect(cs)
            cursor = conn.cursor()
            cursor.execute(sql)
            resultado=cursor.rowcount
            conn.commit()
            print("resultado=",resultado)
        except  pyodbc.Error as erro:
            print(erro)
        finally:
            pass
            #cursor.close()
            #conn.close()
        return resultado
    @staticmethod
    def ExecutaConsultaSQL(sql):
        resultado=[]
        cs="""DRIVER={MySQL ODBC 5.1 Driver};
        USER=root;PASSWORD=admins;
        SERVER=mysqldb;
        DATABASE=tarefasdb;
        PORT=3306"""
        try:
            conn= pyodbc.connect(cs)
            cursor = conn.cursor()
            registos = cursor.execute(sql)
            resultado = registos.fetchall()
            
            conn.commit()
            print("resultado=",resultado)
        except  pyodbc.Error as erro:
            print(erro)
        finally:
            pass
            #cursor.close()
            #conn.close()
        return resultado
    @staticmethod
    def ExecutaComandoMySQL(sql):
        resultado=0
        # Connect to the database
        connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='admins',
                             database='tarefasdb',
                             cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute(sql)
                    connection.commit()
        except  pyodbc.Error as erro:
            print(erro)
        finally:
            pass
        return resultado
    @staticmethod
    def ExecutaConsultaMySQL(sql):
        resultado=[]
        
        try:
            # Connect to the database
            connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='admins',
                             database='tarefasdb',
                             cursorclass=pymysql.cursors.DictCursor)
            with connection:
                with connection.cursor() as cursor:
                    # Read a single record
                    cursor.execute(sql)
                    #result = cursor.fetchall()
                    resultado = cursor.fetchall()
                    print(resultado)
        except  pyodbc.Error as erro:
            print(erro)
        finally:
            pass
        return resultado    