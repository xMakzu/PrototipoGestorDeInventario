import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st

import articulos

class FormularioArticulos:
    def __init__(self):
        self.articulo1=articulos.Articulos()
        self.ventana1=tk.Tk()
        self.ventana1.eval('tk::PlaceWindow . center')
        self.ventana1.title("Mantenimiento de artículos")
        self.cuaderno1 = ttk.Notebook(self.ventana1)        
        self.listado_completo()
        self.carga_articulos()
        self.consulta_por_codigo()
        #self.listado_completo()
        self.borrado()
        self.modificar()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def carga_articulos(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de artículos")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Artículo")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)


        self.label1=ttk.Label(self.labelframe1, text="Código de Barras:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.Codigocarga=tk.StringVar()
        self.entryCodigo=ttk.Entry(self.labelframe1, textvariable=self.Codigocarga)
        self.entryCodigo.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe1, text="Nombre del Producto:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.Nombrecarga=tk.StringVar()
        self.entryNombre=ttk.Entry(self.labelframe1, textvariable=self.Nombrecarga)
        self.entryNombre.grid(column=1, row=1, padx=4, pady=4)

        self.label3 = ttk.Label(self.labelframe1, text="Cantidad:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.Cantidadcarga=tk.StringVar()
        self.entryCantidad=ttk.Entry(self.labelframe1, textvariable=self.Cantidadcarga)
        self.entryCantidad.grid(column=1, row=2, padx=4, pady=4)

        self.label5 = ttk.Label(self.labelframe1, text="Precio de compra:")
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        self.Preciocarga=tk.StringVar()
        self.entryPrecio=ttk.Entry(self.labelframe1, textvariable=self.Preciocarga)
        self.entryPrecio.grid(column=1, row=4, padx=4, pady=4)

        self.label6 = ttk.Label(self.labelframe1, text="Precio de venta:")
        self.label6.grid(column=0, row=5, padx=4, pady=4)
        self.PrecioVcarga=tk.StringVar()
        self.entryPrecioV=ttk.Entry(self.labelframe1, textvariable=self.PrecioVcarga)
        self.entryPrecioV.grid(column=1, row=5, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=7, padx=4, pady=4)

    def agregar(self):
        datos=(self.Codigocarga.get(), self.Nombrecarga.get(), self.Cantidadcarga.get(), self.Preciocarga.get(), self.PrecioVcarga.get())
        self.articulo1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.Codigocarga.set("")
        self.Nombrecarga.set("")
        self.Cantidadcarga.set("")
        self.Preciocarga.set("")
        self.PrecioVcarga.set("")
        

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")
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

        self.label2=ttk.Label(self.labelframe2, text="Precio de compra:")        
        self.label2.grid(column=0, row=3, padx=4, pady=4)
        self.Precio=tk.StringVar()
        self.entryPrecio=ttk.Entry(self.labelframe2, textvariable=self.Precio, state="readonly")
        self.entryPrecio.grid(column=1, row=3, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe2, text="Precio de venta:")        
        self.label2.grid(column=0, row=4, padx=4, pady=4)
        self.PrecioV=tk.StringVar()
        self.entryPrecioV=ttk.Entry(self.labelframe2, textvariable=self.PrecioV, state="readonly")
        self.entryPrecioV.grid(column=1, row=4, padx=4, pady=4)


        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=6, padx=4, pady=4)

    def consultar(self):
        datos=(self.codigo.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            #self.codigo.set(respuesta[0][0])
            self.Nombre.set(respuesta[0][0])
            self.cantidad.set(respuesta[0][1])
            self.Precio.set(respuesta[0][2])
            self.PrecioV.set(respuesta[0][3])
        else:
            self.descripcion.set('')
            self.precio.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")
            
    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")

        self.tabla = ttk.Treeview(self.pagina3, columns=("Codigo", "Nombre", "Cantidad", "Precio", "Precio de venta"), show="headings")
        self.tabla.column("Codigo", width=100, anchor="center")
        self.tabla.column("Nombre", width=200, anchor="center")
        self.tabla.column("Cantidad", width=100, anchor="center")
        self.tabla.column("Precio", width=100, anchor="center")
        self.tabla.column("Precio de venta", width=120, anchor="center")

        self.tabla.heading("Codigo", text="Codigo de barras")
        self.tabla.heading("Nombre", text="Nombre del producto")
        self.tabla.heading("Cantidad", text="Cantidad")
        self.tabla.heading("Precio", text="Precio de compra")
        self.tabla.heading("Precio de venta", text="Precio de venta")

        articulos = self.articulo1.recuperar_todos()

        for articulo in articulos:
            self.tabla.insert("", tk.END, values=articulo)

        self.tabla.pack(padx=5, pady=5)
    # Agregar botón para actualizar el listado
        estilo = ttk.Style()
        estilo.configure("TButton", padding=6, relief="flat", background="#ccc")
        btn_actualizar = ttk.Button(self.pagina3, text="Actualizar", style="TButton", command=self.actualizar_listado)
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
            self.scrolledtext1.insert(tk.END, "código de barras:"+str(fila[0])+"\nNombre del Producto:"+fila[1]+"\nCantidad:"+str(fila[2])+"\nPrecio de compra: "+str(fila[3])+"\nPrecio de venta: "+str(fila[4])+"\n\n")
           # self.scrolledtext1.insert(tk.END, "código de barras:"+str(fila[0])+"\nNombre del Producto:"+fila[1]+"\nCantidad:"+fila[2]+"\nPrecio de compra: "+fila[3]+"\nPrecio de venta: "+fila[4]+"\n\n")

    def borrado(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrado de artículos")
        self.labelframe4=ttk.LabelFrame(self.pagina4, text="Artículo")        
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe4, text="Código del artículo:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigoborra=tk.StringVar()
        self.entryborra=ttk.Entry(self.labelframe4, textvariable=self.codigoborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe4, text="Borrar", command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos=(self.codigoborra.get(), )
        cantidad=self.articulo1.baja(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se borró el artículo con dicho código")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def modificar(self):
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificar artículo")
        self.labelframe5=ttk.LabelFrame(self.pagina5, text="Artículo")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe5, text="Código de barras:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigomod=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe5, textvariable=self.codigomod)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe5, text="Nombre del producto:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.Nombremod=tk.StringVar()
        self.entryNombre=ttk.Entry(self.labelframe5, textvariable=self.Nombremod)
        self.entryNombre.grid(column=1, row=1, padx=4, pady=4)

        self.label4=ttk.Label(self.labelframe5, text="Cantidad:")        
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.Cantidadmod=tk.StringVar()
        self.entryCantidad=ttk.Entry(self.labelframe5, textvariable=self.Cantidadmod)
        self.entryCantidad.grid(column=1, row=3, padx=4, pady=4)

        self.label5=ttk.Label(self.labelframe5, text="Precio de Compra:")        
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        self.preciomod=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe5, textvariable=self.preciomod)
        self.entryprecio.grid(column=1, row=4, padx=4, pady=4)

        self.label5=ttk.Label(self.labelframe5, text="Precio de venta:")        
        self.label5.grid(column=0, row=5, padx=4, pady=4)
        self.preciovmod=tk.StringVar()
        self.entrypreciov=ttk.Entry(self.labelframe5, textvariable=self.preciovmod)
        self.entrypreciov.grid(column=1, row=5, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe5, text="Consultar", command=self.consultar_mod)
        self.boton1.grid(column=1, row=6, padx=5, pady=4)
        self.boton1=ttk.Button(self.labelframe5, text="Modificar", command=self.modifica)
        self.boton1.grid(column=3, row=6, padx=5, pady=4)

    def modifica(self):
        datos=(self.codigomod.get(), self.Nombremod.get(), self.Cantidadmod.get(), self.preciomod.get(), self.preciovmod.get())
        cantidad=self.articulo1.modificacion(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se modificó el artículo")
        else:
            mb.showinfo("Información", "No existe el artículo con ese código")

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

# aplicacion1=FormularioArticulos()