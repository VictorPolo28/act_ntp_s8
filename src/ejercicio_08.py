import pandas as pd
import json

def leer_json():
    filename = "vehiculos.json"

    vehiculos = [
        {"marca": "Toyota", "modelo": "Corolla", "año": 2020},
        {"marca": "Ford", "modelo": "Fiesta", "año": 2018},
        {"marca": "Honda", "modelo": "Civic", "año": 2019}
    ]

    # Guardar JSON
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(vehiculos, file, ensure_ascii=False, indent=4)

    # Leer JSON
    df = pd.read_json(filename)
    print("DataFrame de Vehículos:")
    print(df)

    print("\nTipos de Datos:")
    print(df.dtypes)

leer_json()    