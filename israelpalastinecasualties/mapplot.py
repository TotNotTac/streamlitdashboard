from io import BytesIO
import streamlit as st
from util import date_filter

from load_data import load_data
import pandas as pd
import json
import folium
import streamlit_folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static, st_folium
from folium.plugins import HeatMap
import base64


def mapPlot():

    deaths = load_data()

    objs = []
    with open("locations.json", "r") as f:
        objs = json.load(f)

    featuresRaw = []
    for x in objs:
        if len(x['features']) < 1:
            continue
        row = x['features'][0]['properties']
        row['originalQuery'] = x['originalQuery']
        featuresRaw.append(row)

    features = pd.DataFrame(featuresRaw)
    features = features[['lon', 'lat', 'formatted',
                         'originalQuery']]

    markerType = st.selectbox("Choose point style", ["Circles", "Markers"])

    m = folium.Map(location=(31.877927200212394,
                   35.06102832103248), zoom_start=7)
    # m = folium.Map(location=(31.877927200212394,
    #                35.06102832103248), zoom_start=7, tiles='https://{s}.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}{r}.png', attr='CartoDB.Voyager')

    # folium.TileLayer('Mapbox Bright').add_to(m)
    if markerType == "Markers":
        cluster = MarkerCluster().add_to(m)

    for i, row in features.iterrows():
        match markerType:
            case "Markers":
                folium.Marker(
                    location=[row['lat'], row['lon']]).add_to(cluster)
            case "Circles":
                folium.Circle(
                    location=[row['lat'], row['lon']]).add_to(m)
    folium_static(m, width=400, height=600)

    ###

    withLocations = pd.merge(
        deaths, features, left_on='event_location', right_on='originalQuery')

    m = folium.Map(location=(31.877927200212394,
                   35.06102832103248), zoom_start=7)

    markerType = st.selectbox("Choose point style", ["Markers", "Heatmap"])
    withLocations = date_filter(withLocations)

    if markerType == "Markers":
        cluster = MarkerCluster().add_to(m)

    match markerType:
        case "Markers":
            for i, row in withLocations.iterrows():
                popup = """
                        <div>
                            <div><label>name:&nbsp</label>{name}</div>
                            <div><label>age:&nbsp</label>{age}</div>
                            <div><label>date:&nbsp</label>{date}</div>
                            <div><label>place:&nbsp</label>{place}</div>
                            <div><label>citizenship:&nbsp</label>{citizenship}</div>
                            <div><label>type of injury:&nbsp</label>{injury}</div>
                            <div><label>killed by:&nbsp</label>{killed_by}</div>
                            <div><label>notes:&nbsp</label>{notes}</div>
                        </div>
                        """.format(name=row['name'],
                                   age=row['age'],
                                   date=row['date_of_death'],
                                   place=row['originalQuery'],
                                   citizenship=row['citizenship'],
                                   injury=row['type_of_injury'],
                                   killed_by=row['killed_by'],
                                   notes=row['notes']
                                   )

                folium.Marker(
                    location=[row['lat'], row['lon']
                              ], popup=folium.Popup(popup, max_width=1000)).add_to(cluster)
        case "Heatmap":
            heat_data = [[row['lat'], row['lon']]
                         for index, row in withLocations.iterrows()]
            HeatMap(heat_data).add_to(m)
    folium_static(m, width=1080, height=600)
