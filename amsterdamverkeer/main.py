
import streamlit as st
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import io

import seaborn as sns


@st.cache_data
def load_transactions():
    transacties = pd.read_csv('laadpaaldata.csv')

    transacties = transacties.query('`ChargeTime` >= 0')

    transacties['Ended'] = pd.to_datetime(
        transacties['Ended'], errors='coerce')
    transacties['Started'] = pd.to_datetime(
        transacties['Started'], errors='coerce')
    return transacties


@st.cache_data
def load_laadpalen():
    return pd.read_json('./laadpalen.json')


@st.cache_data
def load_laadpalen_small():
    return pd.read_json('./laadpalen_small.json')


@st.cache_data
def load_elektrische_voertuigen():
    return pd.read_csv('./Elektrische_voertuigen_20231030.csv')


st.set_option('deprecation.showPyplotGlobalUse', False)

"""
# Charging stations Netherlands
"""

data_load_state = st.text('Loading data...')


# Load data from csv file
laadpalen = load_laadpalen()
laadpalen_small = load_laadpalen_small()
transacties = load_transactions()
voertuigen = load_elektrische_voertuigen()

data_load_state.text('')

"""
### Raw data
"""

voertuigen

# transacties

sns.histplot(transacties, x="TotalEnergy")
st.pyplot()

sns.boxplot(transacties, x="TotalEnergy")
st.pyplot()

sns.boxplot(transacties, x="ConnectedTime")
st.pyplot()

sns.boxplot(transacties, x="ChargeTime")
st.pyplot()

sns.boxplot(transacties, x="MaxPower")
st.pyplot()

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

smallSet = st.checkbox("Use small dataset", value=False)

# Create and show empty Folium map
m = folium.Map(location=AMSTERDAM_LAT_LONG, zoom_start=12,
               title="Netherlands charging points")

targetSet = laadpalen_small if smallSet else laadpalen


cluster = MarkerCluster().add_to(m)
for index, row in targetSet.iterrows():
    address = row['AddressInfo']

    color = 'green' if row['IsRecentlyVerified'] else 'blue'

    folium.Marker(location=[address['Latitude'], address['Longitude']],
                  tooltip=address['AddressLine1'],
                  color=color
                  ).add_to(cluster)

"""
Charging stations throughout the Netherlands
"""

st_folium(m)
