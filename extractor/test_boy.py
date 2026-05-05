from notificador import enviar_alerta_telegram
import logging

# Configuramos un log básico para ver qué pasa en la consola
logging.basicConfig(level=logging.INFO)

print("Solicitando envío de mensaje de prueba...")
enviar_alerta_telegram("🚀 *Test de Integración*\n\nSi lees esto, el monitor de commodities está conectado correctamente con Telegram.")
print("Proceso terminado. Revisa tu celular.")