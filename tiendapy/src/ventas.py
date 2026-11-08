from persistencia import guardar_inventario, registrar_venta, fecha_hoy
from validaciones import leer_texto, leer_entero, leer_float


def calcular_descuento(subtotal):
    if subtotal >= 100000:
        return 0.10
    if subtotal >= 50000:
        return 0.05
    return 0.0


def procesar_venta(productos):
    if not productos:
        print("No hay productos registrados.")
        return

    carrito = {}
    print("\n--- NUEVA VENTA ---")
    print("Ingrese el código del producto. Pulse Enter sin escribir código para terminar.")
    while True:
        codigo = input("Código: ").strip().upper()
        if not codigo:
            break
        if codigo not in productos:
            print("Producto no encontrado.")
            continue
        p = productos[codigo]
        disponible = p["stock"] - carrito.get(codigo, 0)
        if disponible <= 0:
            print("No hay unidades disponibles para agregar.")
            continue
        cantidad = leer_entero(f'Cantidad de {p["nombre"]} (disponibles: {disponible}): ', minimo=1)
        if cantidad > disponible:
            print("Cantidad superior al stock disponible. No se agregó.")
            continue
        carrito[codigo] = carrito.get(codigo, 0) + cantidad

    if not carrito:
        print("Venta cancelada: el carrito está vacío.")
        return

    subtotal = sum(productos[c]["precio"] * cantidad for c, cantidad in carrito.items())
    descuento_pct = calcular_descuento(subtotal)
    descuento = subtotal * descuento_pct
    total = subtotal - descuento

    print("\n--- RESUMEN DE VENTA ---")
    for codigo, cantidad in carrito.items():
        p = productos[codigo]
        valor = p["precio"] * cantidad
        print(f'{p["nombre"]} x {cantidad} = ${valor:,.2f}')
    print(f"Subtotal: ${subtotal:,.2f}")
    print(f"Descuento ({descuento_pct * 100:.0f}%): ${descuento:,.2f}")
    print(f"TOTAL: ${total:,.2f}")

    while True:
        pago = leer_float("Pago recibido (COP): ", minimo=0.01)
        if pago < total:
            print(f"Pago insuficiente. Faltan ${total - pago:,.2f}. Intente nuevamente.")
        else:
            break

    cambio = pago - total
    # El stock solo se modifica cuando la venta está completamente confirmada.
    for codigo, cantidad in carrito.items():
        productos[codigo]["stock"] -= cantidad
    guardar_inventario(productos)

    venta = {"fecha": fecha_hoy(), "total": total, "items": carrito}
    registrar_venta(venta)
    print(f"Venta registrada. Cambio: ${cambio:,.2f}")
