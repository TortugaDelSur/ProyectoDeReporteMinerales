import requests
import os
import logging
from dotenv import load_dotenv

load_dotenv()

def enviar_alerta_telegram(mensaje):
    if os.getenv("TELEGRAM_ENABLED", "false").lower() != "true":
        return

    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    payload = {
        "chat_id": chat_id,
        "text": mensaje,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            logging.info("📱 Alerta enviada a Telegram exitosamente.")
        else:
            logging.error(f"Error de Telegram: {response.text}")
    except Exception as e:
        logging.error(f"Error al conectar con Telegram: {e}")