import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from datetime import datetime
from articulos import Articulos
import articulos
import docx
import datetime
from docx import Document
from docx.shared import Cm
from docx.enum.table import WD_TABLE_ALIGNMENT
import sqlite3



class FormularioArticulos:
    def __init__(self):
        self.articulo1=articulos.Articulos()
        self.ventana1=tk.Tk()
        self.ventana1.eval('tk::PlaceWindow . center')
        self.ventana1.title("Prototipo Gestor de Inventario")
        self.cuaderno1 = ttk.Notebook(self.ventana1)        
        self.listado_completo()
        self.carga_articulos()
        self.AnalisisdeDatos()
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
        style.configure('TButton', font=('Arial', 10))
        
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
        ttk.Label(self.labelframe1, text="dd/mm/aaaa").grid(column=2, row=3, padx=10, pady=10)
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
        ttk.Button(self.labelframe1, text="Mostrar Articulo", command=self.consultar).grid(column=2, row=0, padx=10, pady=20, sticky='e')
        

        
        # Agregar padding a las filas y columnas del frame
        for i in range(5):
            self.labelframe1.columnconfigure(i, weight=1, minsize=100)
            self.labelframe1.rowconfigure(i, weight=1, minsize=50)

    # Crear función agregar
    def agregar(self):
        codigo = self.Codigocarga.get()
        nombre = self.Nombrecarga.get()
        cantidad = self.Cantidadcarga.get()
        fecha = self.fechaexp.get()
        precio = self.Preciocarga.get()
        precio_venta = self.PrecioVcarga.get()

        if not codigo or not nombre or not cantidad or not fecha or not precio or not precio_venta:
            mb.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
            return

        datos = (codigo, nombre, cantidad, fecha, precio, precio_venta)
        try:
            self.articulo1.alta(datos)
            mb.showinfo("Información", "Los datos fueron cargados")
            self.Codigocarga.set("")
            self.Nombrecarga.set("")
            self.Cantidadcarga.set("")
            self.fechaexp.set("")
            self.Preciocarga.set("")
            self.PrecioVcarga.set("")
        except sqlite3.IntegrityError:
            mb.showerror("Error", "El código ya existe. No se pueden agregar productos duplicados.")
            #cambio1
            

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
        if not articulo_existente and cantidad is not None and cantidad != 0:
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
            self.limpiar_campos()
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

    def limpiar_campos(self):
        self.Codigocarga.set('')
        self.Nombrecarga.set('')
        self.Cantidadcarga.set('')
        self.fechaexp.set('')
        self.Preciocarga.set('')
        self.PrecioVcarga.set('')

    # Codigo de tabla
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

        btn_buscar = ttk.Button(frame_busqueda, text="Borrar Articulo", command=self.borrar)
        btn_buscar.pack(side="left", padx=10)

        btn_buscar = ttk.Button(frame_busqueda, text="Crear Informe", command=self.crear_informe)
        btn_buscar.pack(side="left", padx=10)
        
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
            
            # Actualizar la tabla de búsqueda de nuevo en 1 segundo
            self.tabla.after(1000, self.actualizar_tabla)  # llamar a actualizar_tabla_busqueda() de nuevo en 1 segundo
            
        else:
            mb.showerror("Error", f"No se encontró el artículo con el código {codigo}")

    def actualizar_tabla(self):
        # Borra todos los elementos de la tabla
        self.tabla.delete(*self.tabla.get_children())

        # Recupera el código de búsqueda
        codigo = self.entry_busqueda.get()

        # Si el campo de búsqueda está vacío, mostrar todos los artículos
        if not codigo:
            for articulo in self.articulo1.recuperar_todos():
                self.tabla.insert("", tk.END, values=articulo)

        # Si hay un código de búsqueda, buscar y mostrar el artículo correspondiente
        else:
            articulo = self.articulo1.recuperar(codigo)
            if articulo:
                self.tabla.insert("", tk.END, values=articulo)

        # Actualizar la tabla de búsqueda de nuevo en 1 segundo
        self.tabla.after(1000, self.actualizar_tabla)  # llamar a actualizar_tabla() de nuevo en 1 segundo

    #Eliminar articulo
    def eliminar_articulo(self):
        codigo = self.entry_busqueda.get()
        if self.articulo1.baja(codigo):
            self.tabla.delete(*self.tabla.get_children())
            self.actualizar_tabla()
            mb.showinfo("Información", f"El artículo con código {codigo} ha sido eliminado exitosamente.")
        else:
            mb.showerror("Error", f"No se encontró el artículo con el código {codigo}.")

    def borrar(self):
        confirmar = mb.askyesno("Confirmar", "¿Desea borrar el artículo?")
        if not confirmar:
            return
        datos=(self.entry_busqueda.get(), )
        cantidad=self.articulo1.baja(datos)
        
        if cantidad==1:
            mb.showinfo("Información", "Se borró el artículo con dicho código")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

    #Crear informe
    def crear_informe(self):
        # Crear el documento de Word y agregar una tabla
        if mb.askyesno("Crear informe", "¿Está seguro que desea crear el informe?"):
            document = Document()
            table = document.add_table(rows=1, cols=6, style="Table Grid")
            
            # Agregar encabezados de columna a la tabla
            headings = table.rows[0].cells
            headings[0].text = "Codigo de barras"
            headings[1].text = "Nombre del producto"
            headings[2].text = "Cantidad"
            headings[3].text = "Fecha de caducidad"
            headings[4].text = "Precio de compra"
            headings[5].text = "Precio de venta"
            
            # Agregar filas de datos a la tabla
            articulos = self.articulo1.recuperar_todos()
            for articulo in articulos:
                row_cells = table.add_row().cells
                row_cells[0].text = str(articulo[0])
                row_cells[1].text = articulo[1]
                row_cells[2].text = str(articulo[2])
                row_cells[3].text = str(articulo[3])
                row_cells[4].text = str(articulo[4])
                row_cells[5].text = str(articulo[5])
            
            # Dar formato a la tabla
            table.alignment = WD_TABLE_ALIGNMENT.CENTER
            table.autofit = False
            table.allow_autofit = False
            for column in table.columns:
                column.width = Cm(2.5)
            
            # Guardar el documento de Word
            document.save("informe.docx")
            mb.showinfo("Informe creado", "Se ha creado el informe con éxito.")

    def AnalisisdeDatos(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Análisis de datos")

        frame_busqueda = ttk.Frame(self.pagina4)
        frame_busqueda.pack(side="top", fill="x", padx=5, pady=5)

        lbl_busqueda = ttk.Label(frame_busqueda, text="Se deben comprar estos articulos:")
        lbl_busqueda.pack(side="left", padx=5)

        # Creación del Treeview para recomendaciones por cantidad
        self.treeview_cantidad = ttk.Treeview(self.pagina4, columns=("codigo_barras", "nombre_producto", "cantidad_producto", "precio"))
        self.treeview_cantidad.pack(side="top", fill="both", expand=True)

        # Configuración de las columnas del Treeview para recomendaciones por cantidad
        self.treeview_cantidad.heading("#0", text="ID")
        self.treeview_cantidad.heading("codigo_barras", text="Código de barras")
        self.treeview_cantidad.heading("nombre_producto", text="Nombre del producto")
        self.treeview_cantidad.heading("cantidad_producto", text="Cantidad")
        self.treeview_cantidad.heading("precio", text="Precio")
        self.treeview_cantidad.column("#0", width=50)
        self.treeview_cantidad.column("codigo_barras", anchor="center")
        self.treeview_cantidad.column("nombre_producto", anchor="center")
        self.treeview_cantidad.column("cantidad_producto", anchor="center")
        self.treeview_cantidad.column("precio", anchor="center")

        # Creación del Treeview para recomendaciones por caducidad
        self.treeview_caducidad = ttk.Treeview(self.pagina4, columns=("codigo_barras", "nombre_producto", "fecha_vencimiento", "precio"))
        self.treeview_caducidad.pack(side="top", fill="both", expand=True)

        # Label para la tabla de recomendaciones por caducidad
        lbl_caducidad = ttk.Label(self.pagina4, text="Estos artículos están proximos a vencer o ya caducaron:")
        lbl_caducidad.pack(side="top", padx=10, before=self.treeview_caducidad)

        # Configuración de las columnas del Treeview para recomendaciones por caducidad
        self.treeview_caducidad.heading("#0", text="ID")
        self.treeview_caducidad.heading("codigo_barras", text="Código de barras")
        self.treeview_caducidad.heading("nombre_producto", text="Nombre del producto")
        self.treeview_caducidad.heading("fecha_vencimiento", text="Fecha de vencimiento")
        self.treeview_caducidad.column("#0", width=50)
        self.treeview_caducidad.column("codigo_barras", anchor="center")
        self.treeview_caducidad.column("nombre_producto", anchor="center")
        self.treeview_caducidad.column("fecha_vencimiento", anchor="center")



        # Botón para obtener la lista de artículos recomendados
        btn_obtener = ttk.Button(frame_busqueda, text="Obtener Análisis", command=self.obtener_articulos)
        btn_obtener.pack(side="right", padx=5, pady=5)

    def obtener_articulos(self):
        # Llamada al método para obtener las recomendaciones de productos
        recomendaciones = self.articulo1.obtener_recomendaciones()

        # Borra todos los elementos de la tabla de recomendaciones
        self.treeview_cantidad.delete(*self.treeview_cantidad.get_children())

        # Inserta las recomendaciones en la tabla de recomendaciones
        for i, recomendacion in enumerate(recomendaciones):
            self.treeview_cantidad.insert("", tk.END, text=i+1, values=recomendacion)

        # Llamada al método para obtener los productos próximos a caducar
        productos_caducidad = self.articulo1.obtener_recomendaciones_caducidad()

        # Borra todos los elementos de la tabla de productos por caducidad
        self.treeview_caducidad.delete(*self.treeview_caducidad.get_children())

        # Inserta los productos por caducidad en la tabla correspondiente
        for i, producto in enumerate(productos_caducidad):
            fecha = datetime.datetime.strptime(producto[2], '%d/%m/%Y').strftime('%d/%m/%Y')
            self.treeview_caducidad.insert("", tk.END, text=i+1, values=(producto[0], producto[1], fecha))










       