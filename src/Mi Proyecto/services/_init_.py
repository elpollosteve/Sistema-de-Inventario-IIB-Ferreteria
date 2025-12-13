"""
Paquete services - Servicios de Negocio
========================================

Este paquete contiene las clases que implementan la lógica de negocio
y servicios adicionales del sistema, como la generación de reportes
y análisis de datos del inventario.

Módulos:
--------
- reportes.py: Define la clase GeneradorReportes.
               Genera estadísticas y reportes completos del inventario,
               como valor total, productos más caros/baratos, stock bajo, etc.

Clases principales:
-------------------
- GeneradorReportes: Genera reportes y estadísticas del inventario

Ejemplo de uso:
---------------
>>> from services.reportes import GeneradorReportes
>>> generador = GeneradorReportes(inventario)
>>> reporte = generador.reporte_completo()
>>> print(reporte['valor_total'])
"""