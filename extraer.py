import pandas as pd

# Leer el archivo CSV
df = pd.read_csv("tu_archivo.csv")

# Seleccionar las columnas deseadas (ajusta los nombres)
columnas = ['columna1', 'columna3']
df_nuevo = df[columnas]

# Guardar el nuevo CSV (opcional)
df_nuevo.to_csv("nuevo_archivo.csv", index=False)
