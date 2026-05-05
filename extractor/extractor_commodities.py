import requests
import pandas as pd
import logging
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def extraer_info_commodity(url, nombre_item):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        

        elemento_precio = soup.find("div", {"data-test": "instrument-price-last"})
        
        if elemento_precio:
            precio_texto = elemento_precio.text

            precio_limpio = float(precio_texto.replace(".", "").replace(",", "."))

            return {
                "nombre": nombre_item,
                "precio": precio_limpio,
                "unidad": "USD/lb",
                "fuente": url,
                "fecha": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
    except Exception as e:
        logging.info(f"Error extrayendo {nombre_item}: {e}")
    return None

