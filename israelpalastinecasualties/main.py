
import streamlit as st
from exploration import *
from jan import jan
from jan2 import jan2
from mapplot import mapPlot

st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

selectedPlot = st.sidebar.selectbox(
    "Select plot",
    ("Home", "Data exploration", "jan", "jan2", "Map"),
)

match selectedPlot:
    case "Home":
        st.markdown("""
        ## Fatalities in the Israeli-Palestinian conflict
        
        """)
    case "Data exploration":
        exploration_plot()
    case "jan":
        jan()
    case "jan2":
        jan2()
    case "Map":
        mapPlot()
