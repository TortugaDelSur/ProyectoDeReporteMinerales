import time
import logging
import pandas as pd
from extractor_commodities import extraer_info_commodity
from db_manager import guardar_precio_db, obtener_ultimos_precios
from notificador import enviar_alerta_telegram

# Configuración de Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='monitor.log'
)

# Lista de minerales escalable
MINERALES_OBJETIVO = [
    {"nombre": "Cobre", "url": "https://es.investing.com/commodities/copper"},
    {"nombre": "Oro", "url": "https://es.investing.com/commodities/gold"},
    {"nombre": "Plata", "url": "https://es.investing.com/commodities/silver"},
    {"nombre": "Platino", "url": "https://es.investing.com/commodities/platinum"}
]

def detectar_anomalia(precio_actual, nombre_commodity):
    historial = obtener_ultimos_precios(nombre_commodity)
    
    if len(historial) < 5:
        logging.info(f"[{nombre_commodity}] Datos insuficientes para calcular anomalías aún.")
        return False

    serie_precios = pd.Series(historial)
    promedio = serie_precios.mean()
    variacion = ((precio_actual - promedio) / promedio) * 100
    
    logging.info(f"[{nombre_commodity}] Promedio: {promedio:.2f} | Var: {variacion:.2f}%")

    # Umbral del 5%
    return abs(variacion) > 5

def ejecutar_monitor():
    logging.info("Iniciando servicio de monitoreo multimineral...")

    while True:
        logging.info("--- Iniciando nuevo ciclo de extracción ---")
        
        for mineral in MINERALES_OBJETIVO:   
            try:
                logging.info(f"Procesando {mineral['nombre']}...")
                datos = extraer_info_commodity(mineral['url'], mineral['nombre'])
                
                if datos:
                    # Validar anomalía
                    if detectar_anomalia(datos['precio'], datos['nombre']):
                        logging.warning(f"¡ANOMALÍA! {datos['nombre']} se desvió significativamente.")
                        msg = f"🚨 *ALERTA DE MERCADO*\n\nEl mineral *{datos['nombre']}* ha tenido una variación significativa.\n💰 Precio actual: {datos['precio']}\n📊 Revisa el dashboard en Grafana."
                        enviar_alerta_telegram(msg)
                    
                    # Guardar en base de datos
                    guardar_precio_db(datos)
                    logging.info(f"✅ {datos['nombre']} guardado: {datos['precio']}")
                else:
                    logging.warning(f"Falló extracción de {mineral['nombre']}")

                time.sleep(2)

            except Exception as e:
                logging.error(f"Error procesando {mineral['nombre']}: {e}")

        logging.info("Ciclo completado. Esperando 5 minutos para la próxima actualización...")
        print("Ciclo completado. Revisa monitor.log para detalles.")
        time.sleep(300)

if __name__ == "__main__":
    ejecutar_monitor()