import pandas as pd

def dataframe_lista_diccionarios():
    empleados = [
        {'empleado': 'Ana', 'salario': 3000, 'departamento': 'Ventas'},
        {'empleado': 'Luis', 'salario': 3500, 'departamento': 'TI'},
        {'empleado': 'Marta', 'salario': 4000, 'departamento': 'RRHH'}
    ]

    df = pd.DataFrame(empleados)

    print("DataFrame de Empleados:")
    print(df)

    print("\nAcceder a la primera fila:")
    print(df.loc[0])

dataframe_lista_diccionarios()    