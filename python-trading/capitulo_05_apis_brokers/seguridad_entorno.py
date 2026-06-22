# Capítulo 5 - Seguridad: Carga de API Keys desde archivo .env
# Autor: Tu Libro de Python Trading

# IMPORTANTE: Antes de ejecutar este script, necesitas instalar python-dotenv
# Ejecuta en tu terminal: pip install python-dotenv

# También necesitas crear un archivo llamado '.env' en la misma carpeta
# con este contenido:
# MI_API_KEY=tu_clave_publica_aqui
# MI_SECRET_KEY=tu_clave_secreta_aqui

import os
from dotenv import load_dotenv

print("--- Sistema de Seguridad para API Keys ---\n")

# Cargamos las variables del archivo .env
load_dotenv()

# Leemos las claves de forma segura
api_key = os.getenv("MI_API_KEY")
secret_key = os.getenv("MI_SECRET_KEY")

# Verificamos que se han cargado (sin imprimirlas en consola)
if api_key and secret_key:
    print("✅ Claves cargadas correctamente desde el archivo .env")
    print(f"   - API Key detectada: {api_key[:5]}...{api_key[-5:]}")
    print(f"   - Secret Key detectada: {secret_key[:5]}...{secret_key[-5:]}")
    print("\nListo para conectar con el broker de forma segura.")
else:
    print("❌ Error: Las claves no se han encontrado en el archivo .env")
    print("   Asegúrate de que el archivo .env existe y contiene:")
    print("   MI_API_KEY=tu_clave_publica_aqui")
    print("   MI_SECRET_KEY=tu_clave_secreta_aqui")

print("\n--- Fin del script ---")
