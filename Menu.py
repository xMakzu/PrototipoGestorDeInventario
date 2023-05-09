import subprocess
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Menú principal")
        
        # Estilo de botones
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 14, 'bold'), foreground='Black', background='#4e5d6c', width=15, height=2)
        style.map('TButton', foreground=[('active', 'white')], background=[('active', '#263745')])
        
        # Crear botones
        self.btn_lista = ttk.Button(self.master, text="Ver lista completa", command=self.ver_lista, style='TButton')
        self.btn_agregar = ttk.Button(self.master, text="Agregar artículo", command=self.agregar_articulo, style='TButton')
        self.btn_consultar = ttk.Button(self.master, text="Consultar artículo", command=self.consultar_articulo, style='TButton')
        self.btn_borrar = ttk.Button(self.master, text="Borrar artículo", command=self.borrar_articulo, style='TButton')
        self.btn_modificar = ttk.Button(self.master, text="Modificar artículo", command=self.modificar_articulo, style='TButton')
        self.btn_recomendacion = ttk.Button(self.master, text="Recomendación IA", command=self.recomendacion_ia, style='TButton')
        
        # Colocar botones en grid
        self.btn_lista.grid(row=0, column=0, padx=20, pady=10)
        self.btn_agregar.grid(row=0, column=1, padx=20, pady=10)
        self.btn_consultar.grid(row=1, column=0, padx=20, pady=10)
        self.btn_borrar.grid(row=1, column=1, padx=20, pady=10)
        self.btn_modificar.grid(row=2, column=0, padx=20, pady=10)
        self.btn_recomendacion.grid(row=2, column=1, padx=20, pady=10)
        
    def ver_lista(self):
        subprocess.Popen(["python", "VerLista.py"])
    
    def agregar_articulo(self):
        subprocess.Popen(["python", "AgregarArticulo.py"])
    
    def consultar_articulo(self):
       subprocess.Popen(["python", "ConsultarArticulo.py"])
    
    def borrar_articulo(self):
       subprocess.Popen(["python", "BorrarArticulo.py"])
    
    def modificar_articulo(self):
       subprocess.Popen(["python", "ModificarArticulo.py"])
    
    def recomendacion_ia(self):
        subprocess.Popen(["python", "RecomendacionIA.py"])

root = tk.Tk()
VentanaPrincipal(root)
root.mainloop()
