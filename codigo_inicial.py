class Aluno:
        def _init_ (self, matricula, nome, email, historico, frequencia):
            self.matricula = matricula
            self.nome = nome
            self.email = email
            self.historico = historico
            self.frequencia = frequencia
            
        def calculo_de_CR(self):
            pass
            # media ponderada simples com sabe no historico
        def calcular_sit_matricula(self):
            pass

class Cursos:
     def _init_ (self, codigo_curso, nome, carga_horaria, lista_requisitos, disciplinas):
            self.codigo_curso = codigo_curso
            self.nome = nome
            self.carga_horaria = carga_horaria
            self.lista_requisitos = lista_requisitos
            self.disciplinas = disciplinas

     def calcular_carga_horaria(self):
        pass
     
     def impedir_ciclos(self):
        pass
class Turmas:
        def _init_ (self, id_turma, codigo_curso, periodo, horario, sala, capacidade, alunos_matriculados):
                self.id_turma = id_turma
                self.codigo_curso = codigo_curso
                self.periodo = periodo
                self.horario = horario
                self.sala = sala
                self.capacidade = capacidade
                self.alunos_matriculados = alunos_matriculados
    
        def abrir_turma(self, aluno):
            pass
        def fechar_turma(self, aluno):
            pass
        
        def impedir_matricula_fech(self):
            pass
        def criar_turmas(self):
            pass



    
