import unittest
from app import app, calcular_cedulas

class TestSaqueAPI(unittest.TestCase):
    
    def setUp(self):
        """
        Configura o cliente de teste do Flask.
        """
        self.app = app.test_client()
        self.app.testing = True
    
    def test_calculo_cedulas(self):
        """
        Testa a função calcular_cedulas para valores específicos.
        """
        self.assertEqual(calcular_cedulas(380), {'100': 3, '50': 1, '20': 1, '10': 1, '5': 0, '2': 0})
        self.assertEqual(calcular_cedulas(0), {'100': 0, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0})
        with self.assertRaises(ValueError):
            calcular_cedulas(123)
    
    def test_saque_endpoint(self):
        """
        Testa o endpoint /api/saque com um valor válido.
        """
        response = self.app.post('/api/saque', json={'valor': 380})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'100': 3, '50': 1, '20': 1, '10': 1, '5': 0, '2': 0})
    
    def test_saque_valor_invalido(self):
        """
        Testa o endpoint /api/saque com valores inválidos.
        """
        response = self.app.post('/api/saque', json={'valor': -50})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'erro': 'Valor de saque inválido. Deve ser um inteiro positivo.'})
        
        response = self.app.post('/api/saque', json={'valor': 'abc'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'erro': 'Valor de saque inválido. Deve ser um inteiro positivo.'})
    
    def test_saque_valor_nao_atendido(self):
        """
        Testa o endpoint /api/saque com um valor que não pode ser atendido.
        """
        response = self.app.post('/api/saque', json={'valor': 123})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'erro': 'Não é possível sacar o valor desejado com as cédulas disponíveis.'})
    
    def test_saque_valor_zero(self):
        """
        Testa o endpoint /api/saque com o valor zero.
        """
        response = self.app.post('/api/saque', json={'valor': 0})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'100': 0, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0})

if __name__ == '__main__':
    unittest.main()
