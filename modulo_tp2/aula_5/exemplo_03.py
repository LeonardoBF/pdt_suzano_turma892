import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px

import streamlit as st


## -- Gráficos -- ##
st.title('Gráficos')

# carrega o datasets
mpg = sns.load_dataset('mpg')
tips = sns.load_dataset('tips')
penguins = sns.load_dataset('penguins')

# Plot com pandas plot
st.header('Pandas Plot')
fig = plt.figure()
mpg['origin'].value_counts().plot.bar()
st.pyplot(fig)

# Plot com matplotlib
st.header('Matplotlib')
fig = plt.figure()
plt.scatter(data=mpg, x='acceleration', y='horsepower')
st.pyplot(fig)

# Plot com seaborn
st.header('Seaborn')
fig, ax = plt.subplots()
sns.barplot(data=tips, x='day', y='tip', estimator=np.mean)
st.pyplot(fig)

# Plot com plotly
st.header('Plotly')
plot_plotly = px.histogram(data_frame=penguins, x='body_mass_g')
st.plotly_chart(plot_plotly)
