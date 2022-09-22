from aula_class import *
from aulas_zaps import *
from mensagens import *
import streamlit as st

# Side Bar
st.sidebar.markdown('''# Instruções

### Entradas

1. Nome do monitor
2. Curso que monitora
3. Aulas

> - Cada aula deve ser separada por uma quebra de linha.
> - As aulas devem vir no estilo:
> - hh:mm - Nome - 71999999999 - Particular - dd/mm/yyyy

4. Id da menssagem

> - Existem dois tipos de menssagem que você pode gerar.
> - Veja quais são abaixo:

### Menssagens

1. Menssagem (Dias anteriores ao dia da aula)
Olá, "aluno", tudo bem!?
Sou "monitor", monitor do curso de "curso" da Infinity School! 

📅 Passando pra lembrar da sua aula que está marcada para dia "data", as "horario" horas, posso cofirmar?

Se sim, preciso das seguintes informações:
- Se é Reposição ou reforço;
- Assunto perdido ou que deseja reforçar;
- Tipo de aula (se você deseja on-line ou presencial);

Aguardo o seu retorno!😉

2. Menssagem (Dia da aula)
☀️Bom dia "aluno", tudo certo?
"monitor" aqui, monitor do curso de "curso" da Infinity School.

✅Gostaria apenas de confirmar sua presença para nossa aula de hoje ("dia"), as "horario" horas.

Aguardo o sua presença!
''')

# Main Page
'''
# Gerador de menssagens
Há dois padrões de menssagens que você pode gerar, só de colar o texto com as aulas e preencher corretamente o formulario.
Leia a sidebar para mais orientações.
'''

with st.form('Infos Aulas'):
    monitor = st.text_input('Nome do Monitor')
    curso = st.selectbox('Curso', ['Dev Full-Stack', 'Desing Full-Stack', 'Art Desing', 'Metaverso', 'Film Desing', 'Fotografia Desing'])
    text = st.text_area('Aulas')
    id_mensagem = st.number_input('Mensagem', min_value=1, max_value=2)
    button = st.form_submit_button('Enviar Menssagens')

if button:
    aulas = lista_aulas(text, curso, monitor)
    # st.write('Baixar as Mensagens:')
    # st.download_button(
    #     label='Download',
    #     data= gerar_txt(id_mensagem, aulas),
    #     file_name= 'menssagens.txt'
    # )
    mandar_zaps(id_mensagem, aulas)
