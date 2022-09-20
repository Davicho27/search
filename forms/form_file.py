import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from tkinter.font import BOLD
import util.progress_line as proline
import util.generic as utl

class App:

    def __init__(self):
        
        global filenameN
        filenameN =""
        global filenameTwoN
        filenameTwoN = ""
        global filenameThreeN
        filenameThreeN = ""
        
        def browseFiles():
            filename = filedialog.askopenfilename(initialdir = "/", 
                                                title = "Select a File", 
                                                filetypes = (("Text files", 
                                                                "*.txt*"), 
                                                            ("all files", 
                                                                "*.*")))
            if(filename!=""):
                label_file_explorer.configure(text="Archivo: "+filename)

            else:
                label_file_explorer.configure(text="Aun no hay archivo disponible")
        
            global filenameN 
            filenameN = filename
            print(filenameN)
            buttonActive() 

        def browseFilesTwo():
            global filenameTwo 
            filenameTwo = filedialog.askopenfilename(initialdir = "/", 
                                                title = "Select a File", 
                                                filetypes = (("Text files", 
                                                                "*.txt*"), 
                                                            ("all files", 
                                                                "*.*"))) 
            label_file_explorer_two.configure(text="Archivo: "+filenameTwo)

            if(filenameTwo!=""):
                label_file_explorer_two.configure(text="Archivo: "+filenameTwo)
            else:
                label_file_explorer_two.configure(text="Aun no hay archivo disponible")
            
            global filenameTwoN 
            filenameTwoN = filenameTwo
            print(filenameTwoN)
            buttonActive() 

        def browseFilesThree(): 
            global filenameThree
            filenameThree = filedialog.askdirectory()

            if(filenameThree!=""):
                label_file_explorer_three.configure(text="Carpeta: "+filenameThree)
            else:
                label_file_explorer_three.configure(text="Aun no hay carpeta disponible")

            global filenameThreeN 
            filenameThreeN = filenameThree
            print(filenameThreeN)
            buttonActive()  

        def buttonActive():
            if((filenameN!="")&(filenameTwoN!="")&(filenameThreeN!="")):
                button_process.configure(state=NORMAL)

        def buttonProcess():
            print("se ejecuto")
            print(filenameN,filenameThreeN,filenameTwoN)
            if((filenameN!="")&(filenameTwoN!="")&(filenameThreeN!="")):
                proline.line_line(filenameN,filenameTwoN)
                print("Exito")
            else:
                print("No se acaba")

        self.ventana = tk.Tk()
        self.ventana.title('Busqueda')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 500)

        label_file_explorer = Label(self.ventana,  
                            text = "Archivo .txt lo que deseas buscar 'línea por línea'", 
                            width = 115, height = 4,  
                            fg = "blue") 
   
       
        button_explore = Button(self.ventana,  
                                text = "Buscar", 
                                command = browseFiles)

        label_file_explorer_two = Label(self.ventana,  
                    text = "Archivo txt de la base de datos 'línea por línea'", 
                    width = 115, height = 4,  
                    fg = "blue")

        button_explore_two = Button(self.ventana,  
                        text = "Buscar", 
                        command = browseFilesTwo)

        label_file_explorer_three = Label(self.ventana,  
                    text = "Destino del archivo", 
                    width = 115, height = 4,  
                    fg = "blue")
        
        button_explore_three = Button(self.ventana,  
                text = "Carpeta de destino", 
                command = browseFilesThree)   
        
        
        button_process = Button(self.ventana,  
                    text = "Procesar datos", 
                    command = buttonProcess,
                    state = DISABLED)  
        
        button_exit = Button(self.ventana,  
                            text = "Salir", 
                            command = exit)  
        
        label_file_explorer.grid(column = 1, row = 1) 
        
        button_explore.grid(column = 1, row = 2) 

        label_file_explorer_two.grid(column = 1, row = 3) 
        
        button_explore_two.grid(column = 1, row = 4) 
        
        label_file_explorer_three.grid(column = 1, row = 5) 
        
        button_explore_three.grid(column = 1, row = 6)
        
        button_explore_three.grid(column = 1, row = 7)  

        button_process.grid(column = 1, row = 8 )
        
        button_exit.grid(column = 1, row = 10) 

        self.ventana.mainloop()
    
    
       
        