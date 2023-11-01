import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from loaddata import load_elektrische_voertuigen


def auto_plot():

    # histogram van aantal EV merken
    st.markdown("""
    ### Meest voorkomende electrische automerken
    """)

    # file_path = 'Elektrische_voertuigen_20231030.csv'

    # df = pd.read_csv(file_path)

    df = load_elektrische_voertuigen()

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("""
        De Tesla is minstens twee keer zo populair in vergelijking met alle andere EV voertuigen in Nederland op Volkswagen na. Reden hiervoor zou kunnen zijn dat de Tesla bekend staat om zijn grote actieradius en hoge comfort.
            """)

    with col2:
        merk_counts = df['Merk'].value_counts()
        filtered_merken = merk_counts[merk_counts > 1500].index
        df_filtered = df[df['Merk'].isin(filtered_merken)]

        df_filtered['Merk'] = pd.Categorical(
            df_filtered['Merk'], categories=merk_counts.index, ordered=True)
        df_filtered = df_filtered.sort_values(by='Merk')

        plt.figure(figsize=(10, 6))
        plt.title("Aantal voertuigen per merk")
        ax = sns.histplot(data=df_filtered, x='Merk', discrete=True)
        ax.set(xlabel="EV merk", ylabel="Aantal")
        plt.xticks(rotation=90)
        st.pyplot()

        st.set_option('deprecation.showPyplotGlobalUse', False)

        # statement over gemiddelde prijs auto's Nederland

        # file_path = 'Elektrische_voertuigen_20231030.csv'


####
    df = load_elektrische_voertuigen()

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("""
                De gemiddelde prijs voor een EV auto is €53.519,64
                    """)
    with col2:
        geselecteerde_merken = ['TESLA', 'VOLKSWAGEN', 'KIA', 'HYUNDAI',
                                'AUDI', 'PEUGEOT', 'RENAULT', 'SKODA', 'BMW', 'OPEL', 'VOLVO']

        df_filtered = df[df['Merk'].isin(geselecteerde_merken)]

        gemiddelde_catalogusprijs_per_merk = df_filtered.groupby(
            'Merk')['Catalogusprijs'].mean().reset_index().sort_values('Catalogusprijs')

        colors = sns.color_palette("viridis", len(
            gemiddelde_catalogusprijs_per_merk))

        fig, ax = plt.subplots()
        ax.set_title("Gemiddelde catalogusprijs per merk")
        ax.bar(gemiddelde_catalogusprijs_per_merk['Merk'],
               gemiddelde_catalogusprijs_per_merk['Catalogusprijs'], color=colors)
        plt.xlabel("Merk")
        plt.ylabel("Catalogusprijs (in euro's)")
        plt.xticks(rotation=45)

        # Plaats een rode lijn op de gemiddelde catalogusprijs van alle merken
        ax.hlines(y=df['Catalogusprijs'].mean(), xmin=-0.5,
                  xmax=len(geselecteerde_merken)-0.5, linewidth=2, color='r')

        # histogram van gemiddelde prijs per merk
        st.pyplot(fig)
