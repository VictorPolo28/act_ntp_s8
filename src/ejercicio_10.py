import pandas as pd
import requests

def consumir_api():
    url = "https://playground.mockoon.com/users"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            df = pd.DataFrame(response.json())
            print("Primeras 5 filas del DataFrame:")
            print(df.head())

            print("\nInformación del DataFrame:")
            print(df.info())
        else:
            print(f"Error en la petición. Código: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print("Error de conexión:", e)

        
consumir_api()        