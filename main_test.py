import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

st.subheader("Math Score Histogram")
sns.histplot(filtered_df['math score'], bins=20, kde=True)
st.pyplot()

st.subheader("Reading Score Histogram")
plt.hist(filtered_df['reading score'], bins=20, edgecolor='k')
plt.xlabel('Reading Score')
plt.ylabel('Frequency')
st.pyplot()

st.subheader("Writing Score Histogram")
sns.histplot(filtered_df['writing score'], bins=20, kde=True)
st.pyplot()