import pandas as pd
import csv

def leer_csv():
    filename = "cursos.csv"

    # Crear archivo CSV
    cursos = [
        ['curso', 'instructor', 'duracion'],
        ['Python Básico', 'Ana', '20h'],
        ['Java Intermedio', 'Luis', '25h'],
        ['Machine Learning', 'Marta', '30h']
    ]

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(cursos)

    # Leer archivo CSV
    try:
        df = pd.read_csv(filename)
        print("DataFrame leído desde CSV:")
        print(df)
    except FileNotFoundError:
        print("El archivo no existe.")

leer_csv()        