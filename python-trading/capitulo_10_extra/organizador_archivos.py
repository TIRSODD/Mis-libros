# Capítulo 10 - Automatización de tareas: Organizador de archivos
# Autor: Tu Libro de Python Trading

import os
import shutil

def organizar_facturas(carpeta_origen):
    """
    Organiza archivos PDF de una carpeta en subcarpetas por año,
    basándose en los primeros 4 caracteres del nombre del archivo.
    """
    # Si la carpeta no existe, la creamos y generamos archivos de prueba
    if not os.path.exists(carpeta_origen):
        print(f"La carpeta '{carpeta_origen}' no existe. Creándola para la prueba...")
        os.makedirs(carpeta_origen)
        
        # Creamos algunos archivos PDF falsos para demostrar el funcionamiento
        nombres_prueba = [
            "2022_factura_luz.pdf", "2023_factura_agua.pdf", 
            "2023_factura_internet.pdf", "2024_factura_movil.pdf",
            "nota.txt" # Este no debería moverse porque no es PDF
        ]
        for nombre in nombres_prueba:
            open(os.path.join(carpeta_origen, nombre), 'w').close()
        print("Archivos de prueba creados.\n")

    archivos = os.listdir(carpeta_origen)
    archivos_movidos = 0

    for archivo in archivos:
        # Solo procesamos archivos PDF y que tengan al menos 4 caracteres
        if archivo.endswith(".pdf") and len(archivo) >= 4:
            # Supongamos que el año está en las primeras 4 letras del nombre
            anio = archivo[:4] 
            
            # Verificamos que sean números (un año)
            if anio.isdigit() and 2000 <= int(anio) <= 2099:
                # Creamos la carpeta del año si no existe
                ruta_carpeta = os.path.join(carpeta_origen, anio)
                os.makedirs(ruta_carpeta, exist_ok=True)
                
                # Rutas completas
                ruta_origen = os.path.join(carpeta_origen, archivo)
                ruta_destino = os.path.join(ruta_carpeta, archivo)
                
                # Movemos el archivo
                shutil.move(ruta_origen, ruta_destino)
                archivos_movidos += 1
                print(f"✅ Movido: {archivo} -> carpeta {anio}/")

    print(f"\n🎉 ¡Proceso completado! {archivos_movidos} facturas organizadas automáticamente.")

if __name__ == "__main__":
    print("--- Organizador Automático de Facturas ---\n")
    
    # Usamos una carpeta de prueba específica para no afectar tus archivos reales
    carpeta_prueba = "./facturas_desordenadas_prueba"
    
    organizar_facturas(carpeta_prueba)
    
    print("\n(Revisa tu carpeta de trabajo, verás que se han creado las subcarpetas 2022, 2023 y 2024)")
