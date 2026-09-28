class Venta: 

    def __init__(self, identificador, usuario, producto, fecha):
        self.identificador = identificador
        self.usuario = usuario
        self.producto = producto
        self.fecha = fecha

    @staticmethod
    def validar_texto(valor, campo):
        if not valor or not valor.strip():
            raise ValueError(f"el campo {campo} no puede estar vacio.")
        return valor.strip()

    @property
    def identificador(self):
        return self._identificador

    @identificador.setter
    def identificador(self, valor):
        self._identificador = self.validar_texto(valor, "identificador")

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, valor):
        self._usuario= self.validar_texto(valor, "usuario")

    @property
    def producto(self):
        return self._producto

    @producto.setter
    def producto(self, valor):
        self._producto = self.validar_texto(valor, "producto")

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        self._fecha = self.validar_texto(valor, "fecha")