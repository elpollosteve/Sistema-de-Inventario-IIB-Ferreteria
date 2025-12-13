from models.producto import Producto, Categoria
from repositories.inventario import RepositorioMemoria, Inventario
from services.reportes import GeneradorReportes
from utils.formatters import Formateadores


def mostrar_menu():
    """Muestra el menú principal."""
    print("\n" + "=" * 70)
    print("        SISTEMA DE GESTIÓN DE FERRETERÍA")
    print("=" * 70)
    print("1. Agregar nuevo producto")
    print("2. Ver todos los productos")
    print("3. Buscar producto por ID")
    print("4. Registrar venta (disminuir stock)")
    print("5. Agregar stock a producto")
    print("6. Ver productos por categoría")
    print("7. Generar reporte completo")
    print("8. Eliminar producto")
    print("0. Salir")
    print("=" * 70)


def agregar_producto_menu(inventario: Inventario):
    """Menú para agregar un producto."""
    print("\n--- AGREGAR NUEVO PRODUCTO ---")
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción: ")
    precio = float(input("Precio (S/.): "))
    cantidad = int(input("Cantidad inicial: "))
    
    print("\nCategorías disponibles:")
    for i, cat in enumerate(Categoria, 1):
        print(f"{i}. {cat.value}")
    
    opcion_cat = int(input("Seleccione categoría (número): "))
    categoria = list(Categoria)[opcion_cat - 1]
    
    try:
        producto = inventario.agregar_producto(nombre, descripcion, precio, cantidad, categoria)
        print(f"\n✓ Producto agregado exitosamente con ID: {producto.id_producto}")
    except ValueError as e:
        print(f"\n✗ Error: {e}")


def registrar_venta(inventario: Inventario):
    """Registra una venta (disminuye stock)."""
    print("\n--- REGISTRAR VENTA ---")
    id_producto = int(input("ID del producto: "))
    cantidad = int(input("Cantidad vendida: "))
    
    try:
        inventario.disminuir_stock(id_producto, cantidad)
        print(f"\n✓ Venta registrada exitosamente. Stock actualizado.")
    except ValueError as e:
        print(f"\n✗ Error: {e}")


def agregar_stock(inventario: Inventario):
    """Agrega stock a un producto."""
    print("\n--- AGREGAR STOCK ---")
    id_producto = int(input("ID del producto: "))
    cantidad = int(input("Cantidad a agregar: "))
    
    try:
        inventario.aumentar_stock(id_producto, cantidad)
        print(f"\n✓ Stock agregado exitosamente.")
    except ValueError as e:
        print(f"\n✗ Error: {e}")


def ver_por_categoria(inventario: Inventario):
    """Muestra productos por categoría."""
    print("\n--- PRODUCTOS POR CATEGORÍA ---")
    print("\nCategorías disponibles:")
    for i, cat in enumerate(Categoria, 1):
        print(f"{i}. {cat.value}")
    
    opcion_cat = int(input("\nSeleccione categoría (número): "))
    categoria = list(Categoria)[opcion_cat - 1]
    
    productos = inventario._repositorio.obtener_por_categoria(categoria)
    print(f"\n{categoria.value}:")
    print(Formateadores.formatear_lista_productos(productos))


def cargar_datos_ejemplo(inventario: Inventario):
    """Carga datos de ejemplo para probar el sistema."""
    productos_ejemplo = [
        ("Martillo 16oz", "Martillo de acero forjado", 25.50, 45, Categoria.HERRAMIENTAS),
        ("Destornillador Phillips", "Set de 6 destornilladores", 18.90, 30, Categoria.HERRAMIENTAS),
        ("Cemento Portland", "Bolsa 42.5kg", 22.00, 8, Categoria.MATERIALES),
        ("Pintura Látex Blanco", "Galón", 45.00, 15, Categoria.PINTURA),
        ("Cable eléctrico 2.5mm", "Rollo 100m", 89.00, 5, Categoria.ELECTRICIDAD),
        ("Tubo PVC 1/2", "6 metros", 12.50, 25, Categoria.PLOMERIA),
        ("Lija para madera", "Pack x10 hojas", 8.50, 50, Categoria.HERRAMIENTAS),
        ("Brocha 3 pulgadas", "Cerdas sintéticas", 15.00, 20, Categoria.PINTURA),
        ("Cinta aislante", "Rollo 18m", 4.50, 60, Categoria.ELECTRICIDAD),
        ("Codo PVC 90° 1/2", "Accesorio", 1.80, 100, Categoria.PLOMERIA),
    ]
    
    for nombre, desc, precio, cant, cat in productos_ejemplo:
        inventario.agregar_producto(nombre, desc, precio, cant, cat)
    
    print("\n✓ Se cargaron 10 productos de ejemplo en el sistema.")


def main():
    """Función principal del programa."""
    # Inicializar sistema
    repositorio = RepositorioMemoria()
    inventario = Inventario(repositorio)
    generador_reportes = GeneradorReportes(inventario)
    
    # Cargar datos de ejemplo
    print("\n¡Bienvenido al Sistema de Ferretería!")
    cargar_datos_ejemplo(inventario)
    
    # Bucle principal
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            agregar_producto_menu(inventario)
        
        elif opcion == "2":
            productos = inventario._repositorio.obtener_todos()
            print("\n--- TODOS LOS PRODUCTOS ---")
            print(Formateadores.formatear_lista_productos(productos))
        
        elif opcion == "3":
            id_prod = int(input("\nID del producto: "))
            producto = inventario._repositorio.obtener(id_prod)
            if producto:
                print(f"\n{producto}")
                print(f"Descripción: {producto.descripcion}")
                print(f"Categoría: {producto.categoria.value}")
                print(f"Valor Total: S/.{producto.calcular_valor_total():.2f}")
            else:
                print("\n✗ Producto no encontrado.")
        
        elif opcion == "4":
            registrar_venta(inventario)
        
        elif opcion == "5":
            agregar_stock(inventario)
        
        elif opcion == "6":
            ver_por_categoria(inventario)
        
        elif opcion == "7":
            reporte = generador_reportes.reporte_completo()
            print(Formateadores.formatear_reporte(reporte))
        
        elif opcion == "8":
            id_prod = int(input("\nID del producto a eliminar: "))
            if inventario._repositorio.eliminar(id_prod):
                print("\n✓ Producto eliminado exitosamente.")
            else:
                print("\n✗ Producto no encontrado.")
        
        elif opcion == "0":
            print("\n¡Gracias por usar el Sistema de Ferretería!")
            print("¡Hasta pronto!\n")
            break
        
        else:
            print("\n✗ Opción inválida. Intente nuevamente.")
        
        input("\nPresione ENTER para continuar...")


# Ejecutar programa
if __name__ == "__main__":
    main()