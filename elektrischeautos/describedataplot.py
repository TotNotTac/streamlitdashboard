
import streamlit as st
from loaddata import *


def describe_dataframe(df: pd.DataFrame, i):
    raw = st.checkbox("Show raw data", key=f"rawData-{i}")
    if not raw:
        st.write(df.describe())
    else:
        st.write(df)


def describe_data_plot():
    st.markdown("""
                ## Raw data
                """)

    voertuig_tab, transacties_tab, laadpalen_tab, laadpalen_small_tab = st.tabs(
        ["Voertuigen", "Transacties", "Laadpalen", "Laadpalen small"])

    with voertuig_tab:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""
            ### Electric vehicles
            This dataset contains data of electric vehicles sold within the Netherlands.
            """)
        with col2:
            voertuigen = load_elektrische_voertuigen()
            describe_dataframe(voertuigen, 1)

    with transacties_tab:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""
            This dataset contains data of charging transactions made in the Netherlands made between 2018-01-01 and 2018-12-31.
            Every row contains important information about the transaction like the energy charged and how long the charger was 
                        connected.
            """)
        with col2:
            transacties = load_transactions()
            describe_dataframe(transacties, 2)

    with laadpalen_tab:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""
            The following dataset contains a limited amount of charge points located in the Netherlands.
            """)
        with col2:
            laadpalen = load_laadpalen()
            describe_dataframe(laadpalen, 3)

    with laadpalen_small_tab:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""
            The following dataset contains an even smaller amount of charge points located in the Netherlands.
            """)
        with col2:
            laadpalen_small = load_laadpalen_small()
            describe_dataframe(laadpalen_small, 4)
