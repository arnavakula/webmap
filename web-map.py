import folium, pandas

map = folium.Map(location = [38.2, -99.1], zoom_start = 6, tiles = "Stamen Terrain") #lat, lon
fg = folium.FeatureGroup(name = 'my-map')
dfv = pandas.read_csv("volcanoes.txt")


for i in range(62):
    fg.add_child(folium.Marker(location = [float(dfv.loc[i, "LAT"]), dfv.loc[i, "LON"]], popup = dfv.loc[i, "NAME"], icon = folium.Icon(color = 'cadetblue')))



map.add_child(fg)
map.save("Web-map.html")


