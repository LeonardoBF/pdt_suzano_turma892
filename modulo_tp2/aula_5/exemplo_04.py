import numpy as np
import streamlit as st

## -- Input e Fluxo -- ##
st.title('Input e Fluxo')


# checkbox
st.header('Checkbox')
check = st.checkbox('me marque')
st.write(check)

if check:
    st.bar_chart(np.random.randn(50, 3))
    
    
# button
st.header('Button')
button = st.button('clique em mim')
st.write(button)

if button:
    st.write(':smile:')
else:
    st.write(':sweat:')
    
# slider
st.header('Slider')
slider = st.slider('Avalie este app:',
                   min_value=1,
                   max_value=5,
                   value=5,
                   step=1)
st.write(slider)

for i in range(1, slider + 1):
    st.write(f'Estrela {i}:', ':star:' * i)