from .oferta import Oferta

def parse_horario(h: str):
    # "10:00-12:00" -> (600, 720) em minutos
    ini, fim = h.split("-")
    ih, im = map(int, ini.split(":"))
    fh, fm = map(int, fim.split(":"))
    return ih * 60 + im, fh * 60 + fm

class Turma(Oferta):
    def __init__(self, curso, id_turma: str, semestre: str, dias_horarios: dict, vagas: int, local: str = ""):
        super().__init__(semestre, vagas, local)  # herda de Oferta
        self._curso = curso
        self._id = id_turma
        # horários comparáveis: {"ter": [(ini,fim)], "qui": [(ini,fim)]}
        self._horarios = {dia: [parse_horario(val)] if isinstance(val, str) else [parse_horario(v) for v in val]
                          for dia, val in (dias_horarios or {}).items()}
        self._matriculas = {}

    @property
    def curso(self): return self._curso
    @property
    def id(self): return self._id
    @property
    def horarios(self): return {d: list(v) for d, v in self._horarios.items()}

    def __len__(self):
        # Retorna quantidade de matrículas ativas
        return sum(1 for m in self._matriculas.values() if m.ativa)

    def tem_choque(self, outra_turma):
        for dia, intervalos in self._horarios.items():
            if dia in outra_turma._horarios:
                for (ini, fim) in intervalos:
                    for (ini2, fim2) in outra_turma._horarios[dia]:
                        if not (fim <= ini2 or fim2 <= ini):  # sobreposição
                            return True
        return False