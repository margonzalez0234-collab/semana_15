import tkinter as tk
from pathlib import Path
from tkinter import ttk

class LoginView(tk.Frame):
    def __init__(self,master, restaurante_servicio, al_iniciar_sesion):
        super().__init__(master, bg="#eef3f8")
        self.restaurante_servicio = restaurante_servicio
        self.al_iniciar_sesion = al_iniciar_sesion

        self.usuario_entry = None
        self.contrasena_entry = None
        self.mensaje_error = None
        self.logo = None

        self.definir_estilo()
        self.construir_interfaz()

    def definir_estilo(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure(
            "Login.TButton",
            background="#2563eb",
            foreground="#ffffff",
            font=("Arial", 12, "bold"),
            padding=(14, 8),
            borderwidth=0,
        )
        estilo.map("Login.TButton", background=[("active", "#1e40af")])
    def cargar_logo(self):
        ruta_base = Path(__file__).resolve().parent.parent
        ruta_logo = ruta_base / "assets" / "logo" / "logo.png"

        if not ruta_logo.exists():
            return None

        logo_original = tk.PhotoImage(file=str(ruta_logo))
        self.logo = logo_original.subsample(1, 1)
        return self.logo
    
    def construir_interfaz(self):
        contenedor = tk.Frame(self, bg="#eef3f8", padx=32, pady=28)
        contenedor.place(relx=0.5, rely=0.5, anchor="center")

        logo = self.cargar_logo()
        if logo is not None:
            tk.Label(
                contenedor,
                imagen=logo,
                bg="#ffffff",
            ).pack(pady=(0, 12))

        titulo = tk.Label(
            contenedor,
            text="Restaurante",
            bg="#eef3f8",
            fg="#2563eb",
            font=("Arial", 22, "bold"),
        )
        titulo.pack(pady=(0, 6))

        subtitulo = tk.Label(
            contenedor,
            text="Iniciar sesión",
            bg="#eef3f8",
            fg="#2563eb",
            font=("Arial", 12),
        )
        subtitulo.pack(pady=(0, 22))

        tk.Label(
            contenedor,
            text="Usuario",
            bg="#eef3f8",
            fg="#2563eb",
            font=("Arial", 12, "bold"),
        ).pack(anchor="w")

        self.usuario_entry = ttk.Entry(contenedor, width=30, font=("Arial", 12))
        self.usuario_entry.pack(pady=(4, 14), ipady=4)
        self.usuario_entry.focus()

        tk.Label(
            contenedor,
            text="Contraseña",
            bg="#eef3f8",
            fg="#2563eb",
            font=("Arial", 12, "bold"),
        ).pack(anchor="w")

        self.contrasena_entry = tk.Entry(
            contenedor,
            width=30,
            font=("Arial", 12),
            show="*",
        )
        self.contrasena_entry.pack(pady=(4, 14), ipady=4)
        
        self.mensaje_error = tk.Label(
            contenedor,
            text="",
            bg="#eef3f8",
            fg="#ff0000",
            font=("Arial", 10),
        )
        self.mensaje_error.pack(pady=(0, 14))

        boton = ttk.Button(
            contenedor,
            text="Iniciar sesión",
            command=self.iniciar_sesion,
            style="Login.TButton",
        )
        boton.pack(fill="x")

    def iniciar_sesion(self):
        assert self.usuario_entry is not None
        assert self.contrasena_entry is not None
        assert self.mensaje_error is not None

        usuario = self.usuario_entry.get().strip()
        contrasena = self.contrasena_entry.get().strip()

        if not usuario or not contrasena:
            self.mensaje_error.config(text="Ingrese usuario y contrasena.")
            return

        usuario_validado = self.restaurante_servicio.validar_acceso(usuario, contrasena)

        if usuario_validado is None:
            self.mensaje_error.config(text="Credenciales incorrectas.")
            return

        self.mensaje_error.config(text="")
        self.al_iniciar_sesion(usuario_validado)