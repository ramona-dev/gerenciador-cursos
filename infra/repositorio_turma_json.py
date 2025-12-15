import json
from modelos.classes.turma import Turma
from modelos.classes.curso import Curso
from infra.repositorio_json import RepositorioCursoJSON

class RepositorioTurmaJSON:
    def __init__(self, caminho="data/turmas.json"):
        self.caminho = caminho
        self.repo_curso = RepositorioCursoJSON()

    def _carregar(self):
        try:
            with open(self.caminho, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def _salvar(self, dados):
        with open(self.caminho, "w") as f:
            json.dump(dados, f, indent=2)

    def salvar(self, turma: Turma):
        dados = self._carregar()
        dados[turma._Turma__id] = {
            "id": turma._Turma__id,
            "curso": turma._Turma__curso.codigo,
            "periodo": turma._Turma__periodo,
            "horario": turma._Turma__horario,
            "capacidade": turma._Turma__capacidade,
            "aberta": turma.esta_aberta()
        }
        self._salvar(dados)

    def buscar(self, id_turma):
        dados = self._carregar()
        if id_turma not in dados:
            return None
        d = dados[id_turma]
        curso = self.repo_curso.buscar(d["curso"])
        return Turma(
            id_turma=d["id"],
            curso=curso,
            periodo=d["periodo"],
            horario=d["horario"],
            capacidade=d["capacidade"]
        )

    def listar(self):
        dados = self._carregar()
        return [self.buscar(tid) for tid in dados]
