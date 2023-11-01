
import streamlit as st
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd

import seaborn as sns

from loaddata import *

from describedataplot import *
from mapplot import *
from chargingtransactions import *
from otherplots import *

st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

selectedPlot = st.sidebar.selectbox(
    "Select plot",
    ("Charging stations", "Describe data", "Map plot", "Transactions"),
)

match selectedPlot:
    case "Describe data":
        describe_data_plot()
    case "Map plot":
        mapplot()
    case "Charging stations":
        chargingtransactionsplot()
    case "Transactions":
        otherplots()
