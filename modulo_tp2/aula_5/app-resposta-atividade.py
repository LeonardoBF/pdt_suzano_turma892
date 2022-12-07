import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st
from funcoes import carrega_dataset


# CORPO
st.markdown("""
            # iNalyze
            ### *A sua ferramenta para análise dados*
            ---
            """)


## CORPO - Carregando o dataset
st.header('Dataset')
nome_dataset = st.text_input('Qual o nome do dataset que deseja carregar?',
                             value='penguins')

if nome_dataset:
    df = carrega_dataset(nome_dataset)
        
# SIDEBAR
with st.sidebar:
    st.title('Filtros')
    cols_selected = \
        st.multiselect('Filtre os campos que deseja analisar:',
                       options=list(df.columns),
                       default=list(df.columns))
    
    frac_sample = \
        st.slider('Defina o percentual do dataset para análise:', 
                  min_value=1, max_value=100, value=50, step=1)

df_selected = df[cols_selected].sample(frac=frac_sample/100)
    
    
## CORPO - Info do dataset
with st.expander('Dados do Dataset'):
    st.header('Dados do Dataset')
    st.subheader('Primeiros registros')
    st.write(df_selected.head())
    
    st.subheader('Tamanho do Dataset')
    st.write('Quantidade de linhas:', df_selected.shape[0])
    st.write('Quantidade de colunas:', df_selected.shape[1])
    
    st.subheader('Colunas')
    for col in df_selected.columns:
        st.text(f'- {col}')
        
    st.subheader('Dados Faltantes')
    st.write(df_selected.isna().sum()[df_selected.isna().sum() > 0])

    st.subheader('Estatísticas Descritivas')
    st.write(df_selected.describe())


## CORPO - Análise Univariada
st.header('Análise Univariada')
univar_campo =  \
    st.selectbox('Selecione o campo que deseja avaliar a distribuição:',
                 options=list(df_selected.select_dtypes(include=np.number)))


st.plotly_chart(px.histogram(data_frame=df_selected, x=univar_campo))
st.plotly_chart(px.box(data_frame=df_selected, y=univar_campo))


## CORPO - Análise Bivariada
st.header('Análise Bivariada')
bivar_graf_option = \
    st.radio('Escolha um tipo de gráfico:',
             options=['dispersão', 'boxplot', 'pairplot'])

if bivar_graf_option == 'dispersão':
    bivar_dispersao_num1 =  \
        st.selectbox('Selecione primeira variável numérica:',
                     options=list(df_selected.select_dtypes(include=np.number)))
        
    bivar_dispersao_num2 =  \
        st.selectbox('Selecione segunda variável numérica:',
                     options=list(df_selected.select_dtypes(include=np.number)))
        
    st.plotly_chart(
        px.scatter(data_frame=df_selected, 
                   x=bivar_dispersao_num1, 
                   y=bivar_dispersao_num2)
    )
        
elif bivar_graf_option == 'boxplot':
    bivar_boxplot_num =  \
        st.selectbox('Selecione uma variável numérica:',
                     options=list(df_selected.select_dtypes(include=np.number)))
        
    bivar_boxplot_cat =  \
        st.selectbox('Selecione uma variável categórica:',
                     options=list(df_selected.select_dtypes(exclude=np.number)))
        
    st.plotly_chart(
        px.box(data_frame=df_selected, 
                   x=bivar_boxplot_cat, 
                   y=bivar_boxplot_num)
    )
    
else:
    bivar_pairplot = sns.pairplot(df_selected)
    st.pyplot(bivar_pairplot)
    

## CORPO - Análise Multivariada
st.header('Análise Multivariada')
multivar_graf_option = \
    st.radio('Escolha um tipo de gráfico:',
             key='multivar_graf_option',
             options=['dispersão', 'boxplot', 'pairplot'])

if multivar_graf_option == 'dispersão':
    multivar_dispersao_num1 =  \
        st.selectbox('Selecione primeira variável numérica:',
                     key='multivar_dispersao_num1',
                     options=list(df_selected.select_dtypes(include=np.number)))
        
    multivar_dispersao_num2 =  \
        st.selectbox('Selecione segunda variável numérica:',
                     key='multivar_dispersao_num2',
                     options=list(df_selected.select_dtypes(include=np.number)))
        
    multivar_dispersao_seg = \
        st.selectbox('Selecione uma variável categórica:',
                     key='multivar_dispersao_seg',
                     options=list(df_selected.select_dtypes(exclude=np.number)))
    
    multivar_dispersao_check = \
        st.checkbox('Adicionar linha de tendência')
    
    if multivar_dispersao_check:
        st.plotly_chart(
            px.scatter(data_frame=df_selected, 
                    x=multivar_dispersao_num1, 
                    y=multivar_dispersao_num2,
                    color=multivar_dispersao_seg,
                    trendline='ols')
        )
    else:
        st.plotly_chart(
            px.scatter(data_frame=df_selected, 
                    x=multivar_dispersao_num1, 
                    y=multivar_dispersao_num2,
                    color=multivar_dispersao_seg)
        )
        
elif multivar_graf_option == 'boxplot':
    multivar_boxplot_num =  \
        st.selectbox('Selecione uma variável numérica:',
                     key='multivar_boxplot_num',
                     options=list(df_selected.select_dtypes(include=np.number)))
        
    multivar_boxplot_cat =  \
        st.selectbox('Selecione uma variável categórica:',
                     key='multivar_boxplot_cat',
                     options=list(df_selected.select_dtypes(exclude=np.number)))
        
    multivar_boxplot_seg =  \
        st.selectbox('Selecione uma variável categórica:',
                     key='multivar_boxplot_seg',
                     options=list(df_selected.select_dtypes(exclude=np.number)))
        
    st.plotly_chart(
        px.box(data_frame=df_selected, 
                   x=multivar_boxplot_cat, 
                   y=multivar_boxplot_num,
                   color=multivar_boxplot_seg)
    )
    
else:
    multivar_pairplot_seg =  \
        st.selectbox('Selecione uma variável categórica:',
                     key='multivar_pairplot_seg',
                     options=list(df_selected.select_dtypes(exclude=np.number)))
        
    multivar_pairplot = sns.pairplot(df_selected, hue=multivar_pairplot_seg)
    st.pyplot(multivar_pairplot)


# ATIVIDADES
# Refatore o código, aplicando as modificações:

# 1 - Modularize o código passando a função "carrega_dataset" para um módulo

# 2 - Crie um slider no sidebar que permita filtrar uma amostra do dataset.
#     Para realizar amostragem, utilize o método sample do dataframe pandas.

# 3 - Adicione a informação do tamanho do dataset na seção 
#     de 'Dados do Dataset'

# 4 - Adicione uma seção de análise multivariada:
#   4.1 - Adicione a possibilidade de segmentação no gráfico de dispersao
#   4.2 - Adicione checkbox que permita incluir linha de tendência 
#         no gráfico de dispersão
#   4.3 - Adicione a possibilidade de segmentação no gráfico de boxplot
#   4.4 - Adicione a possibilidade de segmentação no gráfico de pairplot

