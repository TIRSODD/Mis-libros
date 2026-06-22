# Capítulo 8 - Diario de Trading y Análisis de Rendimiento
# Autor: Tu Libro de Python Trading

import pandas as pd
from datetime import datetime

class DiarioTrading:
    """Registra y analiza todas las operaciones del bot."""
    
    def __init__(self):
        self.operaciones = []
    
    def registrar_operacion(self, simbolo, tipo, precio_entrada, precio_salida, 
                           cantidad, fecha_entrada, fecha_salida=None):
        """Registra una operación completa."""
        if tipo == 'COMPRA':
            beneficio = (precio_salida - precio_entrada) * cantidad
        else:  # VENTA en corto
            beneficio = (precio_entrada - precio_salida) * cantidad
        
        operacion = {
            'simbolo': simbolo,
            'tipo': tipo,
            'precio_entrada': precio_entrada,
            'precio_salida': precio_salida,
            'cantidad': cantidad,
            'beneficio': beneficio,
            'fecha_entrada': fecha_entrada,
            'fecha_salida': fecha_salida or datetime.now(),
            'resultado': 'GANANCIA' if beneficio > 0 else 'PÉRDIDA'
        }
        
        self.operaciones.append(operacion)
        return operacion
    
    def resumen_estadisticas(self):
        """Genera un resumen estadístico del diario."""
        if not self.operaciones:
            print("No hay operaciones registradas.")
            return
        
        df = pd.DataFrame(self.operaciones)
        
        total_operaciones = len(df)
        ganadoras = len(df[df['resultado'] == 'GANANCIA'])
        perdedoras = total_operaciones - ganadoras
        win_rate = (ganadoras / total_operaciones) * 100
        
        beneficio_total = df['beneficio'].sum()
        beneficio_medio = df['beneficio'].mean()
        ganancia_media = df[df['resultado'] == 'GANANCIA']['beneficio'].mean()
        perdida_media = df[df['resultado'] == 'PÉRDIDA']['beneficio'].mean()
        
        # Racha perdedora máxima
        racha_max = 0
        racha_actual = 0
        for _, row in df.iterrows():
            if row['resultado'] == 'PÉRDIDA':
                racha_actual += 1
                racha_max = max(racha_max, racha_actual)
            else:
                racha_actual = 0
        
        print("\n" + "=" * 50)
        print("RESUMEN DEL DIARIO DE TRADING")
        print("=" * 50)
        print(f"Total de operaciones: {total_operaciones}")
        print(f"Ganadoras: {ganadoras} ({win_rate:.1f}%)")
        print(f"Perdedoras: {perdedoras} ({100-win_rate:.1f}%)")
        print(f"Beneficio total: ${beneficio_total:,.2f}")
        print(f"Beneficio medio por operación: ${beneficio_medio:,.2f}")
        print(f"Ganancia media en ganadoras: ${ganancia_media:,.2f}")
        print(f"Pérdida media en perdedoras: ${perdida_media:,.2f}")
        print(f"Ratio ganancia/pérdida: {abs(ganancia_media/perdida_media):.2f}")
        print(f"Racha perdedora máxima: {racha_max} operaciones consecutivas")
        print("=" * 50)
    
    def exportar_csv(self, nombre_archivo='diario_trading.csv'):
        """Exporta el diario a un archivo CSV."""
        df = pd.DataFrame(self.operaciones)
        df.to_csv(nombre_archivo, index=False)
        print(f"Diario exportado a {nombre_archivo}")

# Ejemplo de uso
diario = DiarioTrading()

# Simulamos algunas operaciones
diario.registrar_operacion('AAPL', 'COMPRA', 150.0, 155.0, 10, 
                          datetime(2024, 1, 1), datetime(2024, 1, 5))
diario.registrar_operacion('MSFT', 'COMPRA', 300.0, 295.0, 5, 
                          datetime(2024, 1, 6), datetime(2024, 1, 10))
diario.registrar_operacion('GOOGL', 'COMPRA', 140.0, 148.0, 8, 
                          datetime(2024, 1, 11), datetime(2024, 1, 15))
diario.registrar_operacion('AMZN', 'COMPRA', 180.0, 175.0, 6, 
                          datetime(2024, 1, 16), datetime(2024, 1, 20))
diario.registrar_operacion('TSLA', 'COMPRA', 250.0, 260.0, 4, 
                          datetime(2024, 1, 21), datetime(2024, 1, 25))

# Mostramos el resumen
diario.resumen_estadisticas()

# Exportamos a CSV
diario.exportar_csv()
