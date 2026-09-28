from datetime import date

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class RestauranteServicio:
    def __init__(self, archivo_servicio):
        self.archivo_servicio = archivo_servicio
        self.usuarios =[]
        self.productos = []
        self.cargar_datos()

    def cargar_datos(self):
        usuarios_json = self.archivo_servicio.leer_json("usuarios.json")
        productos_json = self.archivo_servicio.leer_json("productos.json")
        ventas_json = self.archivo_servicio.leer_json("ventas.json")
        self.usuarios = [
            Usuario(
                datos.get("nombre", ""),
                datos.get("identificacion", ""),
                datos.get("usuario", ""),
                datos.get("contraseña", datos.get("contrasena", "")),
            )
            for datos in usuarios_json
        ]

        self.productos = [
            Producto(
                datos.get("nombre", ""),
                datos.get("precio", 0.0),
                datos.get("descripcion", "")
            )
            for datos in productos_json
        ]

        self.ventas = [
            Venta(
                datos.get("identificador", ""),
                datos.get("usuario", ""),
                datos.get("producto", ""),
                datos.get("fecha", ""),
            )
            for datos in ventas_json
        ]
    def validar_acceso(self, usuario, contrasena):
        for usuario_registrado in self.usuarios:
            if (
                usuario_registrado.usuario == usuario
                and usuario_registrado.contrasena == contrasena
            ):
                return usuario_registrado
        return None

    def cantidad_usuarios(self):
        return len(self.usuarios)

    def cantidad_productos(self):
        return len(self.productos)

    def cantidad_ventas(self):
        return len(self.ventas)

    def listar_usuarios(self):
        return self.usuarios

    def listar_productos(self):
        return self.productos

    def listar_ventas(self):
        return self.ventas

    def guardar_productos(self):
        datos = [
            {
                "nombre": producto.nombre,
                "precio": producto.precio,
                "descripcion": producto.descripcion,

            }
            for producto in self.productos
        ]
        self.archivo_servicio.escribir_json("productos.json", datos)

    def buscar_producto_por_nombre(self, nombre):
        nombre = nombre.strip()
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto

        return None

    def buscar_usuario_por_identificador(self, identificador):
        identificador = identificador.strip()
        for usuario in self.usuarios:
            if usuario.identificador == identificador:
                return usuario
        return None

    def generar_identificador_venta(self):
        siguiente = len(self.ventas) + 1
        return f"V{siguiente:03d}"


    def registrar_producto(self, nombre, precio, descripcion):
        nuevo_producto= Producto(nombre, precio, descripcion)

        if self.buscar_producto_por_nombre(nuevo_producto.nombre) is not None:
            raise ValueError("Ya existe in producto con ese nombre.")


        self.productos.append(nuevo_producto)
        self.guardar_productos()
        return nuevo_producto

    def actualizar_producto(self, nombre, precio, descripcion):
        producto_actual = self.buscar_producto_por_nombre(nombre)

        if producto_actual is None:
            raise ValueError("No existe un producto con ese nombre.")

        datos_validados = Producto(nombre, precio, descripcion)
        producto_actual.nombre= datos_validados.nombre
        producto_actual.precio= datos_validados.precio
        producto_actual.descripcion= datos_validados.descripcion
        self.guardar_productos()
        return producto_actual

    def eliminar_producto(self, nombre):
        producto_actual = self.buscar_producto_por_nombre(nombre)

        if producto_actual is None:
            raise ValueError("No existe un producto con ese nombre.")

        self.productos.remove(producto_actual)
        self.guardar_productos()
        return producto_actual

    def guardar_ventas(self):
        datos = [
            {
                "identificador": venta.identificador,
                "usuario": venta.usuario,
                "producto": venta.producto,
                "fecha": venta.fecha,
            }
            for venta in self.ventas
        ]
        self.archivo_servicio.escribir_json("ventas.json", datos)

    def registrar_venta(self, usuario, producto):
        usuario = usuario.strip()
        producto = producto.strip()

        if not usuario:
            raise ValueError("Debe seleccionar un usuario.")
        if not producto:
            raise ValueError("Debe seleccionar un producto.")
        if self.buscar_usuario_por_identificador(usuario) is None:
            raise ValueError("El usuario seleccionado no existe.")
        if self.buscar_producto_por_nombre(producto) is None:
            raise ValueError("El productoseleccionado no existe.")

        nueva_venta = Venta(
            self.generar_identificador_venta(),
            usuario,
            producto,
            date.today().isoformat(),
        )
        self.ventas.append(nueva_venta)
        self.guardar_ventas()
        return nueva_venta
