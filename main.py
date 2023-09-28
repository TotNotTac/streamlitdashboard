
import streamlit as st
import lib
import plotly.express as px

st.title('Student exam performance')

data_load_state = st.text('Loading data...')
data = lib.load_data()
data_load_state.text('')

columns = data.columns

# Fig 1

plotType = st.selectbox("plot type", ["scatterplot", "density contour", "3D scatter"])

thirdDimension = plotType == "3D scatter"

x_column = st.selectbox('X', columns, index=5)
y_column = st.selectbox('Y', columns, index=6)
z_column = st.selectbox('Z (only in 3d plot)', columns, disabled=not(thirdDimension), index=7)
color_column = st.selectbox('Color', columns)

opacity = st.slider("Opacity", min_value=0.0, max_value=1.0, value=0.6)
markSize = st.slider("Size", min_value=0, max_value=25, value=4)

if thirdDimension:
    fig = px.scatter_3d(data, x=x_column, y=y_column, z=z_column, color=color_column, opacity=opacity)
    fig.layout.scene.camera.projection.type = "orthographic"
    fig.update_traces(marker_size = markSize)
    fig.update_layout(height=800)
elif plotType == "scatterplot":
    fig = px.scatter(data, x=x_column, y=y_column, color=color_column, opacity=opacity, size_max=markSize)
else:
    fig = px.density_contour(data, x=x_column, y=y_column, color=color_column)

st.plotly_chart(fig, theme=None, use_container_width=True)


# Fig 2

fig = px.box(data, x="reading score", y="gender", color="gender")
st.plotly_chart(fig, theme=None, use_container_width=True)

fig = px.box(data, x="writing score", y="gender",color="gender")
st.plotly_chart(fig, theme=None, use_container_width=True)

fig = px.box(data, x="math score", y="gender",color="gender")
st.plotly_chart(fig, theme=None, use_container_width=True)

# Fig 3

fig = px.box(data, x="reading score", y="lunch", color="lunch")
st.plotly_chart(fig, theme=None, use_container_width=True)

fig = px.box(data, x="writing score", y="lunch", color="lunch")
st.plotly_chart(fig, theme=None, use_container_width=True)

fig = px.box(data, x="math score", y="lunch", color="lunch")
st.plotly_chart(fig, theme=None, use_container_width=True)