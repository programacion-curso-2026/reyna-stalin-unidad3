# Deber 8 - Mejora Analitica

## Descripcion

Este proyecto realiza el analisis de registros de mantenimiento de equipos de diferentes areas de una institucion.

El programa permite cargar archivos CSV, validar la informacion, detectar registros incorrectos, limpiar los datos, calcular indicadores y representar los resultados mediante graficos.

## Librerias utilizadas

* pandas
* numpy
* matplotlib

## Validaciones realizadas

El programa verifica:

* Codigos vacios.
* Codigos duplicados.
* Fechas invalidas.
* Costos no numericos o negativos.
* Duraciones no numericas o no positivas.
* Satisfaccion fuera del rango de 1 a 5.
* Estados no permitidos.
* Categorias de equipos no contempladas.

Los registros que presentan errores son identificados y excluidos para generar un DataFrame limpio.

## Analisis realizado

Con los datos validos se calcula:

* Numero de mantenimientos validos.
* Costo total.
* Costo promedio.
* Mantenimiento mas costoso.
* Cantidad de mantenimientos por area.
* Costo promedio por tipo de mantenimiento.

Tambien se utiliza NumPy para calcular la media y mediana de los costos y para clasificarlos en las categorias Bajo, Medio y Alto.

## Graficos

Se generan dos graficos con Matplotlib:

1. Costo total de mantenimientos por area.
2. Cantidad de mantenimientos por tipo.

## Pruebas realizadas

Se realizaron tres pruebas:

* Lectura y procesamiento de `mantenimientos.csv`.
* Lectura, validacion y limpieza de `mantenimientos_con_errores.csv`.
* Intento de lectura de un archivo inexistente para comprobar el manejo de excepciones.

## Archivos generados

El programa genera:

* `mantenimientos_limpios.csv`
* `resumen_por_area.csv`

## Ejecucion

El notebook puede ejecutarse en Google Colab o Jupyter Notebook. Los archivos CSV deben encontrarse en la misma ubicacion del notebook antes de ejecutar las celdas.
