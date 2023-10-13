
import streamlit as st
import lib
import plotly.express as px
import pandas as pd

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

df = pd.read_csv('StudentsPerformance.csv')

st.title("Interactive Data Filter")

math_score_range = st.slider("Math Score Range", min_value=0, max_value=100, value=(0, 100), step=5)

reading_score_range = st.slider("Reading Score Range", min_value=0, max_value=100, value=(0, 100), step=5)

writing_score_range = st.slider("Writing Score Range", min_value=0, max_value=100, value=(0, 100), step=5)

filtered_df = df[
    (df['math score'] >= math_score_range[0]) & (df['math score'] <= math_score_range[1]) &
    (df['reading score'] >= reading_score_range[0]) & (df['reading score'] <= reading_score_range[1]) &
    (df['writing score'] >= writing_score_range[0]) & (df['writing score'] <= writing_score_range[1])
]

st.write("Filtered Data:")
st.write(filtered_df)

st.subheader("Histograms")
fig, ax = px.subplots(1, 3, figsize=(15, 5))

ax[0].hist(filtered_df['math score'], bins=20, edgecolor='k')
ax[0].set_xlabel('Math Score')
ax[0].set_ylabel('Frequency')
ax[0].set_title('Math Score Histogram')

ax[1].hist(filtered_df['reading score'], bins=20, edgecolor='k')
ax[1].set_xlabel('Reading Score')
ax[1].set_ylabel('Frequency')
ax[1].set_title('Reading Score Histogram')

ax[2].hist(filtered_df['writing score'], bins=20, edgecolor='k')
ax[2].set_xlabel('Writing Score')
ax[2].set_ylabel('Frequency')
ax[2].set_title('Writing Score Histogram')

px.tight_layout()
st.pyplot(fig)