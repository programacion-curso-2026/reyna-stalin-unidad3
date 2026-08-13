import pandas as pd 
# Datos de los estudiantes
datos = {
    "Estudiante": ["Ana", "Luis", "Carlos", "Maria", "Pedro"],
    "Nota": [9.2, 7.8, 5.9, 8.7, 6.5]
}

# Crear DataFrame
df = pd.DataFrame(datos)

# Validar que las notas esten entre 0 y 10
if ((df["Nota"] < 0) | (df["Nota"] > 10)).any():
    print("Error: existe una nota fuera del rango permitido.")
else:
    # Determinar si aprob o reprobo
    df["Estado"] = df["Nota"].apply(
        lambda nota: "Aprobado" if nota >= 7 else "Reprobado"
    )

    # Calcular promedio
    promedio = df["Nota"].mean()

    print("TABLA DE CALIFICACIONES")
    print(df)

    print(f"\nPromedio general: {promedio:.2f}")

    # Mostrar aprobados y reprobados
    print("\nESTUDIANTES APROBADOS:")
    print(df[df["Estado"] == "Aprobado"])

    print("\nESTUDIANTES REPROBADOS:")
    print(df[df["Estado"] == "Reprobado"])