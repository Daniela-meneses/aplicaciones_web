import sqlite3

class ModeloIndex:
    def __init__(self, db_name='productos.db'):
        self.db_name = db_name

    def obtener_productos(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT nombre, descripcion, precio, existencias FROM productos")
        productos = c.fetchall()
        conn.close()
        return [Producto(*producto) for producto in productos]

    def insertar_producto(self, nombre, descripcion, precio, existencias):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("INSERT INTO productos VALUES (?, ?, ?, ?)", (nombre, descripcion, precio, existencias))
        conn.commit()
        conn.close()

    def obtener_producto_por_nombre(self, nombre):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT nombre, descripcion, precio, existencias FROM productos WHERE nombre=?", (nombre,))
        producto = c.fetchone()
        conn.close()
        if producto:
            return Producto(*producto)
        else:
            return None
        
    def actualizar_producto(self, nombre, descripcion, precio, existencias):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("UPDATE productos SET descripcion=?, precio=?, existencias=? WHERE nombre=?", (descripcion, precio, existencias, nombre))
        conn.commit()
        conn.close()

    def borrar_producto(self, nombre):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("DELETE FROM productos WHERE nombre=?", (nombre,))
        conn.commit()
        conn.close()


class Producto:
    def __init__(self, nombre, descripcion, precio, existencias):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.existencias = existencias
