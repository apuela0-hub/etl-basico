import pandas as pd

# EXTRACT
df = pd.read_csv("datos.txt")

# TRANSFORM
# 1. Eliminar duplicados
df = df.drop_duplicates()

# 2. Convertir edad e importe a numérico (errores → NaN)
df["edad"] = pd.to_numeric(df["edad"], errors="coerce")
df["importe"] = pd.to_numeric(df["importe"], errors="coerce")

# 3. Eliminar edades inválidas
df = df[df["edad"].between(0, 120)]

# 4. Eliminar importes negativos o vacíos
df = df[df["importe"] > 0]

# 5. Rellenar datos faltantes
df["nombre"] = df["nombre"].fillna("SIN NOMBRE")
df["ciudad"] = df["ciudad"].fillna("SIN CIUDAD")

# LOAD
df.to_excel("resultado.xlsx", index=False)

print("ETL ejecutado correctamente. Datos limpios y ordenados.")
