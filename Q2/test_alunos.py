import unittest
from alunos import alunos_acima_media

class TestRenda(unittest.TestCase):
    def test_alunos_acima_media(self):
        situacao1 = [('Aluno 1', 8), ('Aluno 2', 6), ('Aluno 3', 9), ('Aluno 4', 7)]
        r_esperado1 = [('Aluno 1', 8), ('Aluno 3', 9)]
        situacao2 = [('Aluno 1', 7), ('Aluno 2', 7.5), ('Aluno 3', 6), ('Aluno 4', 8.5)]
        r_esperado2 = [('Aluno 2', 7.5), ('Aluno 4', 8.5)]
        situacao3 = [('Aluno 1', 6), ('Aluno 2', 6), ('Aluno 3', 6), ('Aluno 4', 6)]
        r_esperado3 = []

        self.assertEqual(alunos_acima_media(situacao1), r_esperado1)
        self.assertEqual(alunos_acima_media(situacao2), r_esperado2)
        self.assertEqual(alunos_acima_media(situacao3), r_esperado3)

unittest.main()
