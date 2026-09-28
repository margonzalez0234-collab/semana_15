# 🍽️ restaurante_app

Aplicación de gestión para un restaurante desarrollada en **Python** con **Tkinter/ttk**, aplicando conceptos de **Programación Orientada a Objetos**, arquitectura modular, persistencia mediante archivos **JSON** y manejo básico de eventos.

## 📌 Descripción

`restaurante_app` es una aplicación gráfica que permite gestionar información relacionada con **usuarios, productos y ventas**.

El proyecto mantiene una separación de responsabilidades entre los modelos, los servicios, la interfaz gráfica y los archivos de datos. En esta versión se incorporó el módulo de **Ventas**, utilizando un botón asociado mediante `command=` a un callback que coordina el registro de una venta.

La aplicación permite seleccionar un usuario y un producto, registrar la operación y almacenar la información en `ventas.json`.

## 🎯 Objetivo

El objetivo principal es demostrar el funcionamiento básico del **manejo de eventos en una interfaz gráfica**, siguiendo el flujo:

```text
Acción del usuario
        ↓
Botón / componente
        ↓
command=
        ↓
Callback
        ↓
RestauranteServicio
        ↓
Persistencia JSON
        ↓
Actualización de la interfaz
```

De esta manera, la interfaz se encarga de recibir las acciones del usuario, mientras que las reglas de negocio y la persistencia permanecen en la capa de servicios.

## 🛠️ Tecnologías utilizadas

* Python
* Tkinter / ttk
* Programación Orientada a Objetos
* Archivos JSON
* Arquitectura modular
* Treeview
* `command=` y callbacks

## 📂 Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── assets/
│   └── recursos visuales
│
├── main.py
└── README.md
```

## ⚙️ Funcionamiento

### 🔐 Inicio de sesión

La aplicación inicia mediante `main.py` y presenta la interfaz de inicio de sesión. Las validaciones correspondientes son gestionadas mediante los servicios del sistema.

### 🖥️ Interfaz principal

Después de iniciar sesión, el usuario accede a la ventana principal, desde donde puede navegar por las diferentes secciones de la aplicación.

Entre las funcionalidades se encuentran:

* Consulta de usuarios.
* Gestión de productos.
* Registro de ventas.
* Visualización de ventas registradas.

### 💰 Registro de ventas

El módulo de ventas permite relacionar:

* Un **usuario** existente.
* Un **producto** existente.
* La **fecha** de la operación.

El usuario selecciona los datos correspondientes y presiona el botón **Registrar venta**.

El botón utiliza `command=` para ejecutar el callback encargado de procesar la operación.

```text
Usuario selecciona los datos
        ↓
Registrar venta
        ↓
Callback
        ↓
RestauranteServicio
        ↓
Validación
        ↓
ventas.json
        ↓
Actualización de la tabla
```

### 💾 Persistencia

Las ventas registradas se almacenan en:

```text
datos/ventas.json
```

Esto permite conservar la información aunque la aplicación sea cerrada y posteriormente ejecutada nuevamente.

## 🧩 Manejo de eventos

Uno de los elementos principales implementados en esta versión es el manejo de eventos mediante `command=`.

El botón de registro de ventas genera una acción que ejecuta un callback. Este callback obtiene la información seleccionada en la interfaz y delega la operación al servicio correspondiente.

Esto permite mantener separadas las responsabilidades y evita colocar toda la lógica del sistema directamente dentro de la interfaz gráfica.

### Flujo del evento

```text
USUARIO
   ↓
Realiza una acción
   ↓
BOTÓN
   ↓
command=
   ↓
CALLBACK
   ↓
RestauranteServicio
   ↓
PERSISTENCIA
   ↓
RESPUESTA VISUAL
```

## 🗃️ Modelos principales

### Producto

Representa los productos disponibles dentro del restaurante.

### Usuario

Representa a los usuarios registrados en el sistema.

### Venta

Representa una operación de venta y establece la relación entre un usuario, un producto y la fecha de la operación.

## 🔧 Servicios

### `ArchivoServicio`

Se encarga de las operaciones relacionadas con la lectura y escritura de información persistida en archivos JSON.

### `RestauranteServicio`

Contiene las operaciones y validaciones relacionadas con la lógica del restaurante, incluyendo el registro de ventas.

Esta separación permite mantener la interfaz organizada y evita que los archivos JSON sean manipulados directamente desde las vistas.

## 🎨 Interfaz gráfica

La aplicación utiliza **Tkinter/ttk** para construir la interfaz.

La información de las ventas se presenta mediante una tabla o componente equivalente, permitiendo visualizar las operaciones registradas.

El proyecto también utiliza la carpeta:

```text
assets/
```

para almacenar recursos visuales como el logo, logotipo e íconos utilizados por la interfaz.

## ▶️ Ejecución

Para ejecutar el proyecto se debe contar con **Python 3** instalado.

Desde la carpeta principal del proyecto:

```bash
python main.py
```

En algunos sistemas también puede utilizarse:

```bash
python3 main.py
```

## ✅ Funcionalidades implementadas

* Inicio de sesión.
* Navegación por la aplicación.
* Consulta de usuarios.
* Gestión de productos.
* Registro de ventas.
* Selección de usuario y producto.
* Manejo de eventos mediante `command=`.
* Uso de callbacks.
* Validación mediante `RestauranteServicio`.
* Persistencia de ventas en `ventas.json`.
* Visualización de ventas en la interfaz.
* Recuperación de información almacenada al iniciar nuevamente la aplicación.
* Uso de recursos gráficos mediante `assets/`.
* Arquitectura modular y orientada a objetos.

## 📋 Resultado

La implementación permite demostrar cómo una acción realizada por el usuario dentro de una aplicación gráfica puede desencadenar una serie de operaciones coordinadas entre la interfaz, los callbacks, los servicios y la persistencia de datos.

El módulo de ventas representa la evolución del proyecto `restaurante_app`, manteniendo la arquitectura desarrollada previamente y agregando una nueva funcionalidad sin reconstruir completamente la aplicación.

## 👨‍💻 Proyecto académico

**Asignatura:** Programación Orientada a Objetos
**Actividad:** Semana 15 – Conceptos fundamentales de manejo de eventos
**Proyecto:** `restaurante_app`

---

Desarrollado como parte de las actividades académicas de Programación Orientada a Objetos.
