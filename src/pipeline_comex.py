import pandas as pd
import numpy as np
import requests

def obtener_trm_actual():
    """Obtiene la TRM en tiempo real desde la API de Datos Abiertos Colombia"""
    try:
        url = "https://www.datos.gov.co/resource/32sa-8p3r.json?$limit=1&$order=vigenciahasta%20DESC"
        res = requests.get(url, timeout=5).json()
        return float(res[0]['valor'])
    except Exception as e:
        print("Error al conectar con API. Usando TRM por defecto:", e)
        return 4000.0

if __name__ == "__main__":
    trm = obtener_trm_actual()
    print(f"TRM USD/COP actual consultada: ${trm:,.2f}")
    print("Pipeline de Machine Learning inicializado con éxito.")
