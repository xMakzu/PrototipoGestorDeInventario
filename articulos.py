import sqlite3
import datetime

class Articulos:

    def abrir(self):
        conexion=sqlite3.connect("PruebaDB")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into articulos(codigo_barras, nombre_producto, cantidad, fechaexp, precio, precio_venta) values (?,?,?,?,?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select nombre_producto, cantidad, fechaexp, precio, precio_venta from articulos where codigo_barras=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()

    def recuperar_todos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select codigo_barras, nombre_producto, cantidad, fechaexp, precio, precio_venta from articulos"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def recuperar(self, codigo):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select codigo_barras, nombre_producto, cantidad, fechaexp, precio, precio_venta from articulos where codigo_barras=?"
            cursor.execute(sql, (codigo,))
            return cursor.fetchone()
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
            sql="UPDATE articulos set nombre_producto=?, cantidad=?, fechaexp=?, precio=?, precio_venta=? where codigo_barras=?"
            
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas modificadas            
        except:
            cone.close()

    def obtener_recomendaciones(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            # Consulta de los artículos con 20 o menos unidades
            sql="SELECT codigo_barras, nombre_producto, cantidad, precio FROM articulos WHERE cantidad <= 20"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()
        

    def obtener_recomendaciones_caducidad(self):
        fecha_actual = datetime.date.today()
        fecha_limite = fecha_actual + datetime.timedelta(days=7)
        try:
            cone = self.abrir()
            cursor = cone.cursor()
            # Consulta de los artículos próximos a caducar en los próximos 7 días
            sql = "SELECT codigo_barras, nombre_producto, fechaexp FROM articulos WHERE fechaexp IS NOT NULL"
            cursor.execute(sql)
            productos = []
            for codigo_barras, nombre_producto, fechaexp in cursor.fetchall():
                fecha_caducidad = datetime.datetime.strptime(fechaexp, '%d/%m/%Y').date()
                dias_diferencia = (fecha_caducidad - fecha_actual).days
                if (dias_diferencia <= 7 and fecha_caducidad.year == fecha_actual.year) or (fecha_caducidad <= fecha_actual):
                    productos.append((codigo_barras, nombre_producto, fechaexp))
            return productos
        finally:
            cone.close()

    










