# Deber 9 - MiniTienda

## Descripcion

MiniTienda es un programa desarrollado en Python para registrar y analizar ventas de productos.

El programa permite mostrar un catalogo, registrar ventas, controlar el stock, aplicar descuentos, guardar informacion en archivos CSV, calcular metricas y generar graficos de ingresos por producto.

## Librerias utilizadas

* pandas
* numpy
* matplotlib
* os

## Estructuras utilizadas

El programa utiliza diferentes estructuras de datos:

* Tuplas para almacenar el catalogo de productos.
* Diccionarios para almacenar los precios y el stock.
* Listas para almacenar temporalmente las ventas.

## Funciones

El programa fue dividido en funciones para organizar mejor el codigo. Entre las principales funciones se encuentran:

* Mostrar el catalogo.
* Registrar una venta.
* Guardar mensajes en log.txt.
* Crear el DataFrame.
* Leer ventas.csv.
* Exportar el grafico.
* Calcular valores controlando la division por cero.
* Ejecutar el menu principal.

## Validaciones

El programa valida diferentes situaciones para evitar errores durante su ejecucion:

* ID de producto inexistente.
* Cantidades menores o iguales a cero.
* Stock insuficiente.
* Entradas no numericas.
* Archivo ventas.csv inexistente.
* Division por cero.
* Opciones incorrectas en el menu.

Los intentos de venta con un ID de producto inexistente se registran en el archivo log.txt.

## Pandas

Pandas se utiliza para crear un DataFrame con las ventas registradas, realizar agrupaciones mediante groupby y guardar y leer informacion desde ventas.csv.

## NumPy

NumPy se utiliza para calcular:

* Promedio de ventas con np.mean().
* Desviacion estandar con np.std().
* Suma total de ventas con np.sum().

## Matplotlib

Matplotlib se utiliza para crear una grafica de barras que representa los ingresos obtenidos por cada producto.

La grafica tambien puede exportarse como ingresos.png.

## Descuento

Cuando un cliente compra 10 o mas unidades de un producto, el programa aplica un descuento del 5 por ciento sobre el subtotal de la venta.

## Menu

El programa cuenta con un menu que utiliza un ciclo while y estructuras de control como:

* if
* elif
* else
* for
* while
* break
* continue
* try
* except
* else
* finally

## Archivos generados

El programa genera los siguientes archivos:

* ventas.csv
* log.txt
* ingresos.png

## Ejecucion

El programa puede ejecutarse en Google Colab o Jupyter Notebook.

Se debe ejecutar el notebook desde la primera celda hasta la ultima para cargar las librerias, crear las estructuras de datos y habilitar todas las funciones del programa.

## Retos realizados

### Reto A

Se agrego el producto Webcam al catalogo junto con su precio y stock.

### Reto B

Se agrego la opcion para exportar la grafica de ingresos utilizando plt.savefig("ingresos.png").

### Reto C

Se implemento un descuento del 5 por ciento cuando se venden 10 o mas unidades.

### Reto D

Cuando se intenta registrar una venta utilizando un producto ID que no existe, el intento fallido se guarda en log.txt.
