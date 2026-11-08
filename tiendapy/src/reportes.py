from collections import defaultdict
from persistencia import cargar_ventas, fecha_hoy


def reporte_alertas(productos):
    grupos = defaultdict(list)
    for p in productos.values():
        if p["stock"] <= p["stock_minimo"]:
            grupos[p["proveedor"]].append(p)
    if not grupos:
        print("No hay productos que requieran reabastecimiento.")
        return
    print("\n--- ALERTAS DE STOCK POR PROVEEDOR ---")
    for proveedor, lista in sorted(grupos.items()):
        print(f"\nProveedor: {proveedor}")
        for p in lista:
            estado = "AGOTADO" if p["stock"] == 0 else "Stock bajo"
            print(f'  {p["codigo"]} - {p["nombre"]}: {p["stock"]} unidades '
                  f'(mínimo {p["stock_minimo"]}) [{estado}]')


def cierre_dia(productos):
    ventas = [v for v in cargar_ventas() if v["fecha"] == fecha_hoy()]
    print(f"\n--- CIERRE DEL DÍA: {fecha_hoy()} ---")
    total = sum(v["total"] for v in ventas)
    cantidad_ventas = len(ventas)
    promedio = total / cantidad_ventas if cantidad_ventas else 0
    unidades = defaultdict(int)
    for venta in ventas:
        for codigo, cantidad in venta["items"].items():
            unidades[codigo] += cantidad

    print(f"Total vendido: ${total:,.2f}")
    print(f"Número de transacciones: {cantidad_ventas}")
    print(f"Ticket promedio: ${promedio:,.2f}")

    if unidades:
        codigo_top = max(unidades, key=unidades.get)
        nombre = productos.get(codigo_top, {}).get("nombre", codigo_top)
        print(f"Producto más vendido: {nombre} ({unidades[codigo_top]} unidades)")
    else:
        print("Producto más vendido: No hay ventas.")

    sin_ventas = [p["nombre"] for c, p in productos.items() if unidades.get(c, 0) == 0]
    print("Productos sin ventas: " + (", ".join(sin_ventas) if sin_ventas else "Ninguno"))

    categorias = defaultdict(int)
    for codigo, cantidad in unidades.items():
        if codigo in productos:
            categorias[productos[codigo]["categoria"]] += cantidad
    print("Categorías con movimiento:")
    if categorias:
        for categoria, cantidad in sorted(categorias.items()):
            print(f"  {categoria}: {cantidad} unidades")
    else:
        print("  Sin movimiento.")
