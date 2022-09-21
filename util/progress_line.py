import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox as mb

def line_line(self, pathone, pathtwo):
    num = 0
    f = open (pathone, "r")
    ft = open (pathtwo, "r")
    lineaOne = f.readlines()
    lineaDos = ft.readlines()
    nombrearch=filedialog.asksaveasfilename(initialdir = "/",title = "Guardar como",defaultextension='.txt',filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
    archi1=open(nombrearch, "w", encoding="utf-8")
    for linea in lineaOne:
        print(linea.strip())
        archi1.write(linea.strip()+"\n")
        for lineat in lineaDos:
            primero = lineat
            segundo = linea.strip()
            if(segundo in primero):
                num = num + 1
                archi1.write(lineat)
        if(num == 0):
            archi1.write("No se encontro"+"\n")
            print("No se encontro")
        num = 0
        archi1.write('\n')
    mb.showinfo("Información", "Los datos fueron guardados con exito.")
    archi1.close()
    f.close()
    return nombrearch

        
