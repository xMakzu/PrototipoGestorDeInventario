import tkinter as tk
from tkinter import ttk
import articulos

class VerLista:
    def __init__(self, master):
        self.master = master
        master.title("Ver Lista")
        self.articulo1=articulos.Articulos()

        # Crear la página principal
        self.pagina1 = ttk.Frame(self.master)
        self.pagina1.pack(fill="both", expand=True)

        # Crear la tabla en la página principal
        tabla = ttk.Treeview(self.pagina1, columns=("Codigo", "Nombre", "Cantidad","Fecha de caducidad",  "Precio", "Precio de venta"), show="headings")
        tabla.column("Codigo", width=100, anchor="center")
        tabla.column("Nombre", width=200, anchor="center")
        tabla.column("Cantidad", width=100, anchor="center")
        tabla.column("Fecha de caducidad", width=100, anchor="center")
        tabla.column("Precio", width=100, anchor="center")
        tabla.column("Precio de venta", width=120, anchor="center")
        tabla.heading("Codigo", text="Codigo de barras")
        tabla.heading("Nombre", text="Nombre del producto")
        tabla.heading("Cantidad", text="Cantidad")
        tabla.heading("Fecha de caducidad", text="Fecha de caducidad")
        tabla.heading("Precio", text="Precio de compra")
        tabla.heading("Precio de venta", text="Precio de venta")

        # Empaquetar la tabla en la página principal
        tabla.pack(fill="both", expand=True)

# Agregar botón para actualizar el listado
        estilo = ttk.Style()
        estilo.configure("TButton", padding=6, relief="flat", background="#ccc")
        btn_actualizar = ttk.Button(self.pagina1, text="Actualizar", style="TButton", command=self.actualizar_listado)
        btn_actualizar.pack(pady=10)

    def actualizar_listado(self):
        # Borra todos los elementos de la tabla
        self.tabla.delete(*self.tabla.get_children())

        # Recupera los nuevos datos y los inserta en la tabla
        articulos = self.articulo1.recuperar_todos()

        for articulo in articulos:
            self.tabla.insert("", tk.END, values=articulo)


    def listar(self):
        respuesta=self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "código de barras:"+str(fila[0])+"\nNombre del Producto:"+fila[1]+"\nCantidad:"+str(fila[2])+"\nFecha de Caducidad:"+fila[3]+"\nPrecio de compra: "+str(fila[4])+"\nPrecio de venta: "+str(fila[5])+"\n\n")

root = tk.Tk()
VerLista(root)
root.mainloop()