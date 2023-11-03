
from load_data import *
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

DEFAULT_COLS = [1, 1]


def exploration_plot():
    df = load_data()
    df = df.drop("name", axis=1)
    df = df.drop("notes", axis=1)

    col1, col2 = st.columns(DEFAULT_COLS)
    with col1:
        st.markdown("""
        ## Fatalities in the Israeli-Palestinian conflict

        """)
    with col2:
        st.write(df)

    col1, col2 = st.columns(DEFAULT_COLS)
    with col1:
        st.markdown("""
        ### Coorolation matrix for different variables in the dataset
        
        """)
    with col2:
        corr = df.apply(lambda x: pd.factorize(x)[0]).corr(method="pearson")
        sns.heatmap(corr)
        st.pyplot()
