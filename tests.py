import unittest

from dp import knapsack_dp
from greedy import knapsack_greedy


class TestProyectoADA(unittest.TestCase):
	def test_dp_basico(self):
		costos = [2, 3, 4]
		retornos = [3, 4, 5]
		B = 5

		valor, seleccion, _ = knapsack_dp(costos, retornos, B)

		self.assertEqual(valor, 7)
		self.assertEqual(seleccion, [0, 1])

	def test_dp_caso_presupuesto_medio(self):
		costos = [10, 20, 30]
		retornos = [60, 100, 120]
		B = 50

		valor_dp, seleccion_dp, _ = knapsack_dp(costos, retornos, B)

		self.assertEqual(valor_dp, 220)
		self.assertEqual(seleccion_dp, [1, 2])

	def test_errores_entrada(self):
		with self.assertRaises(ValueError):
			knapsack_dp([1, 2], [10], 5)

		with self.assertRaises(ValueError):
			knapsack_dp([1], [10], -1)

	def test_voraz_basico(self):
		costos = [2, 3, 4]
		retornos = [3, 4, 5]
		B = 5

		valor_voraz, seleccion_voraz = knapsack_greedy(costos, retornos, B)

		self.assertEqual(valor_voraz, 7)
		self.assertEqual(seleccion_voraz, [0, 1])

	def test_voraz_no_garantiza_optimo(self):
		costos = [20, 10, 30]
		retornos = [100, 60, 120]
		B = 50

		valor_voraz, seleccion_voraz = knapsack_greedy(costos, retornos, B)
		valor_dp, seleccion_dp, _ = knapsack_dp(costos, retornos, B)

		self.assertEqual(valor_voraz, 160)
		self.assertEqual(seleccion_voraz, [0, 1])
		self.assertEqual(valor_dp, 220)
		self.assertEqual(seleccion_dp, [0, 2])


if __name__ == "__main__":
	unittest.main()
