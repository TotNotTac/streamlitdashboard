
import streamlit as st
from exploration import *

st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

selectedPlot = st.sidebar.selectbox(
    "Select plot",
    ("Data exploration", ""),
)

match selectedPlot:
    case "Data exploration":
        exploration_plot()
