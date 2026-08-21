import pandas as pd

# Crear los datos
datos = {
    "Producto": ["Laptop", "Mouse", "Teclado", "Monitor"],
    "Cantidad": [2, 5, 3, 1],
    "Precio": [700, 15, 30, 200]
}

# Crear la tabla
ventas = pd.DataFrame(datos)

# Calcular el total de cada producto
ventas["Total"] = ventas["Cantidad"] * ventas["Precio"]

# Mostrar la tabla
print("ANÁLISIS DE VENTAS")
print(ventas)

# Calcular las ventas totales
total = ventas["Total"].sum()

print("\nTotal de ventas: $", total)