# Capítulo 4 - Gráfico interactivo con Plotly
# Autor: Tu Libro de Python Trading

import pandas as pd
import plotly.graph_objects as go

# 1. Datos de ejemplo con estructura OHLCV completa
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
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Calculamos la media móvil de 3 periodos
df['SMA_3'] = df['Close'].rolling(window=3).mean()

# 2. Creamos la figura con velas japonesas
fig = go.Figure(data=[go.Candlestick(
    x=df.index,
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close'],
    name='Velas Japonesas'
)])

# 3. Añadimos la media móvil
fig.add_trace(go.Scatter(
    x=df.index,
    y=df['SMA_3'],
    mode='lines',
    name='SMA 3',
    line=dict(color='blue', width=2)
))

# 4. Personalizamos el layout
fig.update_layout(
    title='Gráfico Interactivo - AAPL',
    xaxis_title='Fecha',
    yaxis_title='Precio ($)',
    template='plotly_dark',
    hovermode='x unified'
)

# 5. Mostramos el gráfico (se abrirá en el navegador)
fig.show()
