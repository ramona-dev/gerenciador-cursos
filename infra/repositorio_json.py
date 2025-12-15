import json
from modelos.classes import curso
from modelos.classes.curso import Curso

class RepositorioCursoJSON:
    def __init__(self, caminho="data/cursos.json"):
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

    def salvar(self, curso: Curso):
        dados = self._carregar()
        dados[curso.codigo] = {
            "codigo": curso.codigo,
            "nome": curso._Curso__nome,
            "carga_horaria": curso.carga_horaria,
            "pre_requisitos": curso.pre_requisitos
        }
        self._salvar(dados)

    def buscar(self, codigo):
        dados = self._carregar()
        if codigo not in dados:
            return None
        d = dados[codigo]
        return Curso(d["codigo"], d["nome"], d["carga_horaria"], d["pre_requisitos"])
