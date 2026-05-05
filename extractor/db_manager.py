import psycopg2
import os
import logging
from dotenv import load_dotenv

load_dotenv()

def guardar_precio_db(data):
    conn = None
    try:

        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS")
        )
        cur = conn.cursor()

        query = """
            INSERT INTO precios_commodities 
            (nombre_commodity, precio, unidad, fuente_dato) 
            VALUES (%s, %s, %s, %s);
        """
        cur.execute(query, (
            data['nombre'], 
            data['precio'], 
            data['unidad'], 
            data['fuente']
        ))

        conn.commit()
        print(f"Registro exitoso: {data['nombre']} a {data['precio']} {data['unidad']}")
        
        cur.close()
    except Exception as error:
        logging.info(f"Error al guardar en PostgreSQL: {error}")
    finally:
        if conn is not None:
            conn.close()

def obtener_ultimos_precios(nombre_commodity, limite=10):
    conn = None
    precios = []
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS")
        )
        cur = conn.cursor()

        query = """
            SELECT precio FROM precios_commodities 
            WHERE nombre_commodity = %s 
            ORDER BY fecha_extraccion DESC 
            LIMIT %s;
        """
        cur.execute(query, (nombre_commodity, limite))

        precios = [row[0] for row in cur.fetchall()]
        
        cur.close()
    except Exception as e:
        logging.error(f"Error al consultar historial: {e}")
    finally:
        if conn:
            conn.close()
    return precios