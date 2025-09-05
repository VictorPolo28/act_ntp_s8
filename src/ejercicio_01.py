import pandas as pd

def analisis_ventas():
    ventas = pd.Series([150, 200, 180, 220, 175, 190, 165])
    print("Serie de ventas diarias: ")
    print(ventas)

    print("\nAcceder al índice 3:")
    print(ventas[3])

    print("\nPromedio de ventas:")
    print(ventas.mean())

    print("\nSerie ordenada por valores:")
    print(ventas.sort_values())


analisis_ventas()