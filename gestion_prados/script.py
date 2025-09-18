import csv
import tkinter as tk
from tkinter import ttk

def mostrar_csv(archivo):
     ventana = tk.Tk()
     ventana.title("Visualizador de CSV")

     # Crear un árbol para mostrar los datos en formato tabular
     tabla = ttk.Treeview(ventana, columns=("columna1", "columna2", ...))  # Ajusta las columnas según tu CSV
     tabla.heading("#0", text="Índice")
     tabla.heading("columna1", text="Columna 1")  # ... y así sucesivamente
     tabla.pack(expand=True, fill="both")

     with open(archivo, 'r') as csvfile:
         lector = csv.reader(csvfile)
         # Agregar los datos del CSV al árbol
         for i, fila in enumerate(lector):
             tabla.insert("", "end", values=fila)
     ventana.mainloop()

#mostrar_csv("septiembre.csv")

# import os
# print(os.getcwd())
# import pandas as pd

# df = pd.read_csv("C:/Users/Usuario/Downloads/.py/blog/web/gestion_prados/septiembre.csv", sep=";")
# print(df)

# import chardet

# with open('C:\Users\Usuario\Downloads\.py\blog\web\gestion_prados\resuelto2.csv', 'rb') as f:
#     result = chardet.detect(f.read())

# print(result)