import folium, pandas

map = folium.Map(location = [38.2, -99.1], zoom_start = 6, tiles = "Stamen Terrain") #lat, lon
fg = folium.FeatureGroup(name = 'my-map')
dfv = pandas.read_csv("volcanoes.txt")

def get_color(elev):
    return "green" if elev < 1000 else "orange" if elev < 3000 else "red"

for i in range(62):
    coord = [float(dfv.loc[i, "LAT"]), float(dfv.loc[i, "LON"])]
    name = str(dfv.loc[i, "NAME"])
    elev = float(dfv.loc[i, "ELEV"])
   
    fg.add_child(folium.CircleMarker(location = coord, radius = 9, popup = name + ": %.2f m" %elev, fill_color = get_color(elev), color = "gray", fill_opacity = 0.6))



map.add_child(fg)
map.save("Web-map.html")


