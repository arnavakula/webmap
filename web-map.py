import folium

map = folium.Map(location = [38.2, -99.1], tiles = "Stamen Terrain") #lat, lon

map.save("Web-map.html")

