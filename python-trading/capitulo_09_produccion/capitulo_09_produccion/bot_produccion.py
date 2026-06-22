# Capítulo 9 - Bot de Trading en Producción con sistema de Logs
# Autor: Tu Libro de Python Trading

import logging
import time
from datetime import datetime

# ============================================
# 1. CONFIGURACIÓN DEL SISTEMA DE LOGS
# ============================================
# Creamos un archivo llamado 'bot_trading.log' donde se guardará todo
logging.basicConfig(
    filename='bot_trading.log',
    level=logging.INFO,  # Nivel de detalle (INFO, WARNING, ERROR)
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Función para enviar mensajes al log
def registrar_evento(mensaje, nivel='info'):
    if nivel == 'info':
        logging.info(mensaje)
    elif nivel == 'error':
        logging.error(mensaje)
    elif nivel == 'warning':
        logging.warning(mensaje)

# ============================================
# 2. LÓGICA DEL BOT (SIMULADA)
# ============================================
def obtener_datos_mercado():
    """Simula la obtención de datos de una API."""
    # En un bot real, aquí usarías yfinance o la API de tu broker
    return 150.00 + (time.time() % 10)

def analizar_y_ejecutar(precio):
    """Simula la lógica de trading."""
    if precio > 155.00:
        return "COMPRA"
    elif precio < 145.00:
        return "VENTA"
    else:
        return "ESPERAR"

# ============================================
# 3. BUCLE PRINCIPAL DE PRODUCCIÓN
# ============================================
def main():
    registrar_evento("Bot de producción iniciado correctamente.", nivel='info')
    registrar_evento("Conectando al mercado...", nivel='info')
    
    while True:
        try:
            # 1. Observar
            precio = obtener_datos_mercado()
            registrar_evento(f"Analizando mercado. Precio actual: ${precio:.2f}")
            
            # 2. Pensar y 3. Actuar
            decision = analizar_y_ejecutar(precio)
            
            if decision == "COMPRA":
                registrar_evento(f"SEÑAL DE COMPRA DETECTADA a ${precio:.2f}. Ejecutando orden...", nivel='warning')
                # Aquí iría la lógica real de ejecución con la API del broker
            elif decision == "VENTA":
                registrar_evento(f"SEÑAL DE VENTA DETECTADA a ${precio:.2f}. Ejecutando orden...", nivel='warning')
                # Aquí iría la lógica real de ejecución con la API del broker
            else:
                registrar_evento("Sin señales. Manteniendo posición.")
            
            # 4. Dormir (Esperamos 60 segundos para la simulación)
            time.sleep(60) 
            
        except Exception as e:
            # Si algo falla, lo registramos como ERROR pero el bot no se detiene
            registrar_evento(f"Ocurrió un error inesperado: {str(e)}", nivel='error')
            registrar_evento("Reintentando en 60 segundos...", nivel='warning')
            time.sleep(60)

# Iniciamos el bot
if __name__ == "__main__":
    main()
