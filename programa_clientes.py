# Importamos la biblioteca pandas para manejar los datos
import pandas as pd

# --- PASO 1: Leer el archivo de Excel ---
# pd.read_excel carga los datos de tu archivo en un objeto llamado DataFrame.
# Ten en cuenta que los nombres de las columnas son sensibles a mayúsculas y minúsculas.
try:
    df = pd.read_excel("clientes_gestion_2025.xlsx")
except FileNotFoundError:
    print("Error: El archivo 'clientes_gestion_2025.xlsx' no se encontró. Asegúrate de que esté en la misma carpeta que este script.")
    exit()

# --- PASO 2: Agrupar por cliente y sumar los totales ---
# .groupby('Nombre') agrupa todas las filas que tienen el mismo nombre de cliente.
# ['Total'].sum() suma todos los valores de la columna 'Total' para cada grupo.
total_por_cliente = df.groupby('Nombre')['Total'].sum()

# --- PASO 3: Imprimir el resultado ---
print("El total de compras por cliente es el siguiente:")
print("-" * 30)
print(total_por_cliente)

# --- (Opcional) PASO 4: Guardar el resultado en un nuevo archivo Excel ---
# Puedes descomentar la siguiente línea si quieres guardar el resultado
total_por_cliente.to_excel("total_por_cliente.xlsx")
# print("\nSe ha creado el archivo 'total_por_cliente.xlsx' con los resultados.")