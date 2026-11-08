def leer_texto(mensaje, permitir_vacio=False):
    while True:
        valor = input(mensaje).strip()
        if valor or permitir_vacio:
            return valor
        print("Este campo no puede estar vacío.")


def leer_entero(mensaje, minimo=None, permitir_vacio=False, valor_actual=None):
    while True:
        dato = input(mensaje).strip()
        if permitir_vacio and dato == "":
            return valor_actual
        try:
            valor = int(dato)
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser como mínimo {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite un número entero.")


def leer_float(mensaje, minimo=None, permitir_vacio=False, valor_actual=None):
    while True:
        dato = input(mensaje).strip().replace(",", ".")
        if permitir_vacio and dato == "":
            return valor_actual
        try:
            valor = float(dato)
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser como mínimo {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite un número válido.")


def confirmar(mensaje):
    while True:
        respuesta = input(f"{mensaje} (s/n): ").strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta == "n":
            return False
        print("Responda s o n.")
