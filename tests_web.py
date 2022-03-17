import unittest
from webapp.tarefascls import Tarefa
from webapp import views as webappviews
import webapp
import xmlrunner

class TestWebApp(unittest.TestCase):

    def setUp(self):
        self.app = webapp.app.test_client()

    def test_greeting(self):
        rv = self.app.get('/home')
        self.assertIn('Sergio', str(rv.data))
        #self.assertIn('My Flask Application', str(rv.data))

if __name__ =="__main__":
    unittest.main()
    #unittest.main(testRunner = xmlrunner.XMLTestRunner(output='relatorio-testes'))