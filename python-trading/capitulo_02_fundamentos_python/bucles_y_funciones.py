# Capítulo 2 - Bucles y Funciones aplicados al trading
# Autor: Tu Libro de Python Trading

# --- 1. El bucle FOR: Recorriendo listas de datos ---
print("--- Bucle FOR ---")
precios_cierre = [148.50, 150.25, 149.80, 152.10, 151.75]
cantidad = 10

for precio in precios_cierre:
    valor = precio * cantidad
    print(f"Si el precio fue {precio}, mi cartera valía: ${valor}")
print("\n")

# --- 2. El bucle WHILE: Calculando una Media Móvil ---
print("--- Bucle WHILE ---")
precios = [10, 12, 11, 14, 13, 15]
periodo = 3
indice = 0

print("Calculando Media Móvil Simple de 3 periodos:")
while indice <= len(precios) - periodo:
    ventana = precios[indice:indice + periodo]
    media = sum(ventana) / periodo
    print(f"Media en posición {indice}: {media}")
    indice += 1
print("\n")

# --- 3. Funciones: Calculadora de beneficio ---
print("--- Funciones ---")
def calcular_beneficio(precio_entrada, precio_salida, cantidad):
    beneficio_por_accion = precio_salida - precio_entrada
    beneficio_total = beneficio_por_accion * cantidad
    return beneficio_total

entrada = 100.0
salida = 110.0
acciones = 50
resultado = calcular_beneficio(entrada, salida, acciones)
print(f"Mi beneficio total es: ${resultado}")
print("\n")

# --- 4. Funciones con lógica condicional: Señal RSI ---
print("--- Función con lógica condicional (RSI) ---")
def senal_rsi(rsi_actual):
    if rsi_actual < 30:
        return "COMPRAR"
    elif rsi_actual > 70:
        return "VENDER"
    else:
        return "MANTENER"

print(f"RSI en 25: {senal_rsi(25)}")
print(f"RSI en 50: {senal_rsi(50)}")
print(f"RSI en 80: {senal_rsi(80)}")
