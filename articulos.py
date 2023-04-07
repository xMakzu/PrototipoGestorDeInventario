import sqlite3

class Articulos:

    def abrir(self):
        conexion=sqlite3.connect("PruebaDB")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into articulos(codigo_barras, nombre_producto, cantidad, precio, precio_venta) values (?,?,?,?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select nombre_producto, cantidad,precio, precio_venta from articulos where codigo_barras=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()

    def recuperar_todos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select codigo_barras, nombre_producto, cantidad, precio, precio_venta from articulos"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def baja(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="delete from articulos where codigo_barras=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas borradas
        except:
            cone.close()
    
    def modificacion(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="UPDATE articulos set nombre_producto=?, cantidad=?, precio=?, precio_venta=? where codigo_barras=?"
            
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas modificadas            
        except:
            cone.close()