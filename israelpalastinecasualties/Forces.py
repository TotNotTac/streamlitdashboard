from load_data import *
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np

def Forces():
    df = load_data()

#cirkeldiagrammen man/vrouw
    start_date = '2014-09-01'
    df['date_of_event'] = pd.to_datetime(df['date_of_event']) 
    df_filtered = df[df['date_of_event'] >= start_date]

    data_palestinian = df_filtered[df_filtered['citizenship'] == 'Palestinian']['gender'].value_counts().to_dict()
    data_palestinian = {'Vrouw': data_palestinian.get('F', 0), 'Man': data_palestinian.get('M', 0)}

    data_israeli = df_filtered[df_filtered['citizenship'] == 'Israeli']['gender'].value_counts().to_dict()
    data_israeli = {'Vrouw': data_israeli.get('F', 0), 'Man': data_israeli.get('M', 0)}

    def create_pie_chart(data, title, radius=1.0):
        labels = data.keys()
        sizes = data.values()

        colors = ['#FF69B4', '#1E90FF']

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, radius=radius)
        ax.set_aspect('equal')
        ax.set_title(title)
        return fig

    st.title('Man/vrouw verdeling doden vanaf september 2014')

    col1, col2 = st.columns(2)

    with col1:
        fig_palestinian = create_pie_chart(data_palestinian, 'Man/vrouw verdeling Palestijnse doden')
        st.pyplot(fig_palestinian)

    with col2:
        fig_israeli = create_pie_chart(data_israeli, 'Man/vrouw verdeling Israëlische doden')
        st.pyplot(fig_israeli)
    
    
#horizontale staafdiagrammen
    
    st.title('Moordwapen per groep vanaf het september 2014')

    categories = ['Israeli security forces', 'Palestinian civilians', 'Israeli civilians']

    for category in categories:
        filtered_data = df[df['killed_by'] == category]
    
        grouped_data = filtered_data['ammunition'].value_counts()

        grouped_data = grouped_data.sort_values(ascending=False)

        fig, ax = plt.subplots(figsize=(12, 3))
        grouped_data.plot(kind='barh', ax=ax, color='skyblue')

        plt.title(f'Meest gebruikte moordwapen per {category}')
        plt.xlabel('Aantal gevallen')
        plt.ylabel('Moordwapen')

        st.pyplot(fig)