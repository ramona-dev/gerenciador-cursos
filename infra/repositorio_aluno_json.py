import json
from modelos.classes.aluno import Aluno

class RepositorioAlunoJSON:
    def __init__(self, caminho="data/alunos.json"):
        self.caminho = caminho

    def _carregar(self):
        try:
            with open(self.caminho, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def _salvar(self, dados):
        with open(self.caminho, "w") as f:
            json.dump(dados, f, indent=2)

    def salvar(self, aluno: Aluno):
        dados = self._carregar()
        dados[aluno.matricula] = {
            "matricula": aluno.matricula,
            "nome": aluno.nome,
            "email": aluno.email,
            "historico": aluno.historico()  # lista de disciplinas cursadas
        }
        self._salvar(dados)

    def buscar(self, matricula):
        dados = self._carregar()
        if matricula not in dados:
            return None
        d = dados[matricula]
        aluno = Aluno(d["matricula"], d["nome"], d["email"])
        for disc in d.get("historico", []):
            aluno.adicionar_disciplina(
                curso=disc["curso"], 
                nota=disc["nota"], 
                frequencia=disc["frequencia"]
            )
        return aluno

    def listar(self):
        dados = self._carregar()
        return [self.buscar(m) for m in dados]
