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
Agregar_Datos=[       ('8018190030822','JugoDeNaranja250ml','25','17/09/2023','0.50','1'),
                      ('8018190030823','JugoDeNaranja500ml','25','12/09/2023','1.50','2.50'),     
                      ('8018190030824','JugoDePera250ml','25','24/09/2023','0.50','1'),    
                      ('8018190030825','JugoDeManzana250ml','25','27/10/2023','0.50','1'), 
                      ('1209837410234','BarraDeCereal100g','15','12/06/2024','1.20','3'), 
                      ('8654281093632','AguaMineral500ml','30','30/09/2023','0.90','2'), 
                      ('6749102384105','GalletasDeAvena200g','20','18/05/2024','2.50','5'), 
                      ('3640912385123','LecheDeslactosada1L','50','10/12/2023','1.80','4'), 
                      ('8734901285710','CervezaArtesanal330ml','80','02/03/2025','3.50','6'), 
                      ('9438501287402','YogurtNatural250g','35','25/07/2024','1.10','2'), 
                      ('7601293850129','PapasFritasDeMaiz100g','10','01/09/2023','0.70','1'), 
                      ('2874310948510','AtunEnAceite120g','45','06/11/2024','1.60','3'), 
                      ('5203910483056','MantequillaDeMani500g','70','15/08/2023','4.20','7'), 
                      ('5498102395710','ChocolateNegro75g','25','22/06/2024','1.80','4')]


miCursor.executemany("INSERT INTO articulos values (?,?,?,?,?,?)", Agregar_Datos)


miConexion.commit()

miConexion.close()