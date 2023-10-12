
import streamlit as st
from streamlit_folium import st_folium

import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd

import seaborn as sns

import mapplot

st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown("""
    # Laadpaaldata
""")

data_load_state = st.text('Loading data...')

# Load data from csv file
df = pd.read_csv('laadpaaldata.csv')

# Remove unnamed columns
df.loc[:, ~df.columns.str.contains('^Unnamed')]

data_load_state.text('')

# st_folium(mapplot.map(df))
