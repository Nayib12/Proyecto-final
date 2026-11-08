# TiendaPy

Aplicación de consola en Python para administrar el inventario y las ventas de la tienda Don Aurelio.

## Requisitos
- Python 3.10 o superior.
- No requiere instalar dependencias para funcionar.

## Ejecución
Desde la carpeta raíz del proyecto:

```bash
python src/main.py
```

## Módulos
- `main.py`: menú principal.
- `inventario.py`: registro, consulta, modificación y eliminación.
- `ventas.py`: carrito, descuentos, pago y cambio.
- `reportes.py`: alertas y cierre diario.
- `persistencia.py`: lectura y escritura de archivos de texto.
- `validaciones.py`: validación de entradas.

## Persistencia
El inventario se guarda en `data/inventario.txt` y las ventas en `data/ventas.txt`.
Los archivos utilizan el formato definido en el enunciado.

## Reglas de descuentos
- Subtotal desde $50.000 y menor que $100.000: 5 %.
- Subtotal desde $100.000: 10 %.

## Entorno virtual (opcional)
```bash
python -m venv venv
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Linux/macOS:
source venv/bin/activate
```

## Pruebas manuales recomendadas
1. Registrar un producto y comprobar que queda en `inventario.txt`.
2. Intentar registrar el mismo código.
3. Hacer una venta con varios productos.
4. Probar subtotales inferiores a $50.000, desde $50.000 y desde $100.000.
5. Intentar vender más unidades de las disponibles.
6. Introducir letras en campos numéricos.
7. Cerrar y abrir de nuevo para comprobar la persistencia.
