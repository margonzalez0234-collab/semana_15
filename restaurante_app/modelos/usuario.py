class Usuario:
    def __init__(self, nombre, identificacion, usuario, contrasena):
        self.nombre = nombre
        self.identificacion = identificacion
        self.usuario = usuario
        self.contrasena = contrasena

    @staticmethod
    def validar_texto(valor, campo):
        if not valor or not valor.strip():
            raise ValueError(f"El campo '{campo}' no puede estar vacío.")
        return valor.strip()

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = self.validar_texto(value, "nombre")

    @property
    def identificacion(self):
        return self._identificacion

    @identificacion.setter
    def identificacion(self, value):
        self._identificacion = self.validar_texto(value, "identificacion")

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, value):
        self._usuario = self.validar_texto(value, "usuario")

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, value):
        self._contrasena = self.validar_texto(value, "contrasena")