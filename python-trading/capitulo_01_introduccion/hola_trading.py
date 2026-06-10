# Capitulo 1 - Primer ejemplo de trading
# Autor: Tu Libro de Python Trading
# Ejemplo basico de calculo de precios

print("=" * 50)
print("Bienvenido al trading algoritmico con Python!")
print("=" * 50)

# Variable con el precio de una accion
precio_accion = 150.25

# Calcular un 1% del precio
variacion_1_por_ciento = precio_accion * 0.01

# Mostrar resultados
print(f"\nPrecio actual de la accion: ${precio_accion}")
print(f"1% del precio: ${variacion_1_por_ciento:.2f}")
print(f"Si sube 1%, el nuevo precio seria: ${precio_accion + variacion_1_por_ciento:.2f}")
print(f"Si baja 1%, el nuevo precio seria: ${precio_accion - variacion_1_por_ciento:.2f}")

print("\n" + "=" * 50)
print("Exito en tu trading!")
