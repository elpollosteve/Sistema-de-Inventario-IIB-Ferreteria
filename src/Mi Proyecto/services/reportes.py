from typing import Dict, Any, Optional
from datetime import datetime
from models.producto import Producto
from repositories.inventario import Inventario


class GeneradorReportes:
    """Genera reportes del inventario."""

    def __init__(self, inventario: Inventario):
        self.inventario = inventario

    def valor_total_inventario(self) -> float:
        """Calcula el valor total de todo el inventario."""
        productos = self.inventario._repositorio.obtener_todos()
        return sum(p.calcular_valor_total() for p in productos)

    def cantidad_total_productos(self) -> int:
        """Cuenta cuántos productos diferentes hay."""
        return len(self.inventario._repositorio.obtener_todos())

    def total_items_stock(self) -> int:
        """Suma todos los items en stock."""
        productos = self.inventario._repositorio.obtener_todos()
        return sum(p.cantidad for p in productos)

    def producto_mas_caro(self) -> Optional[Producto]:
        """Encuentra el producto con mayor precio."""
        productos = self.inventario._repositorio.obtener_todos()
        return max(productos, key=lambda p: p.precio) if productos else None

    def producto_mas_barato(self) -> Optional[Producto]:
        """Encuentra el producto con menor precio."""
        productos = self.inventario._repositorio.obtener_todos()
        return min(productos, key=lambda p: p.precio) if productos else None

    def reporte_completo(self) -> Dict[str, Any]:
        """Genera un reporte completo con todas las estadísticas."""
        return {
            "fecha_generacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_productos": self.cantidad_total_productos(),
            "total_items": self.total_items_stock(),
            "valor_total": self.valor_total_inventario(),
            "producto_mas_caro": self.producto_mas_caro(),
            "producto_mas_barato": self.producto_mas_barato(),
            "productos_bajo_stock": self.inventario.obtener_productos_bajo_stock()
        }