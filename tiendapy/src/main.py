from persistencia import cargar_inventario, guardar_inventario, preparar_archivos
from inventario import menu_inventario
from ventas import procesar_venta
from reportes import reporte_alertas, cierre_dia


def menu_principal():
    preparar_archivos()
    productos = cargar_inventario()
    print("=" * 48)
    print("             TIENDAPY - DON AURELIO")
    print("=" * 48)

    while True:
        print("\nMENÚ PRINCIPAL")
        print("1. Gestión de inventario")
        print("2. Registrar venta")
        print("3. Alertas de stock")
        print("4. Cierre y reportes del día")
        print("5. Guardar inventario")
        print("0. Guardar y salir")
        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                menu_inventario(productos)
            elif opcion == "2":
                procesar_venta(productos)
            elif opcion == "3":
                reporte_alertas(productos)
            elif opcion == "4":
                cierre_dia(productos)
            elif opcion == "5":
                guardar_inventario(productos)
                print("Inventario guardado.")
            elif opcion == "0":
                guardar_inventario(productos)
                print("Información guardada. Hasta pronto.")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except (ValueError, OSError) as error:
            print(f"No se pudo completar la operación: {error}")


if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
