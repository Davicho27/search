import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from tkinter.font import BOLD
import util.generic as utl

class App:

    def __init__(self):

        def browseFiles(): 
            filename = filedialog.askopenfilename(initialdir = "/", 
                                                title = "Select a File", 
                                                filetypes = (("Text files", 
                                                                "*.txt*"), 
                                                            ("all files", 
                                                                "*.*"))) 
            label_file_explorer.configure(text="File Opened: "+filename) 

        self.ventana = tk.Tk()
        self.ventana.title('Busqueda')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 500)
        label_file_explorer = Label(self.ventana,  
                            text = "File Explorer using Tkinter", 
                            width = 115, height = 4,  
                            fg = "blue") 
   
       
        button_explore = Button(self.ventana,  
                                text = "Buscar Archivo", 
                                command = browseFiles)  
        
        button_exit = Button(self.ventana,  
                            text = "Salir", 
                            command = exit)  
        
        label_file_explorer.grid(column = 1, row = 1) 
        
        button_explore.grid(column = 1, row = 2) 
        
        button_exit.grid(column = 1,row = 3) 

        self.ventana.mainloop()
    
    
       
        