import pandas as pd

def dataframe_lista_listas():
    libros = [
        ['Cien Años de Soledad', 'Gabriel García Márquez', 1967],
        ['Don Quijote', 'Miguel de Cervantes', 1605],
        ['El Principito', 'Antoine de Saint-Exupéry', 1943]
    ]

    columnas = ['Titulo', 'Autor', 'Año']
    df = pd.DataFrame(libros, columns=columnas)

    print("DataFrame de Libros:")
    print(df)

    print("\nDimensiones del DataFrame:")
    print(df.shape)

dataframe_lista_listas()    