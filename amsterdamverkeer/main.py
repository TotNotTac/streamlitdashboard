
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown("""
    # Amsterdam metro- en tram netwerk
""")

data_load_state = st.text('Loading data...')

# Data acquired from https://maps.amsterdam.nl/open_geodata/?k=420

# Load data from csv file
df = pd.read_csv('TRAMMETRO_LIJNEN_2022.csv', sep=';')

# Remove unnamed columns
df.loc[:, ~df.columns.str.contains('^Unnamed')]

data_load_state.text('')