import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import articulos
from articulos import Articulos

class FormularioArticulos:
    def __init__(self):
        self.articulo1=articulos.Articulos()
        self.ventana1=tk.Tk()
        self.ventana1.eval('tk::PlaceWindow . center')
        self.ventana1.title("Mantenimiento de artículos")
        self.cuaderno1 = ttk.Notebook(self.ventana1)        
        self.listado_completo()
        self.carga_articulos()
        self.borrado()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    # Codigo grafico para penstaña agregar articulos
    def carga_articulos(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Crear/Editar")
        
        # Crear un estilo personalizado para los widgets
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 12))
        
        # Crear el frame principal
        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Crear/Editar", padding=20)
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

        ttk.Label(self.labelframe1, text="Fecha de Caducidad:").grid(column=0, row=3, padx=10, pady=10)
        self.fechaexp = tk.StringVar()
        ttk.Entry(self.labelframe1, textvariable=self.fechaexp, width=30).grid(column=1, row=3, padx=10, pady=10)
        
        ttk.Label(self.labelframe1, text="Precio de compra:").grid(column=0, row=4, padx=10, pady=10)
        self.Preciocarga = tk.StringVar()
        ttk.Entry(self.labelframe1, textvariable=self.Preciocarga, width=30).grid(column=1, row=4, padx=10, pady=10)
        
        ttk.Label(self.labelframe1, text="Precio de venta:").grid(column=0, row=5, padx=10, pady=10)
        self.PrecioVcarga = tk.StringVar()
        ttk.Entry(self.labelframe1, textvariable=self.PrecioVcarga, width=30).grid(column=1, row=5, padx=10, pady=10)
        
        ttk.Button(self.labelframe1, text="Agregar Articulo", command=self.agregar).grid(column=1, row=6, padx=10, pady=20, sticky='e')
        ttk.Button(self.labelframe1, text="Modificar Articulo", command=self.modifica).grid(column=2, row=6, padx=10, pady=20, sticky='e')
        ttk.Button(self.labelframe1, text="Ver Producto", command=self.consultar).grid(column=2, row=0, padx=10, pady=20, sticky='e')
    
        
        # Agregar padding a las filas y columnas del frame
        for i in range(5):
            self.labelframe1.columnconfigure(i, weight=1, minsize=100)
            self.labelframe1.rowconfigure(i, weight=1, minsize=50)

    # Crear función agregar
    def agregar(self):
        datos=(self.Codigocarga.get(), self.Nombrecarga.get(), self.Cantidadcarga.get(), self.fechaexp.get(), self.Preciocarga.get(), self.PrecioVcarga.get())
        self.articulo1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.Codigocarga.set("")
        self.Nombrecarga.set("")
        self.Cantidadcarga.set("")
        self.fechaexp.set("")
        self.Preciocarga.set("")
        self.PrecioVcarga.set("")

     # Función de modificar articulo
    def modifica(self):
        # Obtener los datos de los campos de entrada
        codigo = self.Codigocarga.get()
        nombre = self.Nombrecarga.get()
        cantidad = self.Cantidadcarga.get()
        fecha = self.fechaexp.get()
        precio = self.Preciocarga.get()
        precio_venta = self.PrecioVcarga.get()

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
        datos = (nombre, cantidad, fecha, precio, precio_venta, codigo)
        filas_modificadas = self.articulo1.modificacion(datos)
        if filas_modificadas == 1:
            mb.showinfo("Información", "El artículo ha sido modificado exitosamente.")
        else:
            mb.showerror("Error", "No se pudo modificar el artículo.")

    # Crear función Consultar
    def consultar(self):
        datos=(self.Codigocarga.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.Nombrecarga.set(respuesta[0][0])
            self.Cantidadcarga.set(respuesta[0][1])
            self.fechaexp.set(respuesta[0][2])
            self.Preciocarga.set(respuesta[0][3])
            self.PrecioVcarga.set(respuesta[0][4])
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

    # Codigo de tabla para ver la lista completa
    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")

        self.tabla = ttk.Treeview(self.pagina3, columns=("Codigo", "Nombre", "Cantidad", "Fecha de caducidad", "Precio", "Precio de venta"), show="headings")
        self.tabla.column("Codigo", width=100, anchor="center")
        self.tabla.column("Nombre", width=200, anchor="center")
        self.tabla.column("Cantidad", width=100, anchor="center")
        self.tabla.column("Fecha de caducidad", width=200, anchor="center")
        self.tabla.column("Precio", width=100, anchor="center")
        self.tabla.column("Precio de venta", width=120, anchor="center")

        self.tabla.heading("Codigo", text="Codigo de barras")
        self.tabla.heading("Nombre", text="Nombre del producto")
        self.tabla.heading("Cantidad", text="Cantidad")
        self.tabla.heading("Fecha de caducidad", text="Fecha de caducidad")
        self.tabla.heading("Precio", text="Precio de compra")
        self.tabla.heading("Precio de venta", text="Precio de venta")


        # Crear la entrada para ingresar el código del artículo
        frame_busqueda = ttk.Frame(self.pagina3)
        frame_busqueda.pack(side="top", fill="x", padx=5, pady=5)

        lbl_busqueda = ttk.Label(frame_busqueda, text="Buscar por código:")
        lbl_busqueda.pack(side="left", padx=5)

        self.entry_busqueda = ttk.Entry(frame_busqueda)
        self.entry_busqueda.pack(side="left", fill="x", expand=True, padx=5)

        # Agregar botón de búsqueda
        btn_buscar = ttk.Button(frame_busqueda, text="Buscar", command=self.buscar_articulo)
        btn_buscar.pack(side="left", padx=5)

        articulos = self.articulo1.recuperar_todos()

        for articulo in articulos:
            self.tabla.insert("", tk.END, values=articulo)

        self.tabla.pack(padx=5, pady=5)

    def buscar_articulo(self):
        codigo = self.entry_busqueda.get()
        articulo = self.articulo1.recuperar(codigo)
        if articulo:
            self.tabla.delete(*self.tabla.get_children())
            self.tabla.insert("", tk.END, values=articulo)
        else:
            mb.showerror("Error", f"No se encontró el artículo con el código {codigo}")


    # Codigo grafico para pestaña de borrar articulo
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

    # Función borrar articulo
    def borrar(self):
        confirmar = mb.askyesno("Confirmar", "¿Desea borrar el artículo?")
        if not confirmar:
            return
        
        datos=(self.codigoborra.get(), )
        cantidad=self.articulo1.baja(datos)
        
        if cantidad==1:
            mb.showinfo("Información", "Se borró el artículo con dicho código")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")
