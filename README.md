# Proyecto-1-ADA-II

Implementacion del problema de asignacion de presupuesto limitado con dos enfoques:

- Programacion Dinamica (modelo 0/1 Knapsack)
- Enfoque Voraz por ratio retorno/costo

## Estructura

- `dp.py`: solucion por Programacion Dinamica.
- `greedy.py`: solucion voraz por ratio retorno/costo.
- `main.py`: ejecucion de casos de ejemplo y comparacion DP vs Voraz.
- `tests.py`: pruebas unitarias para ambos enfoques.
- `benchmark.py`: pruebas de rendimiento por tamano de entrada (DP vs Voraz).
- `EXPLICACION_DP.md`: explicacion teorica y ejemplo manual de la solucion DP.
- `EXPLICACION_VORAZ.md`: explicacion del enfoque voraz, complejidad y contraejemplo.
- `requirements.txt`: dependencias del proyecto (no hay dependencias externas).

## Requisitos

- Python 3.10+ (recomendado: Python 3.12)

## Instalacion

Este proyecto no requiere librerias externas. Si deseas usar entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar el codigo

Desde la carpeta del proyecto:

```bash
python main.py
```

Si usas entorno virtual local en `.venv`:

```bash
.venv/bin/python main.py
```

## Ejecutar pruebas

```bash
python -m unittest tests.py
```

Si usas entorno virtual local en `.venv`:

```bash
.venv/bin/python -m unittest tests.py
```

## Pruebas comparativas por tamano de entrada

Para analizar el comportamiento con diferentes tamanos de entrada:

```bash
python benchmark.py
```

Si usas entorno virtual local en `.venv`:

```bash
.venv/bin/python benchmark.py
```

El script reporta:

- Tiempo promedio de DP y Voraz (ms).
- Brecha porcentual promedio respecto al optimo DP.
- Coincidencias exactas entre Voraz y DP.

Con esto se cubre el analisis del punto 5: comparacion de resultados y discusion segun tamano de entrada.

## Modelo DP implementado

Se define `dp[i][b]` como el maximo retorno usando los primeros `i` proyectos con presupuesto `b`.

- Casos base:
	- `dp[0][b] = 0`
	- `dp[i][0] = 0`
- Recurrencia:
	- Si `c[i] > b`: `dp[i][b] = dp[i-1][b]`
	- Si `c[i] <= b`: `dp[i][b] = max(dp[i-1][b], r[i] + dp[i-1][b-c[i]])`
- Respuesta final: `dp[n][B]`

Complejidad:

- Tiempo: `O(n * B)`
- Espacio: `O(n * B)`