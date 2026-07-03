class Validators:

    @staticmethod
    def validar_status_code(response, esperado):
        assert response.status_code == esperado, (
            f"Status code esperado: {esperado}."
            f"Obtenido: {response.status_code}"
        )

    @staticmethod
    def validar_campo_igual(campo, esperado, obtenido):
        assert obtenido == esperado, (
            f"{campo} esperado: {esperado}. "
            f"Obtenido: {obtenido}"
        )

    @staticmethod
    def validar_campo_no_vacio(campo, valor):
        assert valor is not None and valor != "", (
            f"El campo {campo} está vacío o no existe"
        )