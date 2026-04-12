from dp import knapsack_dp
from greedy import knapsack_greedy


def imprimir_resultado(nombre, valor, seleccion, costos, retornos):
	costo_total = sum(costos[i] for i in seleccion)
	retorno_total = sum(retornos[i] for i in seleccion)

	print(f"{nombre}")
	print(f"  Valor reportado: {valor}")
	print(f"  Proyectos elegidos (indices): {seleccion}")
	print(f"  Costo total: {costo_total}")
	print(f"  Retorno total: {retorno_total}")


def ejecutar_caso(costos, retornos, B, titulo):
	print("=" * 70)
	print(titulo)
	print(f"Costos   : {costos}")
	print(f"Retornos : {retornos}")
	print(f"Presupuesto B: {B}\n")

	valor_dp, seleccion_dp, _ = knapsack_dp(costos, retornos, B)
	valor_voraz, seleccion_voraz = knapsack_greedy(costos, retornos, B)

	imprimir_resultado("Programacion Dinamica", valor_dp, seleccion_dp, costos, retornos)
	print()
	imprimir_resultado("Enfoque Voraz (ratio retorno/costo)", valor_voraz, seleccion_voraz, costos, retornos)
	print(f"\nDiferencia DP - Voraz: {valor_dp - valor_voraz}")
	print()


if __name__ == "__main__":
	# Caso simple.
	ejecutar_caso(
		costos=[2, 3, 4],
		retornos=[3, 4, 5],
		B=5,
		titulo="Caso 1: Basico",
	)

	# Caso mas grande para mostrar robustez de DP.
	ejecutar_caso(
		costos=[10, 20, 30],
		retornos=[60, 100, 120],
		B=50,
		titulo="Caso 2: Presupuesto medio",
	)

	# Caso clasico donde voraz falla frente a DP (0/1 knapsack).
	ejecutar_caso(
		costos=[20, 10, 30],
		retornos=[100, 60, 120],
		B=50,
		titulo="Caso 3: Contraejemplo de optimalidad voraz",
	)
