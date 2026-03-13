# Proyecto: zoologico

**Autor:** Zaid Montaño Martinez
**Materia:** Desarrollo 4

## Descripción del Proyecto
Este programa es un sistema de gestión para un zoológico desarrollado en Python. Permite cargar información de animales y sus clasificaciones desde archivos CSV (`zoo.csv` y `clases.csv`), consultar datos mediante filtros específicos y registrar nuevas especies. El programa está diseñado usando Programación Orientada a Objetos (POO) y divide su lógica en funciones modulares.

## Estructura de Archivos
- `main.py`: Archivo principal que ejecuta la lógica del menú interactivo.
- `auxiliares.py`: Módulo que contiene las funciones de procesamiento (lectura/escritura de CSV, filtrado) y la clase `Animal`.
- `zoo.csv`: Base de datos de los animales y sus características.
- `clases.csv`: Base de datos de las clasificaciones biológicas.

## Requisitos
- Python 3.x instalado en el sistema.
- Visual Studio Code (opcional pero recomendado para ejecutar fácilmente).

## Instrucciones: ¿Cómo iniciar el programa?
Puedes arrancar el programa de tres formas diferentes:

**Opción 1: Desde la Terminal (Recomendado)**
1. Abre la terminal integrada de Visual Studio Code.
2. Asegúrate de estar en la carpeta `zoologico` (ruta: `.../desarrollo4/zoologico>`).
3. Escribe el comando: `python main.py` y presiona `Enter`.

**Opción 2: Usando el teclado en Visual Studio Code**
1. Abre el archivo `main.py` para que esté activo en tu pantalla.
2. Presiona la tecla `F5` (o `Ctrl` + `F5`). 
3. *Nota: Si te aparece un menú emergente, selecciona "Python File".*

**Opción 3: Usando el botón de "Play"**
1. Abre el archivo `main.py`.
2. Haz clic en el botón de reproducción (▷) ubicado en la esquina superior derecha de la ventana de Visual Studio Code.

## Instrucciones: ¿Cómo interactuar con el programa?
Una vez iniciado el programa, verás un menú principal en la consola/terminal. Para interactuar, debes escribir el **número** de la opción deseada y presionar `Enter`.

Las opciones disponibles son:
1. **Listar por clase:** Te pedirá que ingreses el ID de una clasificación (ej. 1 para Mamífero) y mostrará todos los animales que pertenecen a ella.
2. **Listar por característica:** Te pedirá que escribas el nombre de una característica (ej. `plumas`, `vuela`, `venenoso`) y mostrará todos los animales que cumplan con esa condición.
3. **Agregar nuevo animal:** El sistema te irá haciendo preguntas paso a paso para ingresar el nombre, la clase y cada una de las características (contestando con 1 para Sí y 0 para No).
4. **Salir y Guardar:** Termina la ejecución del programa y guarda automáticamente cualquier animal nuevo que hayas agregado directamente en el archivo `zoo.csv`.

