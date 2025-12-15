from modelos.classes import aluno
from modelos.classes import turma
from modelos.classes.aluno import Aluno
from modelos.classes.curso import Curso
from modelos.classes.matricula import Matricula 
from modelos.classes.turma import Turma
from modelos.classes.configuracoes import Configuracoes

def test_aprovacao_com_settings():
    settings = Configuracoes.carregar("settings.json")
    m = Matricula(aluno, turma)
    m.lancar_nota(7)
    m.lancar_frequencia(80)
    assert m.calcular_situacao(settings) == "APROVADO"
