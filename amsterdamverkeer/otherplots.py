
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


def otherplots():
    data_load_state = st.text('Loading data...')

    # Load data from csv file
    transacties = load_transactions()
    voertuigen = load_elektrische_voertuigen()

    data_load_state.text('')
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(
            """
            ## Price of cars in the transactions dataset
            While the price of electric cars can heavily vary, this plot clearly shows that the average electric-andy not buy
            overly expensive cars. With a median of 47.8 thousand euros, the mid range is by far the most popular price-category
            for electric car drivers. Curiously some really expensive cars also show up in this dataset. 
            """)

    with col2:
        fig = px.histogram(voertuigen, x="Catalogusprijs", marginal="box")

        st.plotly_chart(fig)  # ``, use_container_width=True)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(
            """
            ## Total energy charged in the transactions dataset
            This plot shows the distribution of energy charged during a transaction. 
            As expected there is some variance in the distribution, with a median of 7kW charged and a std2 of almost 19 kW.

            Notable is that there is points all the way up and between the upper limit of 80kW.
            """)

    with col2:
        fig = px.histogram(transacties, x="TotalEnergy", marginal="box")
        st.plotly_chart(fig)  # ``, use_container_width=True)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(
            """
            ## Charge time in the transactions dataset
            Something that is immidiatly noticable in this plot is the existence of two large peaks; 
            one for people that charge for about 2.5 hours and one for people that charge for about 3.8 hours.

            My working hypothesis is that this can be explained by people disconnecting their car before and after lunch
            while charging at work.
            """)
    with col2:
        fig = px.histogram(transacties, x="ChargeTime", marginal="box")
        st.plotly_chart(fig)  # ``, use_container_width=True)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(
            """
            ## Connected time in the transactions dataset
            While this dataset has some noticable extremes too, it's less clear to me what these extremes could mean.
            I feel like the second and thirt peak _can_ be explained by charging overnight on work weeks and 
            charging overnight on the weekends.
            """)

    with col2:
        fig = px.histogram(transacties, x="ConnectedTime", marginal="box")
        st.plotly_chart(fig)  # ``, use_container_width=True)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(
            """
            ## Max possible power in the transactions dataset
            This plot shows the max power of cars in the transaction dataset. 
            There is one very clear peak, and some barely noticable, smaller peaks. I feel like these peaks could be 
            better explained if we had more information about what type of car the transaction belongs to. 
            """)
    with col2:
        fig = px.histogram(transacties, x="MaxPower", marginal="box")
        st.plotly_chart(fig)  # ``, use_container_width=True)
