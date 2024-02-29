import web
from mvc.models.index import ModeloIndex

render = web.template.render('mvc/views/', base='layout')
m_index = ModeloIndex()

class Index:
    def GET(self):
        try:
            # Obtener los productos de la base de datos
            productos = m_index.obtener_productos()

            return render.index(productos=productos)
        except Exception as e:
            print(f"Error: {e}")
            return "Lo siento, algo salió mal."
        

class Insertar:
    def GET(self):
        try:
            return render.insertar()
        except Exception as e:
            print(f"Error: {e}")
            return "Lo siento, algo salió mal."

    def POST(self):
        try:
            data = web.input(nombre=None, descripcion=None, precio=None, existencias=None)
            nombre = data.get('nombre')
            descripcion = data.get('descripcion')
            precio = data.get('precio')
            existencias = data.get('existencias')

            if not nombre or not descripcion or not precio or not existencias:
                return "Todos los campos son obligatorios. Por favor, complete el formulario correctamente."

            if not precio.isdigit() or not existencias.isdigit():
                return "El precio y las existencias deben ser números enteros."

            precio = int(precio)
            existencias = int(existencias)

            if precio <= 0 or existencias < 0:
                return "El precio debe ser mayor que cero y las existencias no pueden ser negativas."

            m_index.insertar_producto(nombre, descripcion, precio, existencias)

            raise web.seeother('/')
        except Exception as e:
            print(f"Error: {e}")
            return "Lo siento, algo salió mal."
        
class Ver:
    def GET(self):
        try:
            nombre_producto = web.input().get('nombre')
            # Obtener el producto específico del modelo usando el nombre del producto
            producto = m_index.obtener_producto_por_nombre(nombre_producto)
            
            if producto:
                return render.ver(producto=producto)
            else:
                return "Producto no encontrado."
        except Exception as e:
            print(f"Error: {e}")
            return "Lo siento, algo salió mal."


class Actualizar:
    def GET(self):
        try:
            nombre_producto = web.input().get('nombre')

            producto = m_index.obtener_producto_por_nombre(nombre_producto)
            
            if producto:
                return render.actualizar(producto=producto)
            else:
                return "Producto no encontrado."
        except Exception as e:
            print(f"Error: {e}")
            return "Lo siento, algo salió mal."


    def POST(self):
        try:
            data = web.input(nombre=None, descripcion=None, precio=None, existencias=None)
            nombre_producto = data.get('nombre')  # Nombre del producto a actualizar
            descripcion = data.get('descripcion')
            precio = data.get('precio')
            existencias = data.get('existencias')

            if not nombre_producto or not descripcion or not precio or not existencias:
                return "Todos los campos son obligatorios. Por favor, complete el formulario correctamente."

            if not precio.isdigit() or not existencias.isdigit():
                return "El precio y las existencias deben ser números enteros."

            precio = int(precio)
            existencias = int(existencias)

            if precio <= 0 or existencias < 0:
                return "El precio debe ser mayor que cero y las existencias no pueden ser negativas."

            m_index.actualizar_producto(nombre_producto, descripcion, precio, existencias)

            raise web.seeother('/')
        except Exception as e:
            print(f"Error: {e}")
            return "Lo siento, algo salió mal."

class Borrar:
    def GET(self):
        try:
            nombre_producto = web.input().get('nombre')

            producto = m_index.obtener_producto_por_nombre(nombre_producto)
            
            if producto:
                return render.borrar(producto=producto)
            else:
                return "Producto no encontrado."
        except Exception as e:
            print(f"Error: {e}")
            return "Lo siento, algo salió mal."
        
    def POST(self):
        try:
            data = web.input(nombre=None)
            nombre_producto = data.get('nombre')

            if not nombre_producto:
                return "Debe proporcionar el nombre del producto a borrar."

            # Verificar si el producto existe antes de intentar borrarlo
            producto = m_index.obtener_producto_por_nombre(nombre_producto)
            if not producto:
                return "El producto no existe en la base de datos."

            # Borrar el producto
            m_index.borrar_producto(nombre_producto)
            raise web.seeother('/')

        except Exception as e:
            print(f"Error: {e}")
            return "Lo siento, algo salió mal."
