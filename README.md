# Gerenciador de cursos
Descrição do Projeto


Este projeto é um sistema de linha de comando (CLI) ou uma API mínima (usando FastAPI ou Flask) para gerenciar as operações de uma instituição de ensino. O sistema irá modelar e gerenciar as relações entre Cursos, Turmas, Alunos e Matrículas.

O foco principal não é a interface, mas a implementação robusta da lógica de negócios, aplicando princípios de Programação Orientada a Objetos (POO) para garantir um código encapsulado, validado e de fácil manutenção.

Objetivo

O objetivo principal deste projeto é aplicar e demonstrar o domínio de conceitos de POO em um cenário complexo e realista. Isso inclui:

Encapsulamento: Proteger os dados internos das classes e expor o comportamento através de métodos.

Herança: Utilizar uma classe base (ex: Pessoa) para compartilhar atributos e métodos com classes derivadas (ex: Aluno, Professor).

Métodos Especiais: Usar métodos como __init__, __str__, __repr__ para classes bem definidas.

Validações Rigorosas: Implementar validações de lógica de negócios (ex: pré-requisitos, vagas, horários) em todas as operações de matrícula.

Relações entre Classes: Modelar as complexas interações entre múltiplas classes (um aluno tem muitas matrículas, uma turma pertence a um curso, etc.).

Persistência de Dados: Implementar uma forma simples de salvar e carregar o estado do sistema (via arquivos JSON ou um banco de dados SQLite).

Funcionalidades Planejadas

Gerenciamento de Entidades: CRUD (Criar, Ler, Atualizar, Deletar) para Cursos, Turmas, Alunos e Professores.

Controle de Pré-requisitos: Um curso só pode ter a matrícula efetuada se o aluno já foi aprovado nos seus pré-requisitos.

Detecção de Choque de Horário: O sistema deve impedir que um aluno se matricule em duas turmas que tenham sobreposição de horário.

Limite de Vagas: Cada turma terá um número máximo de vagas, e o sistema não deve permitir matrículas além desse limite.

Gestão de Notas e Frequência: Professores (ou administradores) devem poder lançar notas e registrar a frequência para os alunos em uma turma.

Relatórios Acadêmicos: Geração de um histórico acadêmico para o aluno (cursos concluídos, notas, média) e relatórios de turmas (lista de alunos, taxas de aprovação).

Estrutura de Classes Planejada

SistemaAcademico (Fachada/Controlador)
|   - alunos: Lista[Aluno]
|   - professores: Lista[Professor]
|   - cursos: Lista[Curso]
|   - turmas: Lista[Turma]
|   + matricular_aluno(id_aluno, id_turma)
|   + _validar_prerequisitos(aluno, curso)
|   + _checar_choque_horario(aluno, nova_turma)
|   + _validar_vagas(turma)
|   + lancar_nota(id_matricula, nota)
|   + registrar_frequencia(id_matricula, data, status)
|   + gerar_historico_aluno(id_aluno)
|   + carregar_dados(arquivo)
|   + salvar_dados(arquivo)
|
+-- Pessoa (Classe Base Abstrata)
|   - id: string
|   - nome: string
|   - email: string
|
+-- Aluno (herda de Pessoa)
|   - matriculas: Lista[Matricula]
|   + get_historico_aprovado(): Lista[Curso]
|   + get_turmas_atuais(): Lista[Turma]
|
+-- Professor (herda de Pessoa)
|   - turmas_lecionando: Lista[Turma]
|
+-- Curso
|   - id_curso: string
|   - nome: string
|   - creditos: int
|   - prerequisitos: Lista[Curso]
|
+-- Turma
|   - id_turma: string
|   - curso: Curso             (Relação: 1 Turma -> 1 Curso)
|   - professor: Professor     (Relação: 1 Turma -> 1 Professor)
|   - horario: Horario         (Objeto para parsear e comparar horários)
|   - limite_vagas: int
|   - matriculas: Lista[Matricula] (Relação: 1 Turma -> N Matrículas)
|   + get_vagas_disponiveis(): int
|   + adicionar_matricula(aluno): Matricula
|
+-- Matricula (Classe Associativa)
|   - id_matricula: string
|   - aluno: Aluno             (Relação: 1 Matrícula -> 1 Aluno)
|   - turma: Turma             (Relação: 1 Matrícula -> 1 Turma)
|   - notas: Lista[float]
|   - frequencia: Dicionario[data, bool]
|   - status: Enum (Cursando, Aprovado, Reprovado)
|   + calcular_media_final()
|   + calcular_percentual_frequencia()


















