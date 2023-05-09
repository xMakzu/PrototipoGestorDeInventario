import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import articulos

class BorrarArticulo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Borrar Artículo")

        self.articulo = articulos.Articulo()

        # Crear un estilo personalizado para los widgets
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 12))

        # Codigo grafico para pestaña borrar
        self.pagina3 = ttk.Frame(self.ventana)
        self.pagina3.pack()
        self.labelframe3 = ttk.LabelFrame(self.pagina3, text="Artículo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)

        self.label1 = ttk.Label(self.labelframe3, text="Código de Barras:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo = tk.StringVar()
        self.entrycodigo = ttk.Entry(self.labelframe3, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)

        self.boton1 = ttk.Button(self.labelframe3, text="Borrar", command=self.borrar_articulo)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    # Crear función Borrar
    def borrar_articulo(self):
        codigo = self.codigo.get()
        respuesta = self.articulo.borrar(codigo)
        if respuesta:
            mb.showinfo("Información", "El artículo se ha borrado exitosamente")
        else:
            mb.showinfo("Información", "No se ha encontrado el artículo a borrar")

root = tk.Tk()
BorrarArticulo(root)
root.mainloop()
