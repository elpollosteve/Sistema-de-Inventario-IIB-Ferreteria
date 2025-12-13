"""
Paquete models - Modelos de Datos
==================================

Este paquete contiene las clases que representan las entidades principales
del sistema de gestión de ferretería.

Módulos:
--------
- producto.py: Define la clase Producto y el Enum Categoria.
               Representa los productos que se venden en la ferretería
               con sus atributos como nombre, precio, cantidad y categoría.

Clases principales:
-------------------
- Producto: Modelo de datos para un producto de ferretería
- Categoria: Enumeración de las categorías disponibles

Ejemplo de uso:
---------------
>>> from models.producto import Producto, Categoria
>>> producto = Producto("Martillo", "Herramienta", 25.50, 10, Categoria.HERRAMIENTAS)
"""