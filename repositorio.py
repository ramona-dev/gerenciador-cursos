import json

ARQUIVO = "dados.json"

def salvar_tudo(alunos, cursos, turmas, matriculas):
    dados = {
        "alunos": [
            {"matricula": a.matricula, "nome": a.nome, "email": a.email, "historico": a.historico}
            for a in alunos
        ],
        "cursos": [
            {"codigo": c.codigo, "nome": c.nome, "carga_horaria": c.carga_horaria}
            for c in cursos
        ],
        "turmas": [
            {
                "codigo_turma": t.codigo_turma,
                "curso_codigo": t.curso.codigo,
                "semestre": getattr(t, "semestre", None),
                "capacidade": getattr(t, "capacidade", 40),
                "horario": getattr(t, "horario", {}),
                "matriculas": {a.matricula: nota for a, nota in t.matriculas.items()}
            }
            for t in turmas
        ],
        "matriculas": [
            {
                "aluno": m.aluno.matricula,
                "turma": m.turma.codigo_turma,
                "nota": m.nota,
                "frequencia": m.frequencia,
                "ativa": m.ativa,
                "data": str(m.data)
            }
            for m in matriculas
        ]
    }
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def carregar_tudo():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            conteudo = f.read().strip()
            if not conteudo:  # arquivo existe mas está vazio
                return {"alunos": [], "cursos": [], "turmas": [], "matriculas": []}
            return json.loads(conteudo)
    except FileNotFoundError:
        # arquivo ainda não existe
        return {"alunos": [], "cursos": [], "turmas": [], "matriculas": []}