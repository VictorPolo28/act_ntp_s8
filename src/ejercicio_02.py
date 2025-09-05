import pandas as pd

def calificaciones_estudiantes():
    serie = pd.Series([85, 92, 78], index=['Matemáticas', 'Ciencias', 'Historia'])

    print("Serie de Calificaciones:")
    print(serie)

    print("\nAcceder a Ciencias:")
    print(serie['Ciencias'])

    print("\nInformación básica:")
    print(serie.describe())

    print("\nSuma:", serie.sum())
    print("Promedio:", serie.mean())

calificaciones_estudiantes()

