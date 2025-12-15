import sys
from pathlib import Path

# Adicionar o diretório pai ao sys.path para importar modelos
sys.path.insert(0, str(Path(__file__).parent.parent))
from datetime import date
from modelos.classes.aluno import Aluno
from modelos.classes.configuracoes import Configuracoes
from modelos.classes.curso import Curso
from modelos.classes.pessoa import Pessoa 
from modelos.classes.turma import Turma
from modelos.classes.matricula import Matricula
from modelos.classes.oferta import Oferta

if __name__ == "__main__":
    ()

# cli.py
class SistemaAcademicoCLI:
    def __init__(self):
        self.alunos = {}
        self.cursos = {}
        self.turmas = {}
        self.config = Configuracoes(nota_minima=6.0, frequencia_minima=75.0, top_n_alunos=3, limite_turmas=10)

    def iniciar(self):
        while True:
            print("\n=== SISTEMA ACADÊMICO ===")
            print("1 - Cadastrar aluno")
            print("2 - Listar alunos")
            print("3 - Criar curso")
            print("4 - Criar turma")
            print("5 - Sair")

            op = input("Escolha uma opção: ")

            if op == "1":
                self.menu_cadastrar_aluno()
            elif op == "2":
                self.menu_listar_alunos()
            elif op == "3":
                self.menu_criar_curso()
            elif op == "4":
                self.menu_criar_turma()
            elif op == "5":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")

    # ----------------
    # Menus específicos
    # ----------------

    def menu_cadastrar_aluno(self):
        print("\n--- Cadastro de Aluno ---")
        nome = input("Nome: ")
        matricula = input("Matrícula: ")
        email = input("Email: ")

        aluno = Aluno(matricula=matricula, nome=nome, email=email)

        if not aluno.validar_cadastro():
            print("Cadastro inválido.")
            return

        self.alunos[matricula] = aluno
        print("Aluno cadastrado com sucesso!")

    def menu_listar_alunos(self):
        print("\n--- Lista de Alunos ---")
        if not self.alunos:
            print("Nenhum aluno registrado.")
            return

        for m, a in self.alunos.items():
            print(f"{m} - {a.nome}")

    def menu_criar_curso(self):
        print("\n--- Criar Curso ---")
        codigo = input("Código do curso: ")
        nome = input("Nome do curso: ")
        carga = int(input("Carga horária: "))

        curso = Curso(codigo_curso=codigo, nome=nome, carga_horaria=carga)
        self.cursos[codigo] = curso
        print("Curso criado com sucesso!")

    def menu_criar_turma(self):
        print("\n--- Criar Turma ---")
        id_turma = input("ID da turma: ")
        codigo_curso = input("Código do curso: ")

        if codigo_curso not in self.cursos:
            print("Curso não encontrado.")
            return

        periodo = input("Período (ex: 2025.1): ")
        
        # Estrutura de horário vazia por enquanto
        horario = {"dia": "A definir", "hora": "A definir"}
        
        sala = input("Sala: ")
        capacidade = int(input("Capacidade: "))

        turma = Turma(
            id_turma=id_turma,
            codigo_curso=codigo_curso,
            periodo=periodo,
            horario=horario,
            sala=sala,
            capacidade=capacidade
        )

        self.turmas[id_turma] = turma
        print("Turma criada com sucesso!")



if __name__ == "__main__":
    sistema = SistemaAcademicoCLI()
    sistema.iniciar()
