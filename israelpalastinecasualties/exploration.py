
from matplotlib import pyplot as plt
from util import date_filter
from load_data import *
import plotly.express as px
import pandas as pd
import seaborn as sns
from wordcloud import WordCloud

DEFAULT_COLS = [1, 1]


def exploration_plot():
    df = load_data()

    st.markdown("""
    ## Fatalities in the Israeli-Palestinian conflict

    """)
    col1, col2 = st.columns(DEFAULT_COLS)
    allText = df['notes'].str.cat(sep='. ')
    with col1:
        st.markdown("""
                ### Raw data
                    """)
        st.write(df)
    with col2:
        st.markdown("""
                ### Sentiment
                    """)
        wordcloud = WordCloud(max_font_size=320, height=2000,
                              width=3200).generate(allText)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()

        # sentiment_pipeline = pipeline("sentiment-analysis")
        # result = sentiment_pipeline(allText)
        # st.write(result)

    df = df.drop("name", axis=1)
    df = df.drop("notes", axis=1)

    col1, col2 = st.columns(DEFAULT_COLS)
    with col1:
        st.markdown("""
        ### Coorolation matrix for different variables in the dataset

        """)
    with col2:
        removeDates = st.checkbox("Remove dates", value=True)
        if removeDates:
            df = df.drop("date_of_event", axis=1)
            df = df.drop("date_of_death", axis=1)

        corr = df.apply(lambda x: pd.factorize(x)[0]).corr(method="pearson")
        sns.heatmap(corr)
        st.pyplot()

    df = load_data()
    df = date_filter(df)

    col1, col2 = st.columns(2)
    with col1:
        ax = sns.histplot(df, x="citizenship")
        ax.bar_label(ax.containers[0])
        st.pyplot()
    with col2:
        ax = sns.histplot(df, x="killed_by")
        ax.bar_label(ax.containers[0])
        st.pyplot()

    # df['totalDeaths'] = 1
    # df['totalDeaths'] = df['totalDeaths'].cumsum()

    # fig = px.histogram(df, x="citizenship",
    #                    animation_frame="date_of_death", animation_group='citizenship', cumulative=True, facet_col="citizenship")
    # st.plotly_chart(fig)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        """)
    with col2:
        sns.histplot(df, x="type_of_injury", hue="type_of_injury")
        plt.xticks(rotation=-90)
        plt.yscale("log")
        plt.legend([], [], frameon=False)
        st.pyplot()
