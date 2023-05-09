import sqlite3

miConexion=sqlite3.connect('PruebaDB')
miCursor=miConexion.cursor()

miCursor.execute("""
    CREATE TABLE articulos (
        codigo_barras INTEGER PRIMARY KEY,
        nombre_producto TEXT,
        cantidad INTEGER,
        fechaexp TEXT,
        precio REAL,
	    precio_venta REAL
    )
""")
Agregar_Datos=[
    ('8018190030822','JugoDeNaranja250ml','25','17/09/2023','0.50','1'),
    ('8018190030823','JugoDeNaranja500ml','25','12/09/2023','1.50','2.50'),
    ('8018190030824','JugoDePera250ml','25','24/09/2023','0.50','1'),
    ('8018190030825','JugoDeManzana250ml','25','27/10/2023','0.50','1')
]
miCursor.executemany("INSERT INTO articulos values (?,?,?,?,?,?)", Agregar_Datos)


miConexion.commit()

miConexion.close()