import statistics

def alunos_por_turma(turmas, matriculas):
    """
    Lista de alunos por turma, mostrando vagas ocupadas vs. vagas totais.
    """
    resultado = []
    for t in turmas:
        ocupadas = len(t)  # usa __len__ da Turma
        total = t.vagas
        alunos = [m.aluno.nome for m in matriculas if m.turma == t and m.ativa]
        resultado.append({
            "turma": t.id,
            "curso": t.curso.nome,
            "ocupadas": ocupadas,
            "total": total,
            "alunos": alunos
        })
    return resultado


def taxa_aprovacao_por_curso_e_turma(cursos, turmas, matriculas, settings):
    """
    Calcula taxa de aprovação por curso e por turma.
    """
    dados = []
    for t in turmas:
        ms = [m for m in matriculas if m.turma == t]
        if not ms:
            dados.append({"turma": t.id, "curso": t.curso.codigo, "aprovacao": None})
            continue
        aprovados = sum(1 for m in ms if m.situacao() == "APROVADO")
        taxa = aprovados / len(ms)
        dados.append({
            "turma": t.id,
            "curso": t.curso.codigo,
            "aprovacao": round(taxa, 2)
        })
    return dados


def distribuicao_notas_por_turma(turmas, matriculas):
    """
    Distribuição de notas por turma (média, mediana, desvio padrão).
    """
    dist = []
    for t in turmas:
        notas = [m.nota for m in matriculas if m.turma == t and m.nota is not None]
        if notas:
            dist.append({
                "turma": t.id,
                "media": round(sum(notas)/len(notas), 2),
                "mediana": round(statistics.median(notas), 2),
                "desvio": round(statistics.pstdev(notas), 2),
            })
        else:
            dist.append({"turma": t.id, "media": None, "mediana": None, "desvio": None})
    return dist


def alunos_em_risco(matriculas, settings):
    """
    Lista alunos em risco (nota < corte ou frequência < mínimo).
    """
    risco = []
    for m in matriculas:
        corte = settings.nota_minima_aprovacao
        freq_min = settings.frequencia_minima
        if (m.nota is not None and m.nota < corte) or (m.frequencia is not None and m.frequencia < freq_min):
            risco.append({
                "aluno": m.aluno.nome,
                "turma": m.turma.id,
                "nota": m.nota,
                "frequencia": m.frequencia
            })
    return risco


def top_n_por_CR(alunos, n):
    """
    Top N alunos por CR no período.
    """
    ordenados = sorted(alunos, reverse=True)  # usa __lt__ do Aluno
    return [
        {"aluno": a.nome, "matricula": a.matricula, "CR": round(a.calculo_de_CR(), 2)}
        for a in ordenados[:n]
    ]