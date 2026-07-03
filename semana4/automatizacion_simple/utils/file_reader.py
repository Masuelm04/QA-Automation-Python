import json

class FileReader:

    @staticmethod
    def read_json(ruta_archivo):
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
