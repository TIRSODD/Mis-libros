# Capítulo 3 - DataFrames y generación de señales con Pandas
# Autor: Tu Libro de Python Trading

import pandas as pd

# --- 1. Creando un DataFrame desde un diccionario ---
print("--- DataFrame desde diccionario ---")
datos = {
    'Fecha': ['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05'],
    'Cierre': [150.0, 152.5, 151.0, 155.0, 158.0],
    'Volumen': [1000000, 1200000, 900000, 1500000, 1800000]
}
df = pd.DataFrame(datos)
print(df)
print("\n")

# --- 2. Calculando una Media Móvil Simple ---
print("--- Media Móvil Simple de 3 periodos ---")
df['SMA_3'] = df['Cierre'].rolling(window=3).mean()
print(df)
print("\n")

# --- 3. Filtrado de datos ---
print("--- Filtrado: días con volumen alto ---")
df_alto_volumen = df[df['Volumen'] > 1000000]
print(df_alto_volumen)
print("\n")

# --- 4. Generando señales de compra/venta ---
print("--- Señales de trading ---")
df['Senal'] = 0
df.loc[df['Cierre'] > df['SMA_3'], 'Senal'] = 1
print(df)
