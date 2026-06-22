# Capítulo 8 - Calculadora de Riesgo y Stop Loss
# Autor: Tu Libro de Python Trading

import pandas as pd

print("--- CALCULADORA DE RIESGO PROFESIONAL ---\n")

# ============================================
# 1. REGLA DEL 1% - Tamaño de posición
# ============================================
def calcular_tamano_posicion(capital_total, precio_entrada, precio_stop_loss, riesgo_porcentaje=0.01):
    """
    Calcula cuántas unidades comprar respetando la regla del riesgo.
    """
    riesgo_maximo = capital_total * riesgo_porcentaje
    riesgo_por_unidad = abs(precio_entrada - precio_stop_loss)
    unidades = int(riesgo_maximo / riesgo_por_unidad)
    riesgo_real = unidades * riesgo_por_unidad
    return unidades, riesgo_real

print("1. REGLA DEL 1% - Tamaño de posición")
print("-" * 40)
capital = 10000
entrada = 50.0
stop = 48.0

unidades, riesgo = calcular_tamano_posicion(capital, entrada, stop)
print(f"Capital total: ${capital}")
print(f"Precio de entrada: ${entrada}")
print(f"Stop Loss: ${stop}")
print(f"Unidades a comprar: {unidades}")
print(f"Riesgo total: ${riesgo}")
print(f"Riesgo como % del capital: {(riesgo/capital)*100:.2f}%")
print("\n")

# ============================================
# 2. TIPOS DE STOP LOSS
# ============================================
print("2. TIPOS DE STOP LOSS")
print("-" * 40)

# Stop Loss fijo
def stop_loss_fijo(precio_entrada, porcentaje_stop=0.02):
    return precio_entrada * (1 - porcentaje_stop)

entrada = 100.0
stop_fijo = stop_loss_fijo(entrada, 0.02)
print(f"Stop Loss fijo al 2%: ${stop_fijo}")

# Stop Loss basado en ATR
def calcular_atr(datos, periodo=14):
    high = datos['High']
    low = datos['Low']
    close = datos['Close'].shift(1)
    tr1 = high - low
    tr2 = abs(high - close)
    tr3 = abs(low - close)
    true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    atr = true_range.rolling(window=periodo).mean()
    return atr

def stop_loss_atr(precio_entrada, atr_valor, multiplicador=2.0):
    return precio_entrada - (atr_valor * multiplicador)

datos = pd.DataFrame({
    'High': [105, 107, 106, 108, 110, 109, 111, 112, 110, 113],
    'Low': [102, 104, 103, 105, 107, 106, 108, 109, 107, 110],
    'Close': [103, 106, 104, 107, 109, 108, 110, 111, 109, 112]
})

atr = calcular_atr(datos, periodo=5)
ultimo_atr = atr.iloc[-1]
entrada = 112.0
stop_atr = stop_loss_atr(entrada, ultimo_atr, multiplicador=2.0)
print(f"Último ATR: {ultimo_atr:.2f}")
print(f"Stop Loss basado en ATR (2x): ${stop_atr:.2f}")

# Trailing Stop
def trailing_stop(precio_actual, precio_maximo_alcanzado, distancia_trailing):
    stop_dinamico = precio_maximo_alcanzado - distancia_trailing
    return stop_dinamico

entrada = 100
maximo = 120
trailing = 5
stop_trailing = trailing_stop(120, 120, trailing)
print(f"Trailing Stop: ${stop_trailing}")
print("\n")

# ============================================
# 3. RATIO RIESGO/BENEFICIO
# ============================================
print("3. RATIO RIESGO/BENEFICIO")
print("-" * 40)

def evaluar_operacion(precio_entrada, stop_loss, take_profit):
    riesgo_por_unidad = abs(precio_entrada - stop_loss)
    beneficio_por_unidad = abs(take_profit - precio_entrada)
    
    if riesgo_por_unidad == 0:
        ratio_rr = 0
    else:
        ratio_rr = beneficio_por_unidad / riesgo_por_unidad
    
    merece_la_pena = ratio_rr >= 2.0
    
    return {
        'riesgo_por_unidad': riesgo_por_unidad,
        'beneficio_por_unidad': beneficio_por_unidad,
        'ratio_riesgo_beneficio': ratio_rr,
        'merece_la_pena': merece_la_pena,
        'mensaje': "Operación válida" if merece_la_pena else "Ratio insuficiente"
    }

# Ejemplo 1: Buena operación (ratio 1:3)
print("Ejemplo 1: Buena operación")
analisis = evaluar_operacion(
    precio_entrada=100,
    stop_loss=97,
    take_profit=109
)
for clave, valor in analisis.items():
    print(f"  {clave}: {valor}")

print("\nEjemplo 2: Mala operación")
analisis = evaluar_operacion(
    precio_entrada=100,
    stop_loss=98,
    take_profit=102
)
for clave, valor in analisis.items():
    print(f"  {clave}: {valor}")

print("\n--- Fin del script ---")
