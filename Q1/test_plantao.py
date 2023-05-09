import unittest

from plantao import max_horas

class TestMaxHoras(unittest.TestCase):
    
    def test_max_horas_lista_vazia(self):
        # Teste para verificar se a função retorna uma lista vazia quando a entrada é uma lista vazia.
        self.assertEqual(max_horas([]), [])
    
    def test_max_horas_um_elemento(self):
        # Teste para verificar se a função retorna o único elemento quando a entrada é uma lista com um único elemento.
        self.assertEqual(max_horas([(1, 10)]), [(1, 10)])
    
    def test_max_horas_varios_elementos(self):
        # Teste para verificar se a função retorna os elementos corretos quando a entrada é uma lista com vários elementos.
        self.assertEqual(max_horas([(1, 10), (2, 5), (3, 10), (4, 8)]), [(1, 10), (3, 10)])
    
    def test_max_horas_multiplos_maximos(self):
        # Teste para verificar se a função retorna todos os elementos com o horário máximo quando há múltiplos elementos com o horário máximo.
        self.assertEqual(max_horas([(1, 10), (2, 5), (3, 10), (4, 8), (5, 10)]), [(1, 10), (3, 10), (5, 10)])
        
if __name__ == '__main__':
    unittest.main()
