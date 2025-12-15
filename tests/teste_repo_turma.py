from infra.repositorio_turma_json import RepositorioTurmaJSON
from infra.repositorio_json import RepositorioCursoJSON
from modelos.classes.curso import Curso
from modelos.classes.turma import Turma

def teste_turma():
    # Criar repositórios
    repo_curso = RepositorioCursoJSON("data/cursos.json")
    repo_turma = RepositorioTurmaJSON("data/turmas.json")

    # Criar curso seed
    curso_seed = Curso("CSI001", "Algoritmos", 60)
    repo_curso.salvar(curso_seed)

    # Criar turma associada
    horario = {
        "ter": ["10:00", "12:00"],
        "qui": ["10:00", "12:00"]
    }
    turma = Turma(
        id_turma="T2025_1",
        curso=curso_seed,
        periodo="2025.1",
        horario=horario,
        capacidade=30
    )
    repo_turma.salvar(turma)

    # Buscar e imprimir turma
    t = repo_turma.buscar("T2025_1")
    print(f"Turma {t._Turma__id} - Curso: {t._Turma__curso.nome}, Vagas: {t._Turma__capacidade}")

if __name__ == "__main__":
    teste_turma()
