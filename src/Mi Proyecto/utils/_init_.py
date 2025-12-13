"""
Paquete utils - Utilidades y Helpers
=====================================

Este paquete contiene clases y funciones utilitarias que proporcionan
funcionalidades auxiliares al sistema, como validación de datos y
formateo de salida para la interfaz de usuario.

Módulos:
--------
- formatters.py: Clase Formateadores con métodos estáticos para formatear
                 datos para visualización (tablas, precios, reportes).

- validadores.py: Clase Validadores con métodos estáticos para validar
                  datos de entrada (nombres, precios, cantidades, stock).

Clases principales:
-------------------
- Formateadores: Formatea datos para mostrar en consola (precios, tablas, reportes)
- Validadores: Valida datos de entrada del usuario

Ejemplo de uso:
---------------
>>> from utils.formatters import Formateadores
>>> from utils.validadores import Validadores
>>> 
>>> # Formatear precio
>>> precio_formateado = Formateadores.formatear_precio(25.50)
>>> print(precio_formateado)  # Output: S/.25.50
>>> 
>>> # Validar datos
>>> Validadores.validar_precio(25.50)  # Retorna True o lanza ValueError
"""