import folium, pandas

map = folium.Map(location = [38.2, -99.1], zoom_start = 6) #lat, lon
markers = folium.FeatureGroup(name = 'Volcano Markers')
pops = folium.FeatureGroup(name = 'Population')
dfv = pandas.read_csv('volcanoes.txt')

def get_marker_color(elev):
    return 'green' if elev < 1000 else 'orange' if elev < 3000 else 'red'

def get_pop_color(pop):
    return {'fillColor':'yellow'} if pop < 10000000 else {'fillColor':'orange'} if pop < 20000000 else {'fillColor':'red'}

for i in range(62):
    coord = [float(dfv.loc[i, 'LAT']), float(dfv.loc[i, 'LON'])]
    name = str(dfv.loc[i, 'NAME'])
    elev = float(dfv.loc[i, 'ELEV'])
   
    markers.add_child(folium.CircleMarker(location = coord, radius = 7, popup = name + ': %.2f m' %elev, fill_color = get_marker_color(elev), color = 'gray', fill_opacity = 0.6))

pops.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(), style_function = lambda x : get_pop_color(x['properties']['POP2005'])))

map.add_child(markers)
map.add_child(pops)
map.add_child(folium.LayerControl())
map.save('Web-map.html')


