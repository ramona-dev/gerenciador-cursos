# main.py

from modulos.aluno import Aluno
from modulos.curso import Curso
from modulos.turma import Turma
from modulos.matricula import Matricula
import settings
from dados import salvar_tudo, carregar_tudo

# carregar dados existentes
dados = carregar_tudo()
alunos, cursos, turmas, matriculas = [], [], [], []

# reconstrução básica
for d in dados.get("alunos", []):
    alunos.append(Aluno(d["matricula"], d["nome"], d["email"]))
    # restaura histórico (se existir)
    for h in d.get("historico", []):
        # histórico guarda codigo do curso, nota, frequência
        # aqui não temos o objeto Curso, então armazenamos via método do Aluno quando lançarmos notas
        pass

for d in dados.get("cursos", []):
    cursos.append(Curso(d["codigo"], d["nome"], d["carga_horaria"], d.get("prerequisitos", [])))

for d in dados.get("turmas", []):
    curso = next((c for c in cursos if c.codigo == d["curso_codigo"]), None)
    if curso:
        turmas.append(Turma(
            curso,
            d.get("id") or d.get("codigo_turma"),  # aceita 'id' ou 'codigo_turma'
            d.get("semestre"),
            d.get("dias_horarios", {}),
            d.get("vagas", 40),
            d.get("local", "")
        ))
        if not d.get("aberta", True):
            turmas[-1].fechar()
            
# Ao reconstruir matrículas, criamos objetos e atribuimos estado/nota/frequência
for d in dados.get("matriculas", []):
    aluno = next((a for a in alunos if a.matricula == d["aluno"]), None)
    turma = next((t for t in turmas if t.id == d["turma"]), None)
    if aluno and turma:
        try:
            m = Matricula(aluno, turma)  # valida e registra no mapa da turma
        except Exception:
            # Se já estava registrada, crie um objeto "fantasma" sem duplicar ligações
            # Ajuste leve: reaproveita referência existente
            # (Se preferir, cheque turma._matriculas.get(aluno))
            m = turma._matriculas.get(aluno)
            if m is None:
                m = Matricula(aluno, turma)
        m.nota = d.get("nota")
        m.frequencia = d.get("frequencia")
        if d.get("ativa") is False:
            # respeita estado de trancamento sem checar data limite
            m._ativa = False
        matriculas.append(m)

def menu():
    while True:
        print("\n=== Sistema Acadêmico ===")
        print("1. Cadastrar aluno")
        print("2. Cadastrar curso")
        print("3. Criar turma")
        print("4. Matricular aluno")
        print("5. Listar alunos")
        print("6. Listar cursos")
        print("7. Listar turmas")
        print("8. Registrar nota/frequência")
        print("9. Mostrar histórico")
        print("10. Relatórios")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                matricula = input("Matrícula: ")
                if any(a.matricula == matricula for a in alunos):
                    raise ValueError("Já existe aluno com essa matrícula.")
                nome = input("Nome do aluno: ")
                email = input("Email: ")
                alunos.append(Aluno(matricula, nome, email))
                salvar_tudo(alunos, cursos, turmas, matriculas)
                print("Aluno cadastrado!")

            elif opcao == "2":
                codigo = input("Código do curso: ")
                if any(c.codigo == codigo for c in cursos):
                    raise ValueError("Já existe curso com esse código.")
                nome = input("Nome do curso: ")
                carga_horaria = int(input("Carga horária: "))
                cursos.append(Curso(codigo, nome, carga_horaria))
                salvar_tudo(alunos, cursos, turmas, matriculas)
                print("Curso cadastrado!")

            elif opcao == "3":
                if not cursos:
                    print("Cadastre um curso antes de criar uma turma.")
                    continue
                print("Cursos disponíveis:")
                for i, c in enumerate(cursos):
                    print(f"{i+1}. {c.nome} ({c.codigo})")
                idx = int(input("Escolha o curso pelo número: ")) - 1
                codigo_turma = input("ID da turma: ")
                semestre = input("Semestre (ex: 2025.2): ")
                # horários como dict: {"ter": "10:00-12:00", "qui": "10:00-12:00"}
                horarios = {}
                print("Informe dias/horários (vazio para parar). Ex: ter 10:00-12:00")
                while True:
                    linha = input("> ")
                    if not linha.strip():
                        break
                    try:
                        dia, intervalo = linha.split()
                        horarios[dia] = intervalo
                    except ValueError:
                        print("Formato inválido. Use: dia HH:MM-HH:MM")
                vagas = int(input("Vagas (padrão 40): ") or 40)
                local = input("Local (opcional): ") or ""
                t = Turma(cursos[idx], codigo_turma, semestre, horarios, vagas, local)
                turmas.append(t)
                salvar_tudo(alunos, cursos, turmas, matriculas)
                print("Turma criada!")

            elif opcao == "4":
                if not alunos or not turmas:
                    print("Cadastre alunos e turmas primeiro.")
                    continue
                print("Alunos disponíveis:")
                for i, a in enumerate(alunos):
                    print(f"{i+1}. {a.nome} ({a.matricula})")
                aluno_idx = int(input("Escolha o aluno pelo número: ")) - 1
                print("Turmas disponíveis:")
                for i, t in enumerate(turmas):
                    status = "ABERTA" if t.aberta else "FECHADA"
                    print(f"{i+1}. {t.id} ({t.curso.nome}, {t.semestre}) - {status}")
                turma_idx = int(input("Escolha a turma pelo número: ")) - 1
                m = Matricula(alunos[aluno_idx], turmas[turma_idx])
                matriculas.append(m)
                salvar_tudo(alunos, cursos, turmas, matriculas)
                print("Aluno matriculado!")

            elif opcao == "5":
                for a in alunos:
                    print(f"{a.matricula} - {a.nome} - {a.email}")

            elif opcao == "6":
                for c in cursos:
                    print(str(c))

            elif opcao == "7":
                for t in turmas:
                    alunos_turma = ', '.join([m.aluno.nome for m in matriculas if m.turma == t and m.ativa])
                    print(f"{t.id} ({t.curso.nome}, {t.semestre}) - {len(t)}/{t.vagas} vagas - Alunos: {alunos_turma}")

            elif opcao == "8":
                if not matriculas:
                    print("Nenhuma matrícula encontrada.")
                    continue
                for i, m in enumerate(matriculas):
                    print(f"{i+1}. {m.aluno.nome} na turma {m.turma.id}")
                idx = int(input("Escolha a matrícula pelo número: ")) - 1
                m = matriculas[idx]
                nota = float(input("Nota (0-10): "))
                frequencia = float(input("Frequência (0-100): "))
                m.lancar_nota(nota)
                m.lancar_frequencia(frequencia)
                # Atualiza histórico do aluno
                m.aluno.adicionar_disciplina(m.turma.curso, nota, frequencia)
                salvar_tudo(alunos, cursos, turmas, matriculas)
                print("Nota e frequência registradas!")

            elif opcao == "9":
                nome_aluno = input("Nome do aluno: ")
                aluno_obj = next((a for a in alunos if a.nome == nome_aluno), None)
                if aluno_obj:
                    for d in aluno_obj.historico:
                        print(f"Curso {d['curso']} - Nota: {d['nota']} - Frequência: {d['frequencia']}%")
                    print(f"CR: {aluno_obj.calculo_de_CR():.2f}")
                else:
                    print("Aluno não encontrado.")

            elif opcao == "10":
                # Relatórios simples (seu módulo relatorios.py pode ser usado aqui)
                from relatorios import (
                    alunos_por_turma,
                    taxa_aprovacao_por_curso_e_turma,
                    distribuicao_notas_por_turma,
                    alunos_em_risco,
                    top_n_por_CR,
                )
                print("\n=== Relatórios ===")
                print("1. Alunos por turma")
                print("2. Taxa de aprovação")
                print("3. Distribuição de notas")
                print("4. Alunos em risco")
                print("5. Top N alunos por CR")
                escolha = input("Escolha: ")
                if escolha == "1":
                    for r in alunos_por_turma(turmas, matriculas):
                        print(r)
                elif escolha == "2":
                    for r in taxa_aprovacao_por_curso_e_turma(cursos, turmas, matriculas, settings):
                        print(r)
                elif escolha == "3":
                    for r in distribuicao_notas_por_turma(turmas, matriculas):
                        print(r)
                elif escolha == "4":
                    for r in alunos_em_risco(matriculas, settings):
                        print(r)
                elif escolha == "5":
                    n = getattr(settings, "top_n_alunos", 5)
                    for r in top_n_por_CR(alunos, n):
                        print(r)

            elif opcao == "0":
                print("Saindo...")
                break

            else:
                print("Opção inválida.")

        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    menu()