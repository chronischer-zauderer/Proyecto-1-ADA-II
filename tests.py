import unittest

from dp import knapsack_dp


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


if __name__ == "__main__":
	unittest.main()
