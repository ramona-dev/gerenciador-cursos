class Curso:
    def __init__(self, codigo_curso: str, nome: str, carga_horaria: int, lista_requisitos=None, disciplinas=None):
        self.__codigo_curso = codigo_curso
        self.__nome = nome
        self.__carga_horaria = carga_horaria
        self.__lista_requisitos = lista_requisitos or []
        self.__disciplinas = disciplinas or []

    @property
    def codigo(self):
        return self.__codigo_curso

    def calcular_carga_horaria(self):
        return self.__carga_horaria

    def impedir_ciclos(self, outro_curso):
        if outro_curso.codigo == self.__codigo_curso:
            raise ValueError("Um curso não pode ser pré-requisito de si mesmo.")

    def __str__(self):
        return f"Curso {self.__codigo_curso} - {self.__nome} ({self.__carga_horaria}h)"
