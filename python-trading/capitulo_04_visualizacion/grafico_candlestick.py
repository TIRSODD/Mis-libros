# Capítulo 4 - Gráfico de velas japonesas con mplfinance
# Autor: Tu Libro de Python Trading

import pandas as pd
import mplfinance as mpf

# Datos de ejemplo con estructura OHLCV completa
datos = {
    'Date': ['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05',
             '2023-10-06', '2023-10-07', '2023-10-08', '2023-10-09', '2023-10-10'],
    'Open': [150.0, 152.0, 151.5, 154.0, 156.0, 155.5, 157.0, 158.5, 159.0, 160.0],
    'High': [153.0, 154.0, 155.0, 157.0, 158.0, 157.5, 159.0, 160.5, 161.0, 162.0],
    'Low': [149.0, 150.5, 150.0, 153.0, 154.5, 154.0, 155.5, 157.0, 157.5, 158.5],
    'Close': [152.0, 151.5, 154.0, 156.0, 155.5, 157.0, 158.5, 159.0, 160.0, 161.5],
    'Volume': [1000000, 1200000, 900000, 1500000, 1800000, 1600000, 1400000, 1700000, 1900000, 2000000]
}

df = pd.DataFrame(datos)

# Convertimos la columna Date a datetime y la establecemos como índice
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# ¡Y ahora el gráfico de velas en UNA SOLA LÍNEA!
mpf.plot(df, type='candle', style='charles', title='Gráfico de Velas - AAPL',
         ylabel='Precio ($)', volume=True, ylabel_lower='Volumen')
