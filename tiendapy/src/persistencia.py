from pathlib import Path
from datetime import date

RAIZ = Path(__file__).resolve().parent.parent
CARPETA_DATA = RAIZ / "data"
ARCHIVO_INVENTARIO = CARPETA_DATA / "inventario.txt"
ARCHIVO_VENTAS = CARPETA_DATA / "ventas.txt"


def preparar_archivos():
    CARPETA_DATA.mkdir(parents=True, exist_ok=True)
    for archivo in (ARCHIVO_INVENTARIO, ARCHIVO_VENTAS):
        archivo.touch(exist_ok=True)


def cargar_inventario():
    preparar_archivos()
    productos = {}
    try:
        with ARCHIVO_INVENTARIO.open("r", encoding="utf-8") as archivo:
            for numero, linea in enumerate(archivo, start=1):
                linea = linea.strip()
                if not linea:
                    continue
                try:
                    partes = linea.split("|")
                    if len(partes) != 7:
                        raise ValueError("cantidad de campos incorrecta")
                    codigo, nombre, categoria, precio, stock, minimo, proveedor = partes
                    producto = {
                        "codigo": codigo,
                        "nombre": nombre,
                        "categoria": categoria,
                        "precio": float(precio),
                        "stock": int(stock),
                        "stock_minimo": int(minimo),
                        "proveedor": proveedor,
                    }
                    if not codigo or producto["precio"] <= 0 or producto["stock"] < 0 or producto["stock_minimo"] < 0:
                        raise ValueError("datos fuera de rango")
                    if codigo in productos:
                        raise ValueError("código duplicado")
                    productos[codigo] = producto
                except (ValueError, TypeError) as error:
                    print(f"Advertencia: se omitió la línea {numero} del inventario: {error}.")
    except OSError as error:
        print(f"No fue posible leer el inventario: {error}")
    return productos


def guardar_inventario(productos):
    preparar_archivos()
    with ARCHIVO_INVENTARIO.open("w", encoding="utf-8") as archivo:
        for p in productos.values():
            campos = [
                p["codigo"], p["nombre"], p["categoria"],
                str(p["precio"]), str(p["stock"]),
                str(p["stock_minimo"]), p["proveedor"]
            ]
            archivo.write("|".join(campos) + "\n")


def registrar_venta(venta):
    preparar_archivos()
    detalle = ";".join(f'{codigo}:{cantidad}' for codigo, cantidad in venta["items"].items())
    with ARCHIVO_VENTAS.open("a", encoding="utf-8") as archivo:
        archivo.write(f'{venta["fecha"]}|{venta["total"]}|{detalle}\n')


def cargar_ventas():
    preparar_archivos()
    ventas = []
    try:
        with ARCHIVO_VENTAS.open("r", encoding="utf-8") as archivo:
            for numero, linea in enumerate(archivo, start=1):
                linea = linea.strip()
                if not linea:
                    continue
                try:
                    fecha, total, detalle = linea.split("|")
                    items = {}
                    if detalle:
                        for elemento in detalle.split(";"):
                            codigo, cantidad = elemento.split(":")
                            items[codigo] = int(cantidad)
                    ventas.append({
                        "fecha": fecha,
                        "total": float(total),
                        "items": items,
                    })
                except (ValueError, TypeError):
                    print(f"Advertencia: se omitió la línea {numero} del historial de ventas.")
    except OSError as error:
        print(f"No fue posible leer el historial: {error}")
    return ventas


def fecha_hoy():
    return date.today().isoformat()
