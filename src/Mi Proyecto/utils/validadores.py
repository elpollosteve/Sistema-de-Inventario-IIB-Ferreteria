class Validadores:
    """Valida datos de entrada del sistema."""

    @staticmethod
    def validar_nombre(nombre: str) -> bool:
        """Valida que el nombre no esté vacío."""
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        return True

    @staticmethod
    def validar_precio(precio: float) -> bool:
        """Valida que el precio sea positivo."""
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        return True

    @staticmethod
    def validar_cantidad(cantidad: int) -> bool:
        """Valida que la cantidad sea positiva."""
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        return True

    @staticmethod
    def validar_producto_completo(nombre: str, precio: float, cantidad: int) -> bool:
        """Valida todos los datos de un producto antes de crearlo."""
        Validadores.validar_nombre(nombre)
        Validadores.validar_precio(precio)
        Validadores.validar_cantidad(cantidad)
        return True

    @staticmethod
    def validar_id_positivo(id_producto: int) -> bool:
        """Valida que el ID sea un número positivo."""
        if id_producto <= 0:
            raise ValueError("El ID debe ser un número positivo")
        return True

    @staticmethod
    def validar_stock_suficiente(stock_actual: int, cantidad_requerida: int) -> bool:
        """Valida que haya suficiente stock para una operación."""
        if stock_actual < cantidad_requerida:
            raise ValueError(f"Stock insuficiente. Disponible: {stock_actual}")
        return True