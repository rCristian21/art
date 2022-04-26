import pandas as pd
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Notebook
import Util
from datetime import *

#Lista de imágenes para los botones
iconos = ["./iconos/grafica.png", \
          "./iconos/datos.png"
          ]
textosBotones = ["Gráfica", \
                 "Datos"
                 ]
df = None

def obtenerMonedas():
    global df
    df = pd.read_csv("Cambios Monedas.csv")
    #Traer los datos de la columna MONEDA
    monedas = df["Moneda"].tolist()
    return list(dict.fromkeys(monedas))

def graficar():
    global df, monedas, paneles
    #Verificar que se haya seleccionado una moneda
    if cmbMoneda.current()>=0:
        #Ordenar los datos por la fecha
        df.sort_values(by="Fecha", ascending=False).head()
        #filtrar los datos por la moneda seleccionada
        cambios = df[df["Moneda"]==monedas[cmbMoneda.current()]]

        #obtener los datos para el eje Y
        y = cambios["Cambio"]

        #obtener los datos para el eje X
        fechas = cambios["Fecha"]
        #obtener la fecha
        x = [datetime.strptime(f, "%d/%m/%Y").date() for f in fechas]

        #Crear la grafica
        plt.clf() #limpiar la grafica
        plt.title("Cambio "+monedas[cmbMoneda.current()])
        plt.ylabel("Cambio")
        plt.xlabel("Fecha")
        #graficar
        plt.plot(x, y)

        #exportar la grafica a una imagen
        plt.savefig("graficaMonedas.png")

        #Mostrar la imagen de la grafica

        #Quitar elementos de un contenedor
        #list = paneles[0].grid_slaves()
        #for l in list:
        #    l.destroy()

        lblGrafica=Label(paneles[0])
        imgGrafica=PhotoImage(file = "graficaMonedas.png")

        lblGrafica.config(image=imgGrafica)
        lblGrafica.image=imgGrafica
        lblGrafica.place(x=0, y=0)
        #redimensionar la ventana de acuerdo a la dimension de la imagen de la grafica
        v.minsize(imgGrafica.width(), imgGrafica.height()+100)
        



v = Tk()
v.title("Cambios de Moneda")
v.geometry("400x200")
botones = Util.agregarBarra(v, iconos, textosBotones) #Agrega una barra de herramientas
botones[0].configure(command=graficar)

frm = Frame(v)
frm.pack(side=TOP, fill=X)
Util.agregarEtiqueta(frm, "Moneda:", 0, 0)
monedas=obtenerMonedas()
cmbMoneda=Util.agregarLista(frm, monedas, 0, 1)

nb = Notebook(v)
nb.pack(fill=BOTH, expand=YES)
encabezados=["Gráfica", "Datos"]
paneles=[]
for e in encabezados:
    frm = Frame(v)
    paneles.append(frm)
    nb.add(frm, text=e)



