
import streamlit as st
import lib
import plotly.express as px

st.title('Student exam performance')

data_load_state = st.text('Loading data...')
data = lib.load_data()
data_load_state.text('Loading data...done!')

columns = data.columns

x_column = st.selectbox('X', columns)
y_column = st.selectbox('Y', columns)

fig = px.scatter(data, x=x_column, y=y_column)
# fig = px.histogram(data, x=x_column)

st.plotly_chart(fig)