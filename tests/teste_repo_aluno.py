# tests/teste_repo_aluno.py
from infra.repositorio_aluno_json import RepositorioAlunoJSON
from modelos.classes.aluno import Aluno

def teste_aluno():
    repo = RepositorioAlunoJSON("data/alunos.json")
    aluno = Aluno("2025001", "Tristan Biwo", "tristan@example.com")
    repo.salvar(aluno)
    a = repo.buscar("2025001")
    print(a.nome, a.email)

if __name__ == "__main__":
    teste_aluno()
