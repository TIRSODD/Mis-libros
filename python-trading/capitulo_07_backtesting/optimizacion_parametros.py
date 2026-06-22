# Capítulo 7 - Optimización de parámetros con VectorBT
# Autor: Tu Libro de Python Trading

import vectorbt as vbt
import yfinance as yf

print("--- Optimización de Parámetros ---\n")

# 1. Descargamos datos históricos reales de Apple (5 años)
print("Descargando datos históricos de AAPL (5 años)...")
datos = yf.download("AAPL", period="5y")
datos.columns = [col[0] for col in datos.columns]

# 2. Definimos rangos de parámetros a probar
print("\nProbando diferentes combinaciones de medias móviles...")
ventanas_rapidas = range(5, 20, 2)  # 5, 7, 9, 11, 13, 15, 17, 19
ventanas_lentas = range(20, 50, 5)  # 20, 25, 30, 35, 40, 45

print(f"Medias rápidas a probar: {list(ventanas_rapidas)}")
print(f"Medias lentas a probar: {list(ventanas_lentas)}")
print(f"Total de combinaciones: {len(ventanas_rapidas) * len(ventanas_lentas)}")

# 3. VectorBT prueba todas las combinaciones automáticamente
print("\nEjecutando backtests para todas las combinaciones...")
sma_rapida = vbt.MA.run(datos['Close'], window=ventanas_rapidas, per_column=True)
sma_lenta = vbt.MA.run(datos['Close'], window=ventanas_lentas, per_column=True)

# 4. Generamos señales para todas las combinaciones
entradas, salidas = vbt.crossed_above(sma_rapida.ma, sma_lenta.ma), vbt.crossed_below(sma_rapida.ma, sma_lenta.ma)

# 5. Ejecutamos backtests para todas las combinaciones
portfolios = vbt.Portfolio.from_signals(
    close=datos['Close'],
    entries=entradas,
    exits=salidas,
    init_cash=10000,
    fees=0.001,
    freq='1D'
)

# 6. Mostramos los resultados ordenados por retorno total
print("\n" + "=" * 70)
print("TOP 5 COMBINACIONES POR RETORNO TOTAL")
print("=" * 70)

# Obtenemos los índices de las mejores combinaciones
top_5_indices = portfolios.total_return().sort_values().tail(5).index

for i, (rapida_idx, lenta_idx) in enumerate(top_5_indices, 1):
    rapida = ventanas_rapidas[rapida_idx] if rapida_idx < len(ventanas_rapidas) else rapida_idx
    lenta = ventanas_lentas[lenta_idx] if lenta_idx < len(ventanas_lentas) else lenta_idx
    
    retorno = portfolios.total_return().loc[(rapida_idx, lenta_idx)]
    sharpe = portfolios.sharpe_ratio().loc[(rapida_idx, lenta_idx)]
    drawdown = portfolios.max_drawdown().loc[(rapida_idx, lenta_idx)]
    
    print(f"\n#{i} - SMA Rápida: {rapida:2d} | SMA Lenta: {lenta:2d}")
    print(f"    Retorno: ${retorno:,.2f} | Sharpe: {sharpe:.2f} | Drawdown: ${drawdown:,.2f}")

print("\n" + "=" * 70)

# 7. Análisis de estabilidad
print("\n--- ANÁLISIS DE ESTABILIDAD ---")
print("Buscamos combinaciones que funcionen bien de forma consistente...")

# Calculamos la media y desviación estándar de los retornos
media_retorno = portfolios.total_return().mean()
std_retorno = portfolios.total_return().std()

print(f"Retorno promedio de todas las combinaciones: ${media_retorno:,.2f}")
print(f"Desviación estándar: ${std_retorno:,.2f}")

# Encontramos combinaciones estables (dentro de 1 desviación estándar del mejor retorno)
mejor_retorno = portfolios.total_return().max()
umbral_estabilidad = mejor_retorno - std_retorno

combinaciones_estables = portfolios.total_return()[portfolios.total_return() >= umbral_estabilidad]
print(f"\nCombinaciones estables (dentro de 1 desviación del mejor retorno): {len(combinaciones_estables)}")

if len(combinaciones_estables) > 0:
    print("Estas son las combinaciones más robustas:")
    for idx in combinaciones_estables.index[:3]:  # Mostramos las 3 primeras
        rapida_idx, lenta_idx = idx
        rapida = ventanas_rapidas[rapida_idx] if rapida_idx < len(ventanas_rapidas) else rapida_idx
        lenta = ventanas_lentas[lenta_idx] if lenta_idx < len(ventanas_lentas) else lenta_idx
        retorno = combinaciones_estables.loc[(rapida_idx, lenta_idx)]
        print(f"  - SMA({rapida}, {lenta}): ${retorno:,.2f}")

print("\n" + "=" * 70)
print("✅ Optimización completada.")
print("\n⚠️  RECUERDA:")
print("   - No elijas solo la combinación con mejor retorno (overfitting)")
print("   - Busca zonas de estabilidad con múltiples combinaciones similares")
print("   - Valida siempre con datos fuera de muestra (out-of-sample)")
print("=" * 70)
