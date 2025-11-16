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








