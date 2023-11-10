
import streamlit as st
from exploration import *
from jan import jan
from jan2 import jan2

st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

selectedPlot = st.sidebar.selectbox(
    "Select plot",
    ("Data exploration", "jan", "jan2"),
)

match selectedPlot:
    case "Data exploration":
        exploration_plot()
    case "jan":
        jan()
    case "jan2":
        jan2()