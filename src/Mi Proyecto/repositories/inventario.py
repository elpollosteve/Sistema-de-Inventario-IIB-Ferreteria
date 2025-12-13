from typing import Dict, List, Optional
from models.producto import Producto, Categoria
from utils.validadores import Validadores


class RepositorioMemoria:
    """Almacena productos en memoria."""

    def __init__(self):
        self._productos: Dict[int, Producto] = {}

    def agregar(self, producto: Producto) -> bool:
        if producto.id_producto in self._productos:
            raise ValueError(f"El producto con ID {producto.id_producto} ya existe")
        self._productos[producto.id_producto] = producto
        return True

    def obtener(self, id_producto: int) -> Optional[Producto]:
        return self._productos.get(id_producto)

    def obtener_todos(self) -> List[Producto]:
        return list(self._productos.values())

    def eliminar(self, id_producto: int) -> bool:
        if id_producto in self._productos:
            del self._productos[id_producto]
            return True
        return False

    def obtener_por_categoria(self, categoria: Categoria) -> List[Producto]:
        return [p for p in self._productos.values() if p.categoria == categoria]


class Inventario:
    """Gestiona el inventario de la ferretería."""

    def __init__(self, repositorio: RepositorioMemoria):
        self._repositorio = repositorio

    def agregar_producto(self, nombre: str, descripcion: str, precio: float,
                         cantidad: int, categoria: Categoria) -> Producto:
        # Validar datos antes de crear el producto
        Validadores.validar_producto_completo(nombre, precio, cantidad)
        
        producto = Producto(nombre, descripcion, precio, cantidad, categoria)
        self._repositorio.agregar(producto)
        return producto

    def aumentar_stock(self, id_producto: int, cantidad: int) -> bool:
        Validadores.validar_cantidad(cantidad)
        
        producto = self._repositorio.obtener(id_producto)
        if not producto:
            raise ValueError(f"Producto con ID {id_producto} no existe")
        
        producto.actualizar_cantidad(producto.cantidad + cantidad)
        return True

    def disminuir_stock(self, id_producto: int, cantidad: int) -> bool:
        Validadores.validar_cantidad(cantidad)
        
        producto = self._repositorio.obtener(id_producto)
        if not producto:
            raise ValueError(f"Producto con ID {id_producto} no existe")
        
        # Validar que hay suficiente stock
        Validadores.validar_stock_suficiente(producto.cantidad, cantidad)
        
        producto.actualizar_cantidad(producto.cantidad - cantidad)
        return True

    def obtener_productos_bajo_stock(self, limite: int = 10) -> List[Producto]:
        return [p for p in self._repositorio.obtener_todos() if p.cantidad <= limite]