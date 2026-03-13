import csv
import os

# --- CLASE REQUERIDA (4 puntos) ---
class Animal:
    def __init__(self, nombre, caracteristicas, id_clase):
        self.nombre = nombre
        self.caracteristicas = caracteristicas  
        self.id_clase = id_clase

    def __str__(self):
        return f"Animal: {self.nombre.capitalize()} (ID Clase: {self.id_clase})"

    def __repr__(self):
        return f"Animal('{self.nombre}', {self.caracteristicas}, '{self.id_clase}')"

# --- FUNCIONES DE ARCHIVOS (2 puntos c/u) ---
def cargar_csv(ruta_archivo, clave_principal):
    """Carga el contenido de un archivo CSV en un diccionario."""
    diccionario = {}
    if not os.path.exists(ruta_archivo):
        return diccionario
    
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            clave = fila.get(clave_principal)
            diccionario[clave] = fila
    return diccionario

def guardar_csv(ruta_archivo, diccionario, campos):
    """Escribe los datos del diccionario de vuelta al archivo CSV."""
    with open(ruta_archivo, mode='w', encoding='utf-8', newline='') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for clave, fila in diccionario.items():
            escritor.writerow(fila)

# --- FUNCIONES DE LÓGICA (2 y 3 puntos) ---
def listar_por_clase(dic_animales, id_clase):
    """Lista animales filtrando por su clase."""
    resultados = []
    for nombre, datos in dic_animales.items():
        if datos['clase'] == str(id_clase):
            resultados.append(nombre)
    return resultados

def listar_por_caracteristica(dic_animales, caracteristica):
    """Lista animales filtrando por una característica que sea verdadera ('1')."""
    resultados = []
    for nombre, datos in dic_animales.items():
        if datos.get(caracteristica) == '1':
            resultados.append(nombre)
    return resultados

def agregar_animal(dic_animales, animal_obj):
    """Agrega un objeto Animal al diccionario general de animales."""
    nueva_fila = {'nombre_animal': animal_obj.nombre, 'clase': animal_obj.id_clase}
    nueva_fila.update(animal_obj.caracteristicas)
    dic_animales[animal_obj.nombre] = nueva_fila
    return dic_animales