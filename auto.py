import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#histogram van aantal EV merken
st.title("Meestvoorkomende EV auto's op de Nederlandse wegen")

file_path = 'Elektrische_voertuigen_20231030.csv'

df = pd.read_csv(file_path)

merk_counts = df['Merk'].value_counts()
filtered_merken = merk_counts[merk_counts > 1500].index
df_filtered = df[df['Merk'].isin(filtered_merken)]

df_filtered['Merk'] = pd.Categorical(df_filtered['Merk'], categories=merk_counts.index, ordered=True)
df_filtered = df_filtered.sort_values(by='Merk')

plt.figure(figsize=(10, 6))
ax = sns.histplot(data=df_filtered, x='Merk', discrete=True)
ax.set(xlabel="EV merk", ylabel="Aantal")
plt.xticks(rotation=90)
st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False)

#statement over gemiddelde prijs auto's Nederland
st.write("<h1><em>De gemiddelde prijs voor een EV auto is €53.519,64</em></h1>", unsafe_allow_html=True)

#histogram van gemiddelde prijs per merk
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

st.title("Gemiddelde catalogusprijs per merk")

file_path = 'Elektrische_voertuigen_20231030.csv'

df = load_data(file_path)

geselecteerde_merken = ['TESLA', 'VOLKSWAGEN', 'KIA', 'HYUNDAI', 'AUDI', 'PEUGEOT', 'RENAULT', 'SKODA', 'BMW', 'OPEL', 'VOLVO']

df_filtered = df[df['Merk'].isin(geselecteerde_merken)]

gemiddelde_catalogusprijs_per_merk = df_filtered.groupby('Merk')['Catalogusprijs'].mean().reset_index().sort_values('Catalogusprijs')

colors = sns.color_palette("viridis", len(gemiddelde_catalogusprijs_per_merk))

fig, ax = plt.subplots()
ax.bar(gemiddelde_catalogusprijs_per_merk['Merk'], gemiddelde_catalogusprijs_per_merk['Catalogusprijs'], color=colors)
plt.xlabel("Merk")
plt.ylabel("Catalogusprijs (in euro's)")
plt.xticks(rotation=45)

# Plaats een rode lijn op de gemiddelde catalogusprijs van alle merken
ax.hlines(y=df['Catalogusprijs'].mean(), xmin=-0.5, xmax=len(geselecteerde_merken)-0.5, linewidth=2, color='r')

st.pyplot(fig)
