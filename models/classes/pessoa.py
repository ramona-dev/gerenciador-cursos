class Pessoa:
    def __init__(self, nome: str, matricula: str):
        self.__nome = nome
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome

    @property
    def matricula(self):
        return self.__matricula

    def validar_cadastro(self):
        return bool(self.__nome and self.__matricula)
