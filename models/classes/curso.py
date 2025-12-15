class Curso:
    def __init__(self, codigo_curso: str, nome: str, carga_horaria: int, lista_requisitos=None, disciplinas=None):
        self.__codigo_curso = codigo_curso
        self.__nome = nome
        self.__carga_horaria = carga_horaria
        self.__pre_requisitos = lista_requisitos or []
        self.__disciplinas = disciplinas or []

    @property
    def pre_requisitos(self):
        return self.__pre_requisitos

    @property
    def codigo(self):
        return self.__codigo_curso
    @property
    def carga_horaria(self):
        return self.__carga_horaria

    def impedir_ciclos(self, codigo_pre):
        if codigo_pre == self.__codigo_curso:
            raise ValueError("Curso não pode ser pré-requisito de si mesmo.")

    def __str__(self):
        return f"Curso {self.__codigo_curso} - {self.__nome} ({self.__carga_horaria}h)"