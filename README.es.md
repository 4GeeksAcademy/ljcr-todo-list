# Lista de Tareas en Python (CLI)

Aplicación de consola para gestionar tareas (TODO) con las funciones básicas:

- Agregar tareas.
- Listar tareas.
- Eliminar tareas.
- Guardar automáticamente en `todos.csv` para no perder datos al cerrar.

## Resumen rápido del proyecto

Este proyecto está hecho en Python y se ejecuta desde terminal.

- Archivo principal: `app.py`
- Persistencia de datos: `todos.csv`
- Interfaz: menú por texto en consola

## Requisitos

- Python 3 instalado

Para comprobar tu instalación:

```bash
python --version
```

Si ese comando no funciona, prueba:

```bash
python3 --version
```

## Cómo usarlo paso a paso

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta la aplicación:

```bash
python app.py
```

Si tu sistema usa `python3`, ejecuta:

```bash
python3 app.py
```

3. Verás el menú principal con estas opciones:
	- `1. Agregar`
	- `2. Listar`
	- `3. Eliminar`
	- `4. Salir`
4. Escribe el número de la opción que quieras usar y presiona `Enter`.

## Ejemplo de uso

1. Selecciona `1` para agregar una tarea.
2. Escribe el texto de la tarea y confirma con `Enter`.
3. Selecciona `2` para listar tareas guardadas.
4. Selecciona `3` y escribe el número de tarea para eliminarla.
5. Selecciona `4` para salir.

## ¿Dónde se guardan las tareas?

Las tareas se guardan en el archivo `todos.csv` dentro de la misma carpeta del proyecto.

- Al iniciar el programa, las tareas se cargan automáticamente.
- Al agregar o eliminar una tarea, se actualiza el archivo automáticamente.

## Errores comunes

- Si intentas agregar una tarea vacía, el programa muestra un error.
- Si intentas eliminar con un número inválido o fuera de rango, el programa lo indica.

## Estructura del proyecto

```text
.
├── app.py
└── README.es.md
```
