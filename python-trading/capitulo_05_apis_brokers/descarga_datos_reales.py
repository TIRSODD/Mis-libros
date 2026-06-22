# Capítulo 5 - Descarga de datos históricos reales con yfinance
# Autor: Tu Libro de Python Trading

import yfinance as yf
import pandas as pd

print("--- Descarga de Datos Reales de Yahoo Finance ---\n")

# 1. Descargamos datos reales de Apple (AAPL) de los últimos 3 meses
# 'period="3mo"' significa 3 meses. También podríamos usar fechas exactas.
print("Descargando datos reales de Apple (AAPL) de los últimos 3 meses...")
df = yf.download("AAPL", period="3mo")

# yfinance devuelve un DataFrame con índices jerárquicos. Lo simplificamos:
df.columns = [col[0] for col in df.columns]

# 2. Vemos las primeras filas
print("\n--- Primeras filas de datos reales ---")
print(df.head())

# 3. Calculamos la Media Móvil Simple de 20 días
print("\n--- Calculando Media Móvil de 20 días ---")
df['SMA_20'] = df['Close'].rolling(window=20).mean()

# 4. Mostramos los últimos 5 días con el indicador calculado
print("\n--- Últimos 5 días con SMA 20 ---")
print(df[['Close', 'SMA_20']].tail())

# 5. Información adicional
print("\n--- Información del DataFrame ---")
print(f"Total de filas descargadas: {len(df)}")
print(f"Columnas disponibles: {list(df.columns)}")
print(f"Fecha más antigua: {df.index.min()}")
print(f"Fecha más reciente: {df.index.max()}")

print("\n✅ Datos descargados y procesados correctamente.")
