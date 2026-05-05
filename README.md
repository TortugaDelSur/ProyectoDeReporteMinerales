Este es un diseño de README.md con un enfoque de ingeniería, estructurado para resaltar la arquitectura de microservicios y la robustez del código. Está optimizado para ser leído por reclutadores técnicos o arquitectos de software, eliminando elementos visuales informales y priorizando la claridad técnica.

Real-Time Commodities Monitoring System
1. Descripción del Proyecto
Este sistema automatizado de ingeniería de datos permite el monitoreo constante de precios de minerales (Cobre, Oro, Plata, Platino) mediante la extracción de datos desde fuentes financieras (Investing.com). El proyecto utiliza una arquitectura de microservicios orquestada con Docker, que integra servicios de extracción, almacenamiento relacional y observabilidad en tiempo real.

2. Stack Tecnológico
Lenguaje de Programación: Python 3.11.

Gestión de Datos: Pandas (Análisis estadístico y detección de anomalías).

Base de Datos: PostgreSQL 15.

Visualización: Grafana OSS.

Contenerización: Docker & Docker Compose.

Notificaciones: Integración con Telegram Bot API.

3. Arquitectura del Sistema
El flujo de datos sigue el modelo ETL (Extract, Transform, Load) optimizado para series temporales:

Capa de Ingesta: El servicio de Python ejecuta ciclos de scraping cada 5 minutos, procesando el DOM mediante BeautifulSoup y gestionando la resiliencia ante errores de red.

Capa de Transformación y Análisis: Se implementa lógica de detección de anomalías utilizando promedios móviles con Pandas. Si la variación del precio actual supera el 5% respecto al promedio histórico, se cataloga como evento crítico.

Capa de Persistencia: Almacenamiento en PostgreSQL mediante conexiones parametrizadas con psycopg2.

Capa de Presentación: Dashboard dinámico en Grafana conectado directamente al volumen de la base de datos.


4. Instrucciones de Instalación y Despliegue
Requisitos Previos
Docker Engine instalado.

Docker Compose v2.0+.

Pasos para el Despliegue
Clone el repositorio:

Bash
git clone https://github.com/tu-usuario/nombre-del-repo.git
cd nombre-del-repo
Configure las variables de entorno:

Bash
   cp extrator/.env.example extrator/.env
   # Edite extrator/.env con sus credenciales de base de datos y tokens de API
Levante la infraestructura completa:

Bash
   docker-compose up -d --build
5. Configuración de Alertas (Opcional)
El sistema incluye un módulo de notificaciones vía Telegram. Para activarlo, se debe modificar la variable TELEGRAM_ENABLED en el archivo .env a true y proporcionar el TELEGRAM_TOKEN y TELEGRAM_CHAT_ID correspondientes.

6. Acceso al Dashboard
Una vez que el sistema esté en ejecución, los tableros de visualización estarán disponibles en la siguiente dirección:

URL: http://localhost:3000

Credenciales por defecto: admin / admin

Autor
Diego

Técnico Analista Programador | Estudiante de Ingeniería en Informática.