import unittest
from webapi.tarefascls import Tarefa
from webapi import views as webapiviews

import xmlrunner

class TestWebApp(unittest.TestCase):
    def test_tarefas_getall(self):
        resultado = Tarefa.GetAll()
        self.assertNotEqual(resultado,0)
    
    def test_api_tarefas_getall(self):
        resultado = webapiviews.tarefas()

        esperado = '[{"Id": 1, "Descricao": "enviar email", "Estado": 0, "Url": "www.rumos.pt"}, {"Id": 2, "Descricao": "telefonar", "Estado": 0, "Url": "www.rumos.pt"}]'

        self.assertNotEqualEqual(resultado,esperado)
if __name__ =="__main__":
    unittest.main()
    #unittest.main(testRunner = xmlrunner.XMLTestRunner(output='relatorio-testes'))