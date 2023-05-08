import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

class AgregarArticulo:
    def __init__(self, master):
        self.master = master
        self.master.title("Agregar Artículo")

        # Crear un estilo personalizado para los widgets
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 12))

        # Crear el frame principal
        self.labelframe1 = ttk.LabelFrame(self.master, text="Artículo", padding=20)
        self.labelframe1.grid(column=0, row=0, padx=20, pady=20, sticky='nsew')

        # Crear los widgets del formulario
        ttk.Label(self.labelframe1, text="Código de barras:").grid(column=0, row=0, padx=10, pady=10)
        self.Codigocarga = tk.StringVar()
        ttk.Entry(self.labelframe1, textvariable=self.Codigocarga, width=30).grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(self.labelframe1, text="Nombre del producto:").grid(column=0, row=1, padx=10, pady=10)
        self.Nombrecarga = tk.StringVar()
        ttk.Entry(self.labelframe1, textvariable=self.Nombrecarga, width=30).grid(column=1, row=1, padx=10, pady=10)

        ttk.Label(self.labelframe1, text="Cantidad:").grid(column=0, row=2, padx=10, pady=10)
        self.Cantidadcarga = tk.StringVar()
        ttk.Entry(self.labelframe1, textvariable=self.Cantidadcarga, width=30).grid(column=1, row=2, padx=10, pady=10)

        ttk.Label(self.labelframe1, text="Precio de compra:").grid(column=0, row=3, padx=10, pady=10)
        self.Preciocarga = tk.StringVar()
        ttk.Entry(self.labelframe1, textvariable=self.Preciocarga, width=30).grid(column=1, row=3, padx=10, pady=10)

        ttk.Label(self.labelframe1, text="Precio de venta:").grid(column=0, row=4, padx=10, pady=10)
        self.PrecioVcarga = tk.StringVar()
        ttk.Entry(self.labelframe1, textvariable=self.PrecioVcarga, width=30).grid(column=1, row=4, padx=10, pady=10)

        ttk.Label(self.labelframe1, text="Fecha de caducidad:").grid(column=0, row=5, padx=10, pady=10)
        self.FechaCarga = tk.StringVar()
        ttk.Entry(self.labelframe1, textvariable=self.FechaCarga, width=30).grid(column=1, row=5, padx=10, pady=10)

        ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar).grid(column=1, row=6, padx=10, pady=20, sticky='e')

        # Agregar padding a las filas y columnas del frame
        for i in range(6):
            self.labelframe1.columnconfigure(i, weight=1, minsize=100)
            self.labelframe1.rowconfigure(i, weight=1, minsize=50)

    # Crear función agregar
    def agregar(self):
        datos=(self.Codigocarga.get(), self.Nombrecarga.get(), self.Cantidadcarga.get(), self.Preciocarga.get(), self.PrecioVcarga.get())
        self.articulo1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.Codigocarga.set("")
        self.Nombrecarga.set("")
        self.Cantidadcarga.set("")
        self.Preciocarga.set("")
        self.PrecioVcarga.set("")    

root = tk.Tk()
AgregarArticulo(root)
root.mainloop()