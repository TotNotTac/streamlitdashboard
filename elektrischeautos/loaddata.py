
import streamlit as st

import pandas as pd


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
