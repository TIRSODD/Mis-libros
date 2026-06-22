# Capítulo 8 - Gestor de Riesgo a nivel de Cartera
# Autor: Tu Libro de Python Trading

print("--- GESTOR DE RIESGO DE CARTERA ---\n")

class GestorRiesgoCartera:
    """
    Gestiona el riesgo a nivel de cartera completa.
    Controla que no excedamos los límites de riesgo por operación
    ni el riesgo total de toda la cartera.
    """
    
    def __init__(self, capital_total, riesgo_max_operacion=0.01, riesgo_max_cartera=0.05):
        self.capital_total = capital_total
        self.riesgo_max_operacion = riesgo_max_operacion  # 1% por defecto
        self.riesgo_max_cartera = riesgo_max_cartera      # 5% por defecto
        self.operaciones_abiertas = []
    
    def riesgo_actual_cartera(self):
        """Calcula el riesgo total actualmente asumido."""
        riesgo_total = sum(op['riesgo_euros'] for op in self.operaciones_abiertas)
        return riesgo_total
    
    def puede_abrir_operacion(self, riesgo_nueva_operacion):
        """Verifica si podemos abrir una nueva operación sin exceder límites."""
        riesgo_actual = self.riesgo_actual_cartera()
        riesgo_max_euros = self.capital_total * self.riesgo_max_cartera
        riesgo_max_operacion_euros = self.capital_total * self.riesgo_max_operacion
        
        # Verificamos límite por operación
        if riesgo_nueva_operacion > riesgo_max_operacion_euros:
            return False, "Riesgo por operación excede el 1%"
        
        # Verificamos límite de cartera
        if riesgo_actual + riesgo_nueva_operacion > riesgo_max_euros:
            return False, "Riesgo total de cartera excede el 5%"
        
        return True, "Operación permitida"
    
    def registrar_operacion(self, simbolo, riesgo_euros):
        """Registra una nueva operación abierta."""
        self.operaciones_abiertas.append({
            'simbolo': simbolo,
            'riesgo_euros': riesgo_euros
        })
    
    def cerrar_operacion(self, simbolo):
        """Elimina una operación de la lista."""
        self.operaciones_abiertas = [op for op in self.operaciones_abiertas if op['simbolo'] != simbolo]
    
    def estado_cartera(self):
        """Muestra el estado actual de riesgo."""
        riesgo_actual = self.riesgo_actual_cartera()
        riesgo_max = self.capital_total * self.riesgo_max_cartera
        porcentaje_usado = (riesgo_actual / riesgo_max) * 100
        
        print(f"\n=== ESTADO DE RIESGO DE CARTERA ===")
        print(f"Capital total: ${self.capital_total:,.2f}")
        print(f"Riesgo actual asumido: ${riesgo_actual:,.2f}")
        print(f"Riesgo máximo permitido: ${riesgo_max:,.2f}")
        print(f"Porcentaje usado: {porcentaje_usado:.1f}%")
        print(f"Operaciones abiertas: {len(self.operaciones_abiertas)}")
        print("=" * 40)

# Ejemplo de uso
gestor = GestorRiesgoCartera(capital_total=10000)

# Intentamos abrir 5 operaciones
operaciones = [
    ('AAPL', 100),   # 1% de riesgo
    ('MSFT', 100),   # 1% de riesgo
    ('GOOGL', 100),  # 1% de riesgo
    ('AMZN', 100),   # 1% de riesgo
    ('TSLA', 100),   # 1% de riesgo (Esta debería ser rechazada por exceder el 5% total)
]

for simbolo, riesgo in operaciones:
    permitido, mensaje = gestor.puede_abrir_operacion(riesgo)
    
    if permitido:
        gestor.registrar_operacion(simbolo, riesgo)
        print(f"✅ {simbolo}: {mensaje}")
    else:
        print(f"❌ {simbolo}: {mensaje}")
    
    gestor.estado_cartera()
