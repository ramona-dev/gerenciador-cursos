#  📘 LuPOO - README
-----------------------
# Descrição do projeto

O **LuPOO** é um sistema acadêmico simples utilizando Orientação a Objetos em Python. O sistema irá representar entidades como Alunos, Cursos, Turmas, Professores e Configurações, fornecendo uma base sólida para gerenciamento de matrículas, cálculo de CR, controle de frequência, requisitos de curso, entre outros.

O foco inicial é estabelecer uma estrutura limpa e modular, com classes bem definidas e responsabilidades claras, seguindo boas práticas de POO

**Objetivo**

O objetivo deste sistema é fornecer uma plataforma simples e eficiente para gestão acadêmica, permitindo que alunos, professores e administradores consultem informações de forma rápida e organizada. O sistema possibilita criar e gerenciar cursos, turmas e matrículas, além de oferecer funcionalidades como lançamento de frequência, acompanhamento das turmas, abertura de novas turmas e visualização dos dados de alunos e professores. A proposta é entregar uma solução robusta, orientada a objetos, focada na lógica de negócios e adequada para uso em linha de comando ou API mínima.


## Estrutura de classes planejada
🧍 Pessoa (classe base)

Responsabilidade: representar qualquer pessoa da instituição (características comuns).

Atributos: nome, email

Métodos: nenhum obrigatório (podem ser adicionados conforme o sistema evoluir)

🎓 Aluno (herda de Pessoa)

Responsabilidade: representar um aluno e suas informações acadêmicas.

Atributos: matricula, historico (notas e disciplinas cursadas), frequencia

Métodos: calcular_cr() – calcula o coeficiente de rendimento
pode_matricular(turma) – verifica se pode se matricular em uma turma
adicionar_nota()
atualizar_frequencia()

👨‍🏫 Professor (herda de Pessoa)

Responsabilidade: armazenar dados de professores.

Atributos: matricula_prof, historico (disciplinas ministradas)

Métodos:lançar_nota()
registrar_frequencia()

🏫 Curso

Responsabilidade: representar um curso e suas características.

Atributos: codigo, nome, carga_horaria, prerequisitos, disciplinas

Métodos: calcular_carga_total()

👥 Turma

Responsabilidade: representar turmas ofertadas e gerenciar matrículas.

Atributos: id_turma, curso, periodo, horario, sala, capacidade, alunos_matriculados

Métodos:matricular(aluno)
remover_aluno(aluno)
verificar_vagas()
verificar_conflito_horario(aluno)
fechar_turma()

⚙️ Configuracoes

Responsabilidade: regras globais do sistema.

Atributos: nota_minima_aprovacao, frequencia_minima, data_limite_trancamento, max_turmas_por_aluno, top_n_alunos
Métodos: carregar_arquivo()

# UML textual 
### Pessoa
**Responsabilidade:** representar qualquer pessoa da instituição (características comuns).
#### Atributos
| Atributo | Tipo | Descrição |                                        
|---------|------|-----------|
| nome | str | Nome completo |
| email | str | Email da pessoa |

#### Métodos
| Método | Descrição |
|--------|-----------|
| `__str__()` | Representação textual |


### Aluno (herda de Pessoa)
**Responsabilidade:** representar um aluno e suas informações acadêmicas.
#### Atributos
| Atributo | Tipo | Descrição |
|---------|------|-----------|
| matricula | str | Código do aluno |
| historico | list | Lista de disciplinas e notas |
| frequencia | float | Frequência geral |

#### Métodos
| Método | Descrição |
|--------|-----------|
| calcular_cr() | Calcula o coeficiente de rendimento |
| validar_matricula() | Valida matrícula conforme regras |


### Professor 
| Atributo       | Tipo | Descrição               |
| -------------- | ---- | ----------------------- |
| matricula_prof | str  | Registro do professor   |
| historico      | list | Disciplinas ministradas |


### Turma

#### Atributos
| Atributo | Tipo | Descrição |
|----------|------|------------|
| id_turma | str | Identificador da turma |
| codigo_curso | int | Identificador do curso |
| alunos matriculados | str | alunos matriculados |
| horario | str | Horário |
| sala | str | Sala |
| capacidade | int | Máximo de alunos |

### Curso 

| Atributo      | Tipo | Descrição                       |
| ------------- | ---- | ------------------------------- |
| codigo        | str  | Identificador único do curso    |
| nome          | str  | Nome do curso                   |
| carga_horaria | int  | Carga horária total             |
| prerequisitos | list | Lista de cursos necessários     |
| disciplinas   | list | Disciplinas que compõem o curso |

| Método                 | Descrição                                     |
| ---------------------- | --------------------------------------------- |
| calcular_carga_total() | Soma a carga horária das disciplinas do curso |

### Configuraçoes 

| Atributo          | Tipo  | Descrição                       |
| ----------------- | ----- | ------------------------------- |
| nota_minima       | float | Nota mínima para aprovação      |
| frequencia_minima | int   | Percentual mínimo de frequência |
| limite_turmas     | int   | Máximo de turmas por aluno      |
| top_n_alunos      | int   | Quantidade para ranking         |

| Método             | Descrição                             |
| ------------------ | ------------------------------------- |
| carregar_arquivo() | Carrega configuração a partir de JSON |












