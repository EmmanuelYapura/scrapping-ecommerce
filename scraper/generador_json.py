import json

def guardar_json(productos, nombre_archivo='productos.json'):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(productos, archivo, ensure_ascii=False, indent=4)
