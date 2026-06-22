# Capítulo 6 - Bot de Trading en modo Paper Trading (Simulado)
# Autor: Tu Libro de Python Trading

import time
import pandas as pd
import yfinance as yf

# --- CONFIGURACIÓN DE LA ESTRATEGIA ---
SIMBOLO = "AAPL"          # El activo que vamos a operar
VENTANA_SMA_RAPIDA = 10   # Periodo de la media móvil rápida
VENTANA_SMA_LENTA = 30    # Periodo de la media móvil lenta
INTERVALO = "1d"          # Temporalidad: 1 día
CAPITAL_INICIAL = 10000   # Dinero ficticio para empezar (10.000 $)

# --- ESTADO DEL BOT ---
capital = CAPITAL_INICIAL
posicion = 0              # Número de acciones que tenemos (0 = no tenemos nada)
precio_compra = 0.0       # Precio al que compramos las acciones actuales

def analizar_mercado(datos):
    """
    Calcula indicadores y genera señales de trading.
    """
    # Calculamos las medias móviles
    datos['SMA_Rapida'] = datos['Close'].rolling(window=VENTANA_SMA_RAPIDA).mean()
    datos['SMA_Lenta'] = datos['Close'].rolling(window=VENTANA_SMA_LENTA).mean()
    
    # Obtenemos los dos últimos valores para ver si hay un cruce
    ultimo = datos.iloc[-1]
    anterior = datos.iloc[-2]
    
    # Lógica de cruce de medias:
    # COMPRA: La rápida cruza por encima de la lenta
    if anterior['SMA_Rapida'] <= anterior['SMA_Lenta'] and ultimo['SMA_Rapida'] > ultimo['SMA_Lenta']:
        return "COMPRA", ultimo['Close']
    
    # VENTA: La rápida cruza por debajo de la lenta
    elif anterior['SMA_Rapida'] >= anterior['SMA_Lenta'] and ultimo['SMA_Rapida'] < ultimo['SMA_Lenta']:
        return "VENTA", ultimo['Close']
    
    # Si no hay cruce, no hacemos nada
    else:
        return "ESPERAR", ultimo['Close']

def ejecutar_operacion(accion, precio_actual):
    global capital, posicion, precio_compra
    
    if accion == "COMPRA" and posicion == 0:
        # Si no tenemos posición y hay señal de compra
        # Calculamos cuántas acciones podemos comprar (usamos el 90% del capital para dejar margen)
        acciones_a_comprar = int((capital * 0.90) / precio_actual)
        
        if acciones_a_comprar > 0:
            costo = acciones_a_comprar * precio_actual
            capital -= costo
            posicion = acciones_a_comprar
            precio_compra = precio_actual
            print(f"🟢 COMPRA ejecutada: {acciones_a_comprar} acciones a ${precio_actual:.2f}")
            
    elif accion == "VENTA" and posicion > 0:
        # Si tenemos posición y hay señal de venta
        ingresos = posicion * precio_actual
        beneficio = ingresos - (posicion * precio_compra)
        capital += ingresos
        posicion = 0
        precio_compra = 0.0
        print(f"🔴 VENTA ejecutada a ${precio_actual:.2f}. Beneficio: ${beneficio:.2f}")

def main():
    global capital, posicion
    
    print(f"Iniciando Bot para {SIMBOLO}...")
    print(f"Capital inicial: ${capital}")
    print("-" * 40)
    
    while True:
        try:
            print(f"\n[{time.strftime('%Y-%m-%d %H:%M:%S')}] Analizando mercado...")
            
            # 1. OBSERVAR: Descargamos datos recientes
            datos = yf.download(SIMBOLO, period="2mo", interval=INTERVALO)
            
            # Necesitamos al menos 30 datos para calcular la media lenta
            if len(datos) < VENTANA_SMA_LENTA:
                print("Datos insuficientes para calcular indicadores. Esperando...")
                time.sleep(60)
                continue
            
            # 2. PENSAR: Analizamos los datos
            decision, precio = analizar_mercado(datos)
            print(f"Precio actual: ${precio:.2f} | Señal: {decision}")
            
            # 3. ACTUAR: Si hay señal, ejecutamos
            if decision != "ESPERAR":
                ejecutar_operacion(decision, precio)
            
            # Mostramos el estado de la cartera
            valor_cartera = capital + (posicion * precio)
            print(f"Estado: Capital=${capital:.2f} | Posición={posicion} acciones | Valor Total=${valor_cartera:.2f}")
            
            # 4. DORMIR: Esperamos 60 segundos para la prueba
            # En producción real esto sería 86400 (24 horas) para datos diarios
            print("Esperando próxima sesión...")
            time.sleep(60) 
            
        except Exception as e:
            print(f" Ocurrió un error: {e}")
            print("Reintentando en 60 segundos...")
            time.sleep(60)

# Iniciamos el bot
if __name__ == "__main__":
    main()
