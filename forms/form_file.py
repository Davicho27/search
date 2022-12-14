import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog
from tkinter import messagebox as mb
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


        def buttonActive():
            if((filenameN!="")&(filenameTwoN!="")):
                button_process.configure(state=NORMAL)

        def buttonProcess():
            print("se ejecuto")
            button_process.configure(state=DISABLED)
            global filenameN
            global filenameTwoN
            print(filenameN,filenameTwoN)
            if((filenameN!="")&(filenameTwoN!="")):
                archivo = proline.line_line(self, filenameN, filenameTwoN)
                label_file_explorer.configure(text="Archivo .txt lo que deseas buscar 'l??nea por l??nea'")
                label_file_explorer_two.configure(text="Archivo .txt de la base de datos 'l??nea por l??nea'")
                filenameN =""
                filenameTwoN = ""
                label_file_explorer_three.configure(text="Destino del archivo: "+archivo)
                print("Exito")
            else:
                mb.showinfo("Error", "Se ha producido un error en la carga de archivos.")
                print("Se acab??")

        self.ventana = tk.Tk()
        self.ventana.title('B??squeda')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#05B7D0')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 560)

        label_title= Label(self.ventana,  
                            text = "B??squeda .TXT",font=("Times New Roman", 25, 'bold'),
                            bg='#05B7D0',
                            fg='#ffffff', 
                            width = 20, height = 3) 

        label_file_explorer = Label(self.ventana,  
                            text = "Archivo .txt lo que deseas buscar 'l??nea por l??nea'", 
                            width = 90, height = 4,
                            font=("Arial", 10),
                            bg= '#05AAC1',  
                            fg = "white") 
   
       
        button_explore = Button(self.ventana,  
                                text = "Buscar", 
                                command = browseFiles,
                                bg='#007D8F',  
                                fg = 'white', 
                                height = 2, 
                                width = 14)
        


        label_file_explorer_two = Label(self.ventana,  
                    text = "Archivo .txt de la base de datos 'l??nea por l??nea'", 
                    width = 90, height = 4,
                    font=("Arial", 10),
                    bg= '#05AAC1',   
                    fg = "white")

        button_explore_two = Button(self.ventana,  
                        text = "Buscar", 
                        command = browseFilesTwo,
                        bg='#007D8F',  
                        fg = 'white', 
                        height = 2, 
                        width = 14)

        label_file_explorer_three = Label(self.ventana,  
                    text = "Destino del archivo", 
                    width = 90, height = 4,
                    font=("Arial", 11),
                    bg= '#ffffff',   
                    fg = "black") 
        
        
        button_process = Button(self.ventana,  
                    text = "Guardar datos", 
                    command = buttonProcess,
                    state = DISABLED,
                    bg='#25FF7E',  
                    fg = 'white', 
                    height = 2, 
                    width = 14)  
        
        button_exit = Button(self.ventana,  
                            text = "Salir", 
                            command = exit,
                            bg='#F8413C',  
                            fg = 'white', 
                            height = 2, 
                            width = 14)  
        
        label_title.grid(column = 1, row = 1) 

        label_file_explorer.grid(column = 1, row = 2) 
        
        button_explore.grid(column = 1, row = 3, pady = 4, padx = 100) 

        label_file_explorer_two.grid(column = 1, row = 4) 
        
        button_explore_two.grid(column = 1, row = 5, pady = 4, padx = 100)
        
        label_file_explorer_three.grid(column = 1, row = 6) 

        button_process.grid(column = 1, row = 9, pady = 8, padx = 100)
        
        button_exit.grid(column = 1, row = 11, pady = 8, padx = 100) 

        self.ventana.mainloop()
    
    
       
        