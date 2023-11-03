
import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    df = pd.read_csv('./fatalities_isr_pse_conflict_2000_to_2023.csv')
    df['date_of_event'] = pd.to_datetime(df['date_of_event'])
    df['date_of_death'] = pd.to_datetime(df['date_of_death'])
    return df
