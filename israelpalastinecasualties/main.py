
import streamlit as st
from exploration import *
from mapplot import mapPlot

st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

selectedPlot = st.sidebar.selectbox(
    "Select Page",
    ("Home", "Data exploration", "Map"),
)

match selectedPlot:
    case "Home":
        st.markdown("""
        ## Fatalities in the Israeli-Palestinian conflict

        """)
    case "Data exploration":
        exploration_plot()
    case "Map":
        mapPlot()
