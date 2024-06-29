import unittest
from app import app, calcular_cedulas

class TestSaqueAPI(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_calculo_cedulas(self):
        self.assertEqual(calcular_cedulas(380), {'100': 3, '50': 1, '20': 1, '10': 1, '5': 0, '2': 0})
        self.assertEqual(calcular_cedulas(0), {'100': 0, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0})
    
    def test_saque_endpoint(self):
        response = self.app.post('/api/saque', json={'valor': 380})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'100': 3, '50': 1, '20': 1, '10': 1, '5': 0, '2': 0})
    
    def test_saque_valor_invalido(self):
        response = self.app.post('/api/saque', json={'valor': -50})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'erro': 'Valor de saque inválido. Deve ser um inteiro positivo.'})
        
        response = self.app.post('/api/saque', json={'valor': 'abc'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'erro': 'Valor de saque inválido. Deve ser um inteiro positivo.'})

if __name__ == '__main__':
    unittest.main()
