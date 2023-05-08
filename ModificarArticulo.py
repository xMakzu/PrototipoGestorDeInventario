import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
class ModificarArticulo:
    def __init__(self, master):
        self.master = master
        master.title("Mi Aplicación")

        # Crear un labelframe para contener todos los elementos
        self.labelframe = ttk.LabelFrame(self.master, text="Modificar Producto")
        self.labelframe.pack(fill="both", expand=True, padx=10, pady=10)

        self.label1=ttk.Label(self.labelframe, text="Código de barras:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigomod=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe, textvariable=self.codigomod)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe, text="Nombre del producto:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.Nombremod=tk.StringVar()
        self.entryNombre=ttk.Entry(self.labelframe, textvariable=self.Nombremod)
        self.entryNombre.grid(column=1, row=1, padx=4, pady=4)

        self.label4=ttk.Label(self.labelframe, text="Cantidad:")        
        self.label4.grid(column=0, row=2, padx=4, pady=4)
        self.Cantidadmod=tk.StringVar()
        self.entryCantidad=ttk.Entry(self.labelframe, textvariable=self.Cantidadmod)
        self.entryCantidad.grid(column=1, row=2, padx=4, pady=4)

        self.label4=ttk.Label(self.labelframe, text="Fecha de vencimiento:")        
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.Fechamod=tk.StringVar()
        self.entryFecha=ttk.Entry(self.labelframe, textvariable=self.Fechamod)
        self.entryFecha.grid(column=1, row=3, padx=4, pady=4)

        self.label5=ttk.Label(self.labelframe, text="Precio de Compra:")        
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        self.preciomod=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe, textvariable=self.preciomod)
        self.entryprecio.grid(column=1, row=4, padx=4, pady=4)

        self.label6=ttk.Label(self.labelframe, text="Precio de venta:")        
        self.label6.grid(column=0, row=5, padx=4, pady=4)
        self.preciovmod=tk.StringVar()
        self.entrypreciov=ttk.Entry(self.labelframe, textvariable=self.preciovmod)
        self.entrypreciov.grid(column=1, row=5, padx=4, pady=4)



        self.boton1=ttk.Button(self.labelframe, text="Consultar")
        self.boton1.grid(column=1, row=6, padx=5, pady=4)
        self.boton1=ttk.Button(self.labelframe, text="Modificar")
        self.boton1.grid(column=3, row=6, padx=5, pady=4)

         # Función de modificar articulo
    def modifica(self):
        # Obtener los datos de los campos de entrada
        codigo = self.codigomod.get()
        nombre = self.Nombremod.get()
        cantidad = self.Cantidadmod.get()
        precio = self.preciomod.get()
        precio_venta = self.preciovmod.get()

        # Verificar que el código de barras ingresado existe en la base de datos
        datos = (codigo,)
        articulo_existente = self.articulo1.consulta(datos)
        if not articulo_existente:
            mb.showerror("Error", "El artículo con ese código de barras no existe.")
            return

        # Preguntar al usuario si desea modificar el artículo
        confirmar = mb.askyesno("Confirmar", "¿Desea modificar el artículo?")
        if not confirmar:
            return

        # Modificar el artículo en la base de datos
        datos = (nombre, cantidad, precio, precio_venta, codigo)
        filas_modificadas = self.articulo1.modificacion(datos)
        if filas_modificadas == 1:
            mb.showinfo("Información", "El artículo ha sido modificado exitosamente.")
        else:
            mb.showerror("Error", "No se pudo modificar el artículo.")

    #Función de consultar articulo en la pestaña de modificar
    def consultar_mod(self):
        datos=(self.codigomod.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.Nombremod.set(respuesta[0][0])
            self.Cantidadmod.set(respuesta[0][1])
            self.preciomod.set(respuesta[0][2])
            self.preciovmod.set(respuesta[0][3])
        else:
            self.Nombremod.set('')
            self.Cantidadmod.set('')
            self.Nombremod.set('')
            self.preciomod.set('')
            self.preciovmod.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")
    
root = tk.Tk()
ModificarArticulo(root)
root.mainloop()