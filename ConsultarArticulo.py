import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import articulos
from articulos import consulta


class ConsultarArticulo:
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.title("Consultar Artículo")

        self.articulo1=Articulo()

         # Crear un estilo personalizado para los widgets
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 12))

        # Codigo grafico para pestaña consultar
        self.pagina2 = ttk.Frame(self.ventana)
        self.pagina2.pack()
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Artículo")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe2, text="Código de Barras:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe2, text="Nombre del Producto:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.Nombre=tk.StringVar()
        self.entryNombre=ttk.Entry(self.labelframe2, textvariable=self.Nombre, state="readonly")
        self.entryNombre.grid(column=1, row=1, padx=4, pady=4)

        self.label3=ttk.Label(self.labelframe2, text="Cantidad:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.cantidad=tk.StringVar()
        self.entrycantidad=ttk.Entry(self.labelframe2, textvariable=self.cantidad, state="readonly")
        self.entrycantidad.grid(column=1, row=2, padx=4, pady=4)

        self.label4=ttk.Label(self.labelframe2, text="Precio de compra:")        
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.Precio=tk.StringVar()
        self.entryPrecio=ttk.Entry(self.labelframe2, textvariable=self.Precio, state="readonly")
        self.entryPrecio.grid(column=1, row=3, padx=4, pady=4)

        self.label5=ttk.Label(self.labelframe2, text="Precio de venta:")        
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        self.PrecioV=tk.StringVar()
        self.entryPrecioV=ttk.Entry(self.labelframe2, textvariable=self.PrecioV, state="readonly")
        self.entryPrecioV.grid(column=1, row=4, padx=4, pady=4)

        self.label6 = ttk.Label(self.labelframe2, text="Fecha de caducidad:")
        self.label6.grid(column=0, row=5, padx=4, pady=4)
        self.fecha = tk.StringVar()
        self.entryFecha = ttk.Entry(self.labelframe2, textvariable=self.fecha, state="readonly")
        self.entryFecha.grid(column=1, row=5, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=6, padx=4, pady=4)


    # Crear función Consultar
    def consultar(self):
        datos=(self.codigo.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.Nombre.set(respuesta[0][0])
            self.cantidad.set(respuesta[0][1])
            self.Precio.set(respuesta[0][2])
            self.PrecioV.set(respuesta[0][3])
        else:
            self.descripcion.set('')
            self.precio.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")

root = tk.Tk()
ConsultarArticulo(root)
root.mainloop()