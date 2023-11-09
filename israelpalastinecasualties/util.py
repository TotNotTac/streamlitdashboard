import streamlit as st
import pandas as pd


def date_filter(df):
    df['date_of_event'] = pd.to_datetime(
        df['date_of_event']).dt.to_pydatetime()

    minDate = df['date_of_event'].min().to_pydatetime()
    maxDate = df['date_of_event'].max().to_pydatetime()
    dateRange = st.slider('select a date range', min_value=minDate,
                          max_value=maxDate, value=(minDate, maxDate))

    return df.query(
        f'`date_of_event` >= "{dateRange[0]}" and `date_of_event` <= "{dateRange[1]}"')
