from aula_class import *

def gerar_txt(id_msg: int, aulas: list) -> str: 
    msgs_aluno = '-'*70 + '\n'
    for aula in aulas:
        msg = gerar_mensagem(id_msg, aula)
        msgs_aluno += msg
        msgs_aluno += '-'*70 + '\n'
    return msgs_aluno

def gerar_mensagem(id_msg: int, aula: Aula) -> str:
    if id_msg == 1:
        msg = f'''Olá, {aula.aluno.nome}, tudo bem!?
Sou {aula.monitor}, monitor do curso de {aula.curso} da Infinity School! 

📅 Passando pra lembrar da sua aula que está marcada para dia {aula.data}, as {aula.hora[0]} horas, posso cofirmar?

Se sim, preciso das seguintes informações:
- Se é Reposição ou reforço;
- Assunto perdido ou que deseja reforçar;
- Tipo de aula (se você deseja on-line ou presencial);

Aguardo o seu retorno!😉\n'''
    elif id_msg == 2:
        msg = f'''☀️Bom dia {aula.aluno.nome}, tudo certo?
{aula.monitor} aqui, monitor do curso de {aula.curso} da Infinity School.

✅Gostaria apenas de confirmar sua presença para nossa aula de hoje {aula.data}, as {aula.hora[0]} horas.

Aguardo o sua presença!'''
    return msg

