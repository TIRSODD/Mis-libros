# Capítulo 2 - Variables y operadores aplicados al trading

# Definición de variables para una operación de trading
ticker = "AAPL"                  # str: El activo que vamos a operar
precio_compra = 150.50           # float: Precio al que entramos
cantidad_acciones = 100          # int: Cuántas acciones compramos
posicion_abierta = True          # bool: ¿Estamos dentro del mercado?

# Podemos hacer cálculos usando estas variables
valor_cartera = precio_compra * cantidad_acciones

print(f"El valor de mi posición en {ticker} es: ${valor_cartera}")

# Ejemplo de lógica de señal de compra
precio_actual = 145.0
media_movil = 140.0
volumen_hoy = 5000000
volumen_medio = 4000000

# Queremos comprar si el precio supera la media Y el volumen es alto
senal_compra = (precio_actual > media_movil) and (volumen_hoy > volumen_medio)

print(f"¿Se genera señal de compra? {senal_compra}")

# Estructura de control: Tomando decisiones
precio_entrada = 100.0
precio_actual = 105.0
porcentaje_beneficio = (precio_actual - precio_entrada) / precio_entrada

# Lógica de toma de decisiones
if porcentaje_beneficio >= 0.10:
    print("¡Objetivo de beneficio alcanzado! Vendemos.")
elif porcentaje_beneficio <= -0.05:
    print("¡Stop Loss activado! Vendemos para limitar pérdidas.")
else:
    print("El precio está en rango. Mantenemos la posición.")
