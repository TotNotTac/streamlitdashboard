
import streamlit as st
import lib
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown("""

    # Student exam performance
                
    datasource: https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

    Data is gathered during high-school exams in a high school in the USA. The students are 
    tested in the following subjects: mathmatics, reading, and writing.
""")

data_load_state = st.text('Loading data...')
df = lib.load_data()
data_load_state.text('')

columns = df.columns

# Fig 1

plotType = st.selectbox("plot type", ["scatterplot", "contour", "3D scatter"])

thirdDimension = plotType == "3D scatter"

x_column = st.selectbox('X', columns, index=5)
y_column = st.selectbox('Y', columns, index=6)
z_column = st.selectbox('Z (only in 3d plot)', columns, disabled=not(thirdDimension), index=7)
color_column = st.selectbox('Color', columns)

opacity = st.slider("Opacity", min_value=0.0, max_value=1.0, value=0.6, disabled=(plotType == 'contour'))
markSize = st.slider("Size", min_value=0, max_value=25, value=4, disabled=not(thirdDimension))

if thirdDimension:
    orthographiccamera = st.checkbox("Orthographic camera", value=False)

    plot = px.scatter_3d(df, x=x_column, y=y_column, z=z_column, color=color_column, opacity=opacity)
    if orthographiccamera:
        plot.layout.scene.camera.projection.type = "orthographic"
    plot.update_traces(marker_size = markSize)
    plot.update_layout(height=800)
elif plotType == "scatterplot":
    plot = px.scatter(df, x=x_column, y=y_column, color=color_column, opacity=opacity, size_max=markSize)
else:
    plot = px.density_contour(df, x=x_column, y=y_column, color=color_column)

st.plotly_chart(plot, theme=None, use_container_width=True)


# Fig 2

plot = px.box(df, x="reading score", y="gender", color="gender")
st.plotly_chart(plot, theme=None, use_container_width=True)

plot = px.box(df, x="writing score", y="gender",color="gender")
st.plotly_chart(plot, theme=None, use_container_width=True)

plot = px.box(df, x="math score", y="gender",color="gender")
st.plotly_chart(plot, theme=None, use_container_width=True)

# Fig 3

plot = px.box(df, x="reading score", y="lunch", color="lunch")
st.plotly_chart(plot, theme=None, use_container_width=True)

plot = px.box(df, x="writing score", y="lunch", color="lunch")
st.plotly_chart(plot, theme=None, use_container_width=True)

plot = px.box(df, x="math score", y="lunch", color="lunch")
st.plotly_chart(plot, theme=None, use_container_width=True)

# Fig 4


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