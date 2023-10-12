import folium

AMSTERDAM_LAT_LONG = (52.377956, 4.897070)


def map(df):
    # Create and show empty Folium map
    m = folium.Map(location=AMSTERDAM_LAT_LONG, zoom_start=12,
                   title="Amsterdam tram and metro")

    for index, row in df.iterrows():
        # Add markers, no idea what data this is
        # folium.Marker(location=[row.LAT, row.LNG], tooltip=f"{row.Modaliteit} {row.Lijn}").add_to(m)

        lijnen = row.Lijn.split("|")
        lijnen = [x.strip() for x in lijnen]

        coordinaten = row.WKT_LAT_LNG[11:-1].split(",")

        line = []
        for lat_long_str in coordinaten:
            coords = lat_long_str.split(" ")
            line.append((float(coords[0]), float(coords[1])))

        folium.PolyLine(line, tooltip=f"{row.Modaliteit} {row.Lijn}").add_to(m)

    return m
