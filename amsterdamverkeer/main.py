
import streamlit as st
import folium
from streamlit_folium import st_folium

import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import io

import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

"""
# Charging stations Netherlands
"""

data_load_state = st.text('Loading data...')


# Load data from csv file
laadpalen = pd.read_json('./laadpalen.json')
laadpalen_small = pd.read_json('./laadpalen_small.json')
transacties = pd.read_csv('laadpaaldata.csv')

transacties = transacties.query('`ChargeTime` >= 0')

transacties['Ended'] = pd.to_datetime(
    transacties['Ended'], errors='coerce')
transacties['Started'] = pd.to_datetime(
    transacties['Started'], errors='coerce')

data_load_state.text('')

"""
### Raw data
"""

transacties

logscale = st.checkbox("Logarithmic scale")
overlay = st.checkbox("Overlay plots")

if overlay:
    plt.hist(transacties['ConnectedTime'],
             label="Connected time", color="orange")
    plt.hist(transacties['ChargeTime'], label="Charge time", color="blue")
    plt.legend()
else:
    fig, axs = plt.subplots(1, 2, sharey=True, sharex=True)

    axs[0].hist(transacties['ChargeTime'], label="Charge time", color="blue")
    axs[1].hist(transacties['ConnectedTime'],
                label="Connected time", color="orange")
    fig.legend()
if logscale:
    plt.yscale('log')

"""
### Distribution of charging- & connnected times
"""
st.pyplot()

transacties = transacties.sort_values('Ended')

transacties['TotalEnergy_cumm'] = transacties['TotalEnergy'].cumsum()

sns.lineplot(transacties, x='Ended', y='TotalEnergy_cumm')
st.pyplot()

AMSTERDAM_LAT_LONG = (52.377956, 4.897070)

smallSet = st.checkbox("Use small dataset", value=True)

# Create and show empty Folium map
m = folium.Map(location=AMSTERDAM_LAT_LONG, zoom_start=12,
               title="Netherlands charging points")

targetSet = laadpalen_small if smallSet else laadpalen

for index, row in targetSet.iterrows():
    address = row['AddressInfo']

    color = 'green' if row['IsRecentlyVerified'] else 'blue'

    folium.Circle(location=[address['Latitude'], address['Longitude']],
                  tooltip=address['AddressLine1'],
                  color=color
                  ).add_to(m)

"""
Charging stations throughout the Netherlands
"""

st_folium(m)
