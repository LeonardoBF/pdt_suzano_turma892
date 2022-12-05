import streamlit as st

## -- Layouts -- ##
st.title('Layouts')

# corpo principal
st.markdown("""
## Corpo do documento

Texto qualquer que fala algo super interessante
da nossa aplicação.            
""")


# sidebar
# st.sidebar.title('Sidebar')
# st.sidebar.button('button')
# st.sidebar.checkbox('checkbox')

with st.sidebar:
    st.title('Sidebar com with')
    nome = st.text_input('Digite seu nome')
    st.text(f'Bem-vindo {nome}')


# columns
st.header('Colunas')
col1, col2, col3 = st.columns(3)
with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")
   

# Expander
st.header('Expander')
st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})
with st.expander('Mais explicações:'):
    st.write("""Notamos que o cenário 3 apresentou
             uma maior frequência de ocorrência denotando
             de forma sui generis uma maior propensão do mesmo.""")