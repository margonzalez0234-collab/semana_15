class Producto:
        def __init__(self, nombre, precio, descripcion):
            self.nombre = nombre
            self.precio = precio
            self.descripcion = descripcion

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
        def precio(self):
            return self._precio

        @precio.setter
        def precio(self, valor):
            try:
                valor_float= float(valor)
                if valor_float <0:
                 self._precio = valor_float
            except (ValueError, TypeError):
                raise ValueError("El precio debe ser un numero valido.")

        @property
        def descripcion(self):
            return self._descripcion

        @descripcion.setter
        def descripcion(self, valor):
            self._descripcion = self.validar_texto(valor, "descripcion")