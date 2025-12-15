import json
from modelos.classes.matricula import Matricula
from infra.repositorio_aluno_json import RepositorioAlunoJSON
from infra.repositorio_turma_json import RepositorioTurmaJSON
from infra.repositorio_json import RepositorioCursoJSON
class RepositorioMatriculaJSON:
    def __init__(self, caminho="data/matriculas.json"):
        self.caminho = caminho
        self.repo_aluno = RepositorioAlunoJSON()
        self.repo_turma = RepositorioTurmaJSON()

    def _carregar(self):
        try:
            with open(self.caminho, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def _salvar(self, dados):
        with open(self.caminho, "w") as f:
            json.dump(dados, f, indent=2)

    def salvar(self, matricula: Matricula):
        dados = self._carregar()
        key = f"{matricula.aluno.matricula}_{matricula.turma._Turma__id}"
        dados[key] = {
            "aluno": matricula.aluno.matricula,
            "turma": matricula.turma._Turma__id,
            "nota": matricula._Matricula__nota,
            "frequencia": matricula._Matricula__frequencia,
            "ativa": matricula._Matricula__ativa
        }
        self._salvar(dados)

    def buscar(self, aluno_matricula, turma_id):
        dados = self._carregar()
        key = f"{aluno_matricula}_{turma_id}"
        if key not in dados:
            return None
        d = dados[key]
        aluno = self.repo_aluno.buscar(d["aluno"])
        turma = self.repo_turma.buscar(d["turma"])
        matricula = Matricula(aluno, turma)
        matricula._Matricula__nota = d["nota"]
        matricula._Matricula__frequencia = d["frequencia"]
        matricula._Matricula__ativa = d["ativa"]
        return matricula

    def listar(self):
        dados = self._carregar()
        matriculas = []
        for key, d in dados.items():
            matricula = self.buscar(d["aluno"], d["turma"])
            matriculas.append(matricula)
        return matriculas
