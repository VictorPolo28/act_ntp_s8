import pandas as pd
import numpy as np

def dataframe_numpy():
    ventas = np.array([
        [1000, 1200, 1100],
        [1500, 1600, 1550],
        [2000, 2100, 2050]
    ])

    df = pd.DataFrame(ventas, columns=['Q1', 'Q2', 'Q3'])

    print("DataFrame de Ventas Trimestrales:")
    print(df)

    print("\nTipos de Datos:")
    print(df.dtypes)
dataframe_numpy()    