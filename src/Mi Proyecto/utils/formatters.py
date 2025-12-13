from typing import List, Dict, Any
from models.producto import Producto


class Formateadores:
    """Formatea datos para visualización."""

    @staticmethod
    def formatear_precio(precio: float) -> str:
        """Formatea un precio con el símbolo de soles."""
        return f"S/.{precio:.2f}"

    @staticmethod
    def formatear_producto_tabla(producto: Producto) -> str:
        """Formatea un producto en formato de tabla."""
        return f"| {producto.id_producto:>6} | {producto.nombre:<35} | {Formateadores.formatear_precio(producto.precio):>10} | {producto.cantidad:>6} |"

    @staticmethod
    def formatear_lista_productos(productos: List[Producto]) -> str:
        """Formatea una lista de productos en tabla."""
        if not productos:
            return "No hay productos para mostrar"

        encabezado = "| ID     | Nombre                              | Precio     | Stock  |"
        separador = "-" * 70
        filas = [Formateadores.formatear_producto_tabla(p) for p in productos]
        return f"\n{encabezado}\n{separador}\n" + "\n".join(filas) + f"\n{separador}"

    @staticmethod
    def formatear_reporte(reporte: Dict[str, Any]) -> str:
        """Formatea un reporte completo para mostrar en pantalla."""
        output = "\n" + "=" * 70 + "\n"
        output += "           REPORTE DE INVENTARIO - FERRETERÍA\n"
        output += "=" * 70 + "\n"
        output += f"Fecha: {reporte['fecha_generacion']}\n"
        output += f"Total de Productos Diferentes: {reporte['total_productos']}\n"
        output += f"Total Ítems en Stock: {reporte['total_items']}\n"
        output += f"Valor Total del Inventario: {Formateadores.formatear_precio(reporte['valor_total'])}\n\n"

        if reporte['producto_mas_caro']:
            output += f"Producto Más Caro: {reporte['producto_mas_caro'].nombre} - {Formateadores.formatear_precio(reporte['producto_mas_caro'].precio)}\n"
        if reporte['producto_mas_barato']:
            output += f"Producto Más Barato: {reporte['producto_mas_barato'].nombre} - {Formateadores.formatear_precio(reporte['producto_mas_barato'].precio)}\n"

        output += "\n⚠️  Productos con Bajo Stock: (Límite: 10 unidades)\n"
        output += "-" * 70 + "\n"
        if reporte['productos_bajo_stock']:
            for p in reporte['productos_bajo_stock']:
                output += f"  • {p.nombre} - Stock actual: {p.cantidad} unidades\n"
        else:
            output += "  ✓ Todos los productos tienen stock suficiente.\n"
        output += "=" * 70 + "\n"
        return output