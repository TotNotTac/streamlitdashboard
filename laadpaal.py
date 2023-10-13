import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('laadpaaldata (1).csv')

laadtijden = data['ChargeTime']

min_laadtijd = int(min(laadtijden))
max_laadtijd = int(max(laadtijden))
bins = range(min_laadtijd, max_laadtijd + 2, 1)

st.subheader("Staafdiagram van Laadtijden")
plt.hist(laadtijden, bins=bins, edgecolor='k')
#plt.xticks(range(min_laadtijd, max_laadtijd + 1), rotation=90)  # Aantal laaduren per 1 uur
plt.xlabel('ChargeTime (uren)')
plt.ylabel('Aantal auto\'s')
st.pyplot(plt)