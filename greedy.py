"""Solucion voraz para asignacion de presupuesto.

Ordena por ratio retorno/costo de mayor a menor y agrega mientras quepa.
No garantiza optimalidad para el caso 0/1.
"""


def knapsack_greedy(costos, retornos, B):
	"""Retorna (valor_total, indices_seleccionados)."""
	if len(costos) != len(retornos):
		raise ValueError("costos y retornos deben tener la misma longitud")
	if B < 0:
		raise ValueError("el presupuesto B no puede ser negativo")

	proyectos = []
	for i, (costo, retorno) in enumerate(zip(costos, retornos)):
		if costo <= 0:
			raise ValueError("todos los costos deben ser mayores que 0")
		ratio = retorno / costo
		proyectos.append((ratio, retorno, costo, i))

	proyectos.sort(reverse=True)

	valor_total = 0
	presupuesto_usado = 0
	seleccion = []

	for _, retorno, costo, idx in proyectos:
		if presupuesto_usado + costo <= B:
			presupuesto_usado += costo
			valor_total += retorno
			seleccion.append(idx)

	seleccion.sort()
	return valor_total, seleccion
