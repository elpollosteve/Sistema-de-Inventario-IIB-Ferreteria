from enum import Enum
from datetime import datetime


class Categoria(Enum):
    """Categorías de productos de ferretería."""
    HERRAMIENTAS = "Herramientas"
    MATERIALES = "Materiales de Construcción"
    PINTURA = "Pintura y Accesorios"
    ELECTRICIDAD = "Electricidad"
    PLOMERIA = "Plomería"
    OTROS = "Otros"


class Producto:
    """Representa un producto en la ferretería."""
    _contador = 1000

    def __init__(self, nombre: str, descripcion: str, precio: float,
                 cantidad: int, categoria: Categoria):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")

        Producto._contador += 1
        self.id_producto = Producto._contador
        self.nombre = nombre.strip()
        self.descripcion = descripcion.strip()
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria
        self.fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def actualizar_cantidad(self, cantidad: int) -> bool:
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.cantidad = cantidad
        return True

    def actualizar_precio(self, precio: float) -> bool:
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.precio = precio
        return True

    def calcular_valor_total(self) -> float:
        return self.precio * self.cantidad

    def __str__(self) -> str:
        return f"{self.id_producto} | {self.nombre} | S/.{self.precio} | Stock: {self.cantidad}"