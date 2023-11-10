
import streamlit as st
from exploration import *
from Deaths import Deaths
from Forces import Forces
from mapplot import mapPlot

st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

selectedPlot = st.sidebar.selectbox(
    "Select plot",
    ("Home", "Data exploration", "Deaths", "Forces", "Map"),
)

match selectedPlot:
    case "Home":
        st.markdown("""
        ## Fatalities in the Israeli-Palestinian conflict
        
        """)
    case "Data exploration":
        exploration_plot()
    case "Deaths":
        Deaths()
    case "Map":
        mapPlot()
    case "Forces":
        Forces()
    case "Deaths":
        Deaths()
