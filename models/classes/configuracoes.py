import json
from datetime import date

class Configuracoes:
    def __init__(self,
        nota_minima: float,
        frequencia_minima: float,
        top_n_alunos: int,
        limite_turmas: int,
        data_limite_trancamento: str):
        
        self.nota_minima = nota_minima
        self.frequencia_minima = frequencia_minima
        self.top_n_alunos = top_n_alunos
        self.limite_turmas = limite_turmas
        self.data_limite_trancamento = date.fromisoformat(data_limite_trancamento)

    @classmethod
    def carregar(cls, caminho="settings.json"):
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)

        return cls(
            nota_minima=dados["nota_minima_aprovacao"],
            frequencia_minima=dados["frequencia_minima"],
            top_n_alunos=dados["top_n_alunos"],
            limite_turmas=dados["max_turmas_por_aluno"],
            data_limite_trancamento=dados["data_limite_trancamento"],
        )
