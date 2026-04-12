"""Solucion por programacion dinamica para asignacion de presupuesto.

Modelo equivalente a 0/1 Knapsack:
- costos[i]: costo del proyecto i
- retornos[i]: retorno del proyecto i
- B: presupuesto maximo
"""


def knapsack_dp(costos, retornos, B):
	"""Retorna (valor_maximo, indices_seleccionados, tabla_dp)."""
	# Validar que los datos de entrada sean coherentes.
	if len(costos) != len(retornos):
		raise ValueError("costos y retornos deben tener la misma longitud")
	if B < 0:
		raise ValueError("el presupuesto B no puede ser negativo")

	n = len(costos)
	# Crear la tabla DP con casos base en cero.
	dp = [[0] * (B + 1) for _ in range(n + 1)]

	# Llenar la tabla con la mejor decision para cada proyecto y presupuesto.
	for i in range(1, n + 1):
		c_i = costos[i - 1]
		r_i = retornos[i - 1]
		for b in range(B + 1):
			if c_i > b:
				dp[i][b] = dp[i - 1][b]
			else:
				dp[i][b] = max(dp[i - 1][b], r_i + dp[i - 1][b - c_i])

	# Reconstruir los proyectos elegidos desde la tabla final.
	seleccion = []
	b = B
	for i in range(n, 0, -1):
		if dp[i][b] != dp[i - 1][b]:
			seleccion.append(i - 1)
			b -= costos[i - 1]

	seleccion.reverse()
	return dp[n][B], seleccion, dp
