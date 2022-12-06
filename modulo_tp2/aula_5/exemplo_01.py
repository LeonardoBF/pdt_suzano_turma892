import streamlit as st

## -- Textos -- ##
st.title('Elementos Textuais')

# Title
st.title('Olá isto é um título!')

# Header
st.header('Sou um título 2')

# Subheader
st.subheader('sou um título 3 / subtítulo')

# Text
st.text('Isto é um texto: Eu S2 Python!')

var = 10
st.text(f'Minha var = {var}')

# Markdown
st.markdown("""
    # Título 1
    ## Título 2
    ### Título 3
    
    - texto normal
    - **negrito**
    - *itálico* 
    
    :smile:          
""")

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')




