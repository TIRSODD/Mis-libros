# Capítulo 9 - Alertas de Telegram para monitorización
# Autor: Tu Libro de Python Trading

import requests

# Configuración de Telegram
# IMPORTANTE: Reemplaza estos valores con tu Token y Chat ID reales.
# Nunca subas tus credenciales reales a un repositorio público.
TELEGRAM_BOT_TOKEN = "TU_TOKEN_AQUI"
TELEGRAM_CHAT_ID = "TU_CHAT_ID_AQUI"

def enviar_alerta_telegram(mensaje):
    """Envía un mensaje a tu canal o chat privado de Telegram."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    parametros = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': mensaje,
        'parse_mode': 'HTML' # Permite usar negritas y cursivas
    }
    
    try:
        respuesta = requests.get(url, params=parametros)
        if respuesta.status_code == 200:
            print("Alerta enviada a Telegram correctamente.")
        else:
            print(f"Error al enviar a Telegram: {respuesta.text}")
    except Exception as e:
        print(f"Fallo de conexión con Telegram: {e}")

# Ejemplo de uso en el bot
def ejecutar_operacion_real(simbolo, precio):
    print(f"Simulando ejecución de orden para {simbolo} a ${precio}...")
    
    mensaje = f"🚨 <b>OPERACIÓN EJECUTADA</b>\n\n"
    mensaje += f"Activo: {simbolo}\n"
    mensaje += f"Precio: ${precio}\n"
    mensaje += f"Estado: ✅ Orden de mercado enviada."
    
    enviar_alerta_telegram(mensaje)

# Prueba del script
if __name__ == "__main__":
    print("--- Sistema de Alertas Telegram ---")
    # Descomenta la siguiente línea para probar el envío real si tienes el Token configurado
    # ejecutar_operacion_real("AAPL", 150.50)
    print("Script de alertas cargado correctamente.")
