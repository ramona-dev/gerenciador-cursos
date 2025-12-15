from infra.repositorio_json import RepositorioCursoJSON
from modelos.classes.curso import Curso

def teste_repositorio_curso():
    repo = RepositorioCursoJSON("data/cursos.json")

    # Criar curso de teste
    curso = Curso("CSI001", "Algoritmos", 60)
    repo.salvar(curso)

    # Buscar curso salvo
    c = repo.buscar("CSI001")
    print(c)

if __name__ == "__main__":
    teste_repositorio_curso()
