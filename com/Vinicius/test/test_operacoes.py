from unittest import TestCase
from com.Vinicius.operacoes import Operacoes

class TestOperacoes(TestCase):

	def setUp (self):
		self.operacoes = Operacoes()
		
	def test_multiplica(self):
		self.assertEqual(self.operacoes.multiplica(2,5),10)