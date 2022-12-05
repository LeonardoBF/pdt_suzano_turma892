import streamlit as st
import pandas as pd

## -- Monstrando Elementos -- ##
st.title('Mostrando Elementos')

# utilizando st.write
st.write('## Exemplos com st.write')

def soma(a, b):
    """Esta é uma função que soma 2 números.

    Args:
        a (float, int): variável 1
        b (flot, int): variável 2
    """
    return a + b

st.write(soma)

df = pd.DataFrame({
    'col1': [1, 2, 3, 4, 5],
    'col2': [10, 20, 30, 40, 50]
})

st.write(df)


# utilizando magic
'## Exemplos com Magic'

soma
df


# utilizando st.dataframe
st.write('## Exemplo com st.dataframe')
st.dataframe(df, width=500)