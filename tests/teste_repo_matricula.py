from infra.repositorio_matricula_json import RepositorioMatriculaJSON
from infra.repositorio_aluno_json import RepositorioAlunoJSON
from infra.repositorio_turma_json import RepositorioTurmaJSON
from infra.repositorio_json import RepositorioCursoJSON
from  modelos.classes.curso import Curso
from modelos.classes.turma import Turma
from modelos.classes.aluno import Aluno
from modelos.classes.matricula import Matricula
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from infra.repositorio_matricula_json import RepositorioMatriculaJSON

def teste_matricula():
    # Criar repositórios
    repo_curso = RepositorioCursoJSON("data/cursos.json")
    repo_aluno = RepositorioAlunoJSON("data/alunos.json")
    repo_turma = RepositorioTurmaJSON("data/turmas.json")
    repo_matricula = RepositorioMatriculaJSON("data/matriculas.json")

    # Seed: curso
    curso = Curso("CSI001", "Algoritmos", 60)
    repo_curso.salvar(curso)

    # Seed: turma
    horario = {"ter": ["10:00", "12:00"], "qui": ["10:00", "12:00"]}
    turma = Turma("T2025_1", curso, "2025.1", horario, 30)
    repo_turma.salvar(turma)

    # Seed: aluno
    aluno = Aluno("2025001", "Tristan Biwo", "tristan@example.com")
    repo_aluno.salvar(aluno)

    # Criar matrícula
    matricula = Matricula(aluno, turma)
    matricula._Matricula__nota = 8.5
    matricula._Matricula__frequencia = 90
    repo_matricula.salvar(matricula)

    # Buscar e imprimir
    m = repo_matricula.buscar("2025001", "T2025_1")
    print(f"Aluno: {m.aluno.nome}, Turma: {m.turma._Turma__id}, Nota: {m._Matricula__nota}, Frequencia: {m._Matricula__frequencia}")

if __name__ == "__main__":
    teste_matricula()
