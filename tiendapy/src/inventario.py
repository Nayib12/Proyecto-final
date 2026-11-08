from validaciones import leer_texto, leer_entero, leer_float, confirmar
from persistencia import guardar_inventario


def registrar_producto(productos):
    print("\n--- Registrar producto ---")
    codigo = leer_texto("Código: ").upper()
    if codigo in productos:
        raise ValueError("Ya existe un producto con ese código.")
    nombre = leer_texto("Nombre: ")
    categoria = leer_texto("Categoría: ")
    precio = leer_float("Precio de venta (COP): ", minimo=0.01)
    stock = leer_entero("Stock inicial: ", minimo=0)
    minimo = leer_entero("Stock mínimo: ", minimo=0)
    proveedor = leer_texto("Proveedor: ")
    productos[codigo] = {
        "codigo": codigo, "nombre": nombre, "categoria": categoria,
        "precio": precio, "stock": stock,
        "stock_minimo": minimo, "proveedor": proveedor
    }
    guardar_inventario(productos)
    print("Producto registrado correctamente.")


def mostrar_productos(lista):
    if not lista:
        print("No se encontraron productos.")
        return
    print("-" * 105)
    print(f'{"CÓDIGO":<10} {"NOMBRE":<24} {"CATEGORÍA":<15} {"PRECIO":>12} {"STOCK":>8} {"MÍNIMO":>8}  PROVEEDOR')
    print("-" * 105)
    for p in lista:
        print(f'{p["codigo"]:<10} {p["nombre"][:23]:<24} {p["categoria"][:14]:<15} '
              f'{p["precio"]:>12,.2f} {p["stock"]:>8} {p["stock_minimo"]:>8}  {p["proveedor"]}')
    print("-" * 105)


def consultar_producto(productos):
    print("\n1. Buscar por código\n2. Buscar por categoría\n3. Mostrar todos")
    opcion = input("Opción: ").strip()
    if opcion == "1":
        codigo = leer_texto("Código: ").upper()
        producto = productos.get(codigo)
        mostrar_productos([producto] if producto else [])
    elif opcion == "2":
        categoria = leer_texto("Categoría: ").casefold()
        encontrados = [p for p in productos.values() if p["categoria"].casefold() == categoria]
        mostrar_productos(encontrados)
    elif opcion == "3":
        mostrar_productos(list(productos.values()))
    else:
        print("Opción inválida.")


def modificar_producto(productos):
    codigo = leer_texto("Código del producto: ").upper()
    if codigo not in productos:
        print("No existe un producto con ese código.")
        return
    p = productos[codigo]
    print("Deje el campo vacío para conservar el valor actual.")
    p["precio"] = leer_float(f'Nuevo precio [{p["precio"]}]: ', minimo=0.01,
                             permitir_vacio=True, valor_actual=p["precio"])
    p["stock"] = leer_entero(f'Nuevo stock [{p["stock"]}]: ', minimo=0,
                             permitir_vacio=True, valor_actual=p["stock"])
    guardar_inventario(productos)
    print("Producto actualizado.")


def eliminar_producto(productos):
    codigo = leer_texto("Código del producto que desea eliminar: ").upper()
    if codigo not in productos:
        print("No existe un producto con ese código.")
        return
    if confirmar(f'¿Eliminar {productos[codigo]["nombre"]}?'):
        del productos[codigo]
        guardar_inventario(productos)
        print("Producto eliminado.")


def menu_inventario(productos):
    while True:
        print("\n--- GESTIÓN DE INVENTARIO ---")
        print("1. Registrar producto\n2. Consultar/buscar\n3. Modificar precio y stock")
        print("4. Eliminar producto\n5. Volver")
        opcion = input("Seleccione: ").strip()
        try:
            if opcion == "1":
                registrar_producto(productos)
            elif opcion == "2":
                consultar_producto(productos)
            elif opcion == "3":
                modificar_producto(productos)
            elif opcion == "4":
                eliminar_producto(productos)
            elif opcion == "5":
                return
            else:
                print("Opción inválida.")
        except ValueError as error:
            print(f"Error: {error}")
