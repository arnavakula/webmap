import folium

map = folium.Map(location = [38.2, -99.1], zoom_start = 6, tiles = "Stamen Terrain") #lat, lon
fg = folium.FeatureGroup(name = 'my-map')

for coordinates in [[38.2, -99.1], [39.2, -97.1]]:
    fg.add_child(folium.Marker(location = coordinates, popup = "Testing marker", icon = folium.Icon(color = 'red')))

map.add_child(fg)
map.save("Web-map.html")

