# Capítulo 7 - Backtesting con VectorBT
# Autor: Tu Libro de Python Trading

import vectorbt as vbt
import yfinance as yf

print("--- Iniciando Backtest con VectorBT ---\n")

# 1. Descargamos datos históricos reales de Apple (5 años)
print("Descargando datos históricos de AAPL (5 años)...")
datos = yf.download("AAPL", period="5y")

# yfinance devuelve un DataFrame con índices jerárquicos. Lo simplificamos:
datos.columns = [col[0] for col in datos.columns]

# 2. Definimos la estrategia: cruce de medias móviles
ventana_rapida = 10
ventana_lenta = 30

# 3. Calculamos las medias móviles
sma_rapida = vbt.MA.run(datos['Close'], window=ventana_rapida)
sma_lenta = vbt.MA.run(datos['Close'], window=ventana_lenta)

# 4. Generamos las señales de entrada y salida
entradas = sma_rapida.ma_crossed_above(sma_lenta)
salidas = sma_rapida.ma_crossed_below(sma_lenta)

# 5. Ejecutamos el backtest
portfolio = vbt.Portfolio.from_signals(
    close=datos['Close'],
    entries=entradas,
    exits=salidas,
    init_cash=10000,  # Capital inicial: 10.000$
    fees=0.001,       # Comisiones: 0.1% por operación
    freq='1D'         # Frecuencia: diaria
)

# 6. Mostramos los resultados básicos
print("\n" + "=" * 50)
print("RESULTADOS DEL BACKTEST")
print("=" * 50)
print(f"Estrategia: Cruce de medias {ventana_rapida}/{ventana_lenta}")
print(f"Periodo: 5 años de datos de AAPL")
print(f"Capital inicial: $10,000")
print(f"Capital final: ${portfolio.final_value():,.2f}")
print(f"Beneficio total: ${portfolio.total_return():,.2f}")
print(f"Retorno (%): {portfolio.total_return() / 10000 * 100:.2f}%")
print(f"Número de operaciones: {portfolio.trades.count()}")
print(f"Win Rate (%): {portfolio.trades.win_rate() * 100:.2f}%")

# 7. Métricas de riesgo avanzadas
print("\n--- MÉTRICAS DE RIESGO ---")
print(f"Drawdown máximo: ${portfolio.max_drawdown():,.2f}")
print(f"Drawdown máximo (%): {portfolio.max_drawdown() / 10000 * 100:.2f}%")
print(f"Profit Factor: {portfolio.trades.profit_factor():.2f}")
print(f"Ratio de Sharpe: {portfolio.sharpe_ratio():.2f}")
print("=" * 50)
