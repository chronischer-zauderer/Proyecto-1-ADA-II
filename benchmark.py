"""Benchmark de DP vs Voraz para asignacion de presupuesto (0/1 knapsack)."""

import random
import time
from statistics import mean

from dp import knapsack_dp
from greedy import knapsack_greedy


def generar_instancia(n, max_costo=50, max_retorno=120):
	"""Genera costos y retornos aleatorios para una instancia."""
	costos = [random.randint(1, max_costo) for _ in range(n)]
	retornos = [random.randint(1, max_retorno) for _ in range(n)]
	return costos, retornos


def medir_tiempo(func, costos, retornos, presupuesto, repeticiones=5):
	"""Mide el tiempo promedio de ejecucion en milisegundos."""
	tiempos = []
	for _ in range(repeticiones):
		inicio = time.perf_counter()
		func(costos, retornos, presupuesto)
		fin = time.perf_counter()
		tiempos.append((fin - inicio) * 1000.0)
	return mean(tiempos)


def ejecutar_benchmark(configuraciones, muestras=10, repeticiones=3, semilla=42):
	"""Ejecuta benchmark y retorna resultados agregados por configuracion."""
	random.seed(semilla)
	resultados = []

	for n, presupuesto in configuraciones:
		dp_ms = []
		voraz_ms = []
		brechas = []
		iguales = 0

		for _ in range(muestras):
			costos, retornos = generar_instancia(n)
			valor_dp, _, _ = knapsack_dp(costos, retornos, presupuesto)
			valor_voraz, _ = knapsack_greedy(costos, retornos, presupuesto)

			dp_ms.append(medir_tiempo(knapsack_dp, costos, retornos, presupuesto, repeticiones))
			voraz_ms.append(medir_tiempo(knapsack_greedy, costos, retornos, presupuesto, repeticiones))

			if valor_dp == valor_voraz:
				iguales += 1
			if valor_dp > 0:
				brecha = (valor_dp - valor_voraz) / valor_dp * 100.0
			else:
				brecha = 0.0
			brechas.append(brecha)

		resultados.append(
			{
				"n": n,
				"B": presupuesto,
				"dp_ms": mean(dp_ms),
				"voraz_ms": mean(voraz_ms),
				"brecha_pct": mean(brechas),
				"coincidencias": iguales,
				"muestras": muestras,
			}
		)

	return resultados


def imprimir_tabla_markdown(resultados):
	"""Imprime resultados en formato tabla Markdown."""
	print("| n | B | DP (ms) | Voraz (ms) | Brecha promedio (%) | Coincidencias exactas |")
	print("|---:|---:|---:|---:|---:|---:|")
	for r in resultados:
		print(
			f"| {r['n']} | {r['B']} | {r['dp_ms']:.3f} | {r['voraz_ms']:.3f} | "
			f"{r['brecha_pct']:.2f} | {r['coincidencias']}/{r['muestras']} |"
		)


if __name__ == "__main__":
	# Pares (n, B) para observar crecimiento por tamano de entrada.
	configuraciones = [(20, 100), (40, 200), (80, 400), (120, 800)]
	resultados = ejecutar_benchmark(configuraciones, muestras=10, repeticiones=3, semilla=42)
	print("Resultados de benchmark DP vs Voraz\n")
	imprimir_tabla_markdown(resultados)
