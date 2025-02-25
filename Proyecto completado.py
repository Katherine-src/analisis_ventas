import numpy as np
import csv
analisis_ventas_np= np.array ([
    ["producto1",15,7.0],
    ["producto2",30,8.5,],
    ["producto3",25,6.5,],
    ["producto4",40,10.0],
    ["producto5",20,5.5]
    ])

print(analisis_ventas_np)

nombre_archivo = "analisis_ventas.csv"

with open(nombre_archivo, mode='w', newline='') as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerows(analisis_ventas_np)

print(f"Archivo CSV '{nombre_archivo}' creado exitosamente.")

import pandas as pd

df= pd.read_csv('analisis_ventas.csv')

print("analisis_ventas_pd se creó bien")

import pandas as pd

analisis_ventas_df= pd.DataFrame ({
    "producto1":[15,7.0],
    "producto2":[30,8.5,],
    "producto3":[25,6.5,],
    "producto4":[40,10.0],
    "producto5":[20,5.5]
    })

print(analisis_ventas_df)

column_names = ["producto", "cantidad", "precio"]

df = pd.read_csv("analisis_ventas.csv", names=column_names)

print(df)

def calcular_precio_total(cantidad,precio):
    return cantidad*precio

df["precio_total"]=df.apply(lambda row: calcular_precio_total(row["cantidad"],row["precio"]),axis=1)

print ("\nDataFrame con el precio total:")
print(df)

import matplotlib.pyplot as plt

plt.bar(df["producto"], df["precio_total"])
plt.xlabel("Producto")
plt.ylabel("Precio_total")
plt.title("precio total por producto")
plt.show()
        








