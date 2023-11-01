
import streamlit as st
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium, folium_static

from loaddata import *


def mapplot():

    left_col, right_col = st.columns([1, 2])

    with left_col:
        st.markdown(
            """
        ### Charging stations througout the Netherlands
        
        This plot displays an overview of the charging stations in the Netherlands. Data is fetched through the following endpoint: `https://api.openchargemap.io/v3/poi/?output=json&countrycode=NL`.
        Due to the nature of this API, only a limited set of charge points can be fetched at a time. We fetch the data with a limit of 10.000 records, sadly we only receive about 7500 records. 
        This can be due to a limit that's set in the API. 

        However despite the limited data, this plot still gives an overview of the density of chargepoints throughout certain areas of the Netherlands.
        """
        )

    with right_col:
        laadpalen = load_laadpalen()
        laadpalen_small = load_laadpalen_small()

        AMSTERDAM_LAT_LONG = (52.377956, 4.897070)
        NETHERLANDS_LAT_LONG = (52.2129919, 5.2793703)

        smallSet = st.checkbox("Use small dataset", value=False)

        # Create and show empty Folium map
        m = folium.Map(location=NETHERLANDS_LAT_LONG, zoom_start=7,
                       title="Netherlands charging points")

        targetSet = laadpalen_small if smallSet else laadpalen

        cluster = MarkerCluster().add_to(m)
        for index, row in targetSet.iterrows():
            address = row['AddressInfo']

            color = 'green' if row['IsRecentlyVerified'] else 'blue'

            folium.Marker(location=[address['Latitude'], address['Longitude']],
                          tooltip=address['AddressLine1'],
                          color=color
                          ).add_to(cluster)

        """
        Charging stations throughout the Netherlands
        """

        # st_folium(m, width=800, height=500)
        folium_static(m, width=690, height=540)
