from load_data import *
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np

def Deaths():
    df = load_data()

    palestinian_data = df[df['citizenship'] == 'Palestinian']
    israeli_data = df[df['citizenship'] == 'Israeli']

    palestinian_counts = palestinian_data.groupby(df['date_of_event'].dt.year)['citizenship'].count().to_dict()
    israeli_counts = israeli_data.groupby(df['date_of_event'].dt.year)['citizenship'].count().to_dict()

    st.title('Aantal doden in het Palestina - Israel conflict per jaar')

    years = range(df['date_of_event'].dt.year.min(), df['date_of_event'].dt.year.max() + 1)

    years_short = [str(year)[-2:] for year in years]

    palestinian_yearly_counts = []
    israeli_yearly_counts = []

    for year in years:
        palestinian_yearly_counts.append(palestinian_counts.get(year, 0))
        israeli_yearly_counts.append(israeli_counts.get(year, 0))

    bar_width = 0.40
    index = np.arange(len(years))

    fig, ax = plt.subplots()
    ax.bar(index, palestinian_yearly_counts, bar_width, label='Palestinian', alpha=0.8)
    ax.bar(index + bar_width, israeli_yearly_counts, bar_width, label='Israeli', alpha=0.8)

    plt.xticks(index + bar_width / 2, years_short, rotation=45, ha='right')

    ax.set_xlabel('Jaar')
    ax.set_ylabel('Aantal')
    ax.legend()

    if st.checkbox('Logaritmische geschaalde y-as'):
        ax.set_yscale('log')

    st.pyplot(fig)


# Histogram met dropdown per jaar keuze
    st.title('Aantal doden per maand')
    st.sidebar.title('Jaarselectie')

    years = df['date_of_event'].dt.year.unique()
    selected_year = st.sidebar.selectbox('Jaar', years)

    filtered_data = df[df['date_of_event'].dt.year == selected_year]

    monthly_counts_palestinian = filtered_data[filtered_data['citizenship'] == 'Palestinian']['date_of_event'].dt.month.value_counts().sort_index()
    monthly_counts_israeli = filtered_data[filtered_data['citizenship'] == 'Israeli']['date_of_event'].dt.month.value_counts().sort_index()

    months = range(1, 13)
    monthly_counts_palestinian = monthly_counts_palestinian.reindex(months, fill_value=0)
    monthly_counts_israeli = monthly_counts_israeli.reindex(months, fill_value=0)

    st.subheader(f'Aantal doden per maand in {selected_year} (Opdeling: Palestinian vs. Israeli)')
    fig, ax = plt.subplots()
    bar_width = 0.4
    ax.bar(months, monthly_counts_palestinian, width=bar_width, label='Palestinian', alpha=0.8)
    ax.bar([month + bar_width for month in months], monthly_counts_israeli, width=bar_width, label='Israeli', alpha=0.8)
    ax.set_xlabel('Maand')
    ax.set_ylabel('Aantal doden')
    ax.set_xticks([month + bar_width/2 for month in months])
    ax.set_xticklabels(['Jan', 'Feb', 'Mrt', 'Apr', 'Mei', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec'])
    ax.legend()

    st.pyplot(fig)


# Histogram dropdown keuze per maand

    st.title('Aantal doden per dag')
    st.sidebar.title('Selecteer jaar en maand')

    maandnamen = {
        1: 'Januari',
        2: 'Februari',
        3: 'Maart',
        4: 'April',
        5: 'Mei',
        6: 'Juni',
        7: 'Juli',
        8: 'Augustus',
        9: 'September',
        10: 'Oktober',
        11: 'November',
        12: 'December'
    }

    years = df['date_of_event'].dt.year.unique()
    selected_year = st.sidebar.selectbox('Jaar', years, key='year_selectbox')

    months = df['date_of_event'].dt.month.unique()
    selected_month = st.sidebar.selectbox('Maand', list(maandnamen.values()), key='month_selectbox')

    selected_month_number = [k for k, v in maandnamen.items() if v == selected_month][0]

    filtered_data = df[(df['date_of_event'].dt.year == selected_year) & (df['date_of_event'].dt.month == selected_month_number)]

    daily_counts = filtered_data['date_of_event'].dt.day.value_counts().sort_index()

    st.subheader(f'Aantal doden per dag in {selected_month} {selected_year}')
    fig, ax = plt.subplots()
    ax.bar(daily_counts.index, daily_counts.values)
    ax.set_xlabel('Dag')
    ax.set_ylabel('Aantal doden')

    st.pyplot(fig)


#cirkeldiagram doden aantal

    data = [10095, 1029]

    labels = ['Palestijnen', 'Israëliërs']

    st.title('Verdeling van totaal doden aantal')

    fig, ax = plt.subplots()
    ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=140)
    st.pyplot(fig)


#cirkeldiagrammen man/vrouw verhouding

    data_palestinian = df[df['citizenship'] == 'Palestinian']['gender'].value_counts().to_dict()
    data_israeli = df[df['citizenship'] == 'Israeli']['gender'].value_counts().to_dict()

    data_palestinian = {'Vrouw': data_palestinian.get('F', 0), 'Man': data_palestinian.get('M', 0)}
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

    st.title('Man/vrouw verdeling doden')

    col1, col2 = st.columns(2)

    with col1:
        fig_palestinian = create_pie_chart(data_palestinian, 'Man/vrouw verdeling Palestijnse doden')
        st.pyplot(fig_palestinian)

    with col2:
        fig_israeli = create_pie_chart(data_israeli, 'Man/vrouw verdeling Israëlische doden')
        st.pyplot(fig_israeli)






#code voor overzicht totaal doden Israel
    # st.title('Totaal aantal doden per jaar met "Israeli" als nationaliteit')
   # israeli_deaths_per_year = df[df['citizenship'] == 'Israeli'].groupby(df['date_of_event'].dt.year)['citizenship'].count()
   # st.write(israeli_deaths_per_year)
   # totaal aantal doden Israel: 1029
   # totaal aantal doden Palestijn: 10.095

   