import pywhatkit as zap
from aula_class import *
from mensagens import *

# Funções
def lista_aulas(aulas_text: str, course: str, monitor: str) -> list:
    '''
    Uma função que recebe uma string com varias aulas no formato:
    
    -> hora - nome_aluno - telefone - tipo_aula - data

    e retorna uma lista com objetos do tipo "aula" que tem como atributo:

    -> Aluno
    -> Horario
    -> Data

    O aluno é do tipo "aluno" que tem nome e telefone
    '''
    # Transformando o txt em uma lista com strs, onde cada item é uma aula
    aulas_raw = aulas_text.split('\n')
    aulas = []
    for aula in aulas_raw:
        aulas.append(aula.split(' - '))
    for aula in aulas:
        aula.pop(3)

    # Removendo aulas duplicadas (mesmo aluno, mais de um horario)
    alunos = aulas.copy()
    alunos = list(map(lambda aluno: aluno[1:], aulas))
    alunos_aux = set([tuple(aluno) for aluno in alunos])
    alunos.clear()
    for nome, numero, _ in alunos_aux:
        alunos.append(Aluno(nome, numero))

    # Criando as aulas
    aulas_raw = aulas.copy()
    aulas.clear()
    for aluno in alunos:
        aulas.append(Aula(aluno, [], '', course, monitor))

    # Adicionando os horarios das Aulas:
    for horario, nome_aluno, _, data in aulas_raw:
        for aula in aulas:
            if (horario not in aula.hora) and (nome_aluno == aula.aluno.nome):
                if len(horario) == 4:
                    horario = '0' + horario
                aula.hora.append(horario)
                aula.data = data[:5]

    # Organizando por ordem das Aulas:
    aulas.sort(key= lambda aula: aula.hora[0])
    return aulas

def mandar_zaps(id_msg: int, aulas: list) -> None:
    for aula in aulas:
        msg = gerar_mensagem(id_msg, aula)
        zap.sendwhatmsg_instantly(
            phone_no= '+55'+aula.aluno.numero, 
            message= msg,
            tab_close= True,
            close_time= 2
            )
