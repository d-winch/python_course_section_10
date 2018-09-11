import folium
import pandas

map = folium.Map(location=[-54.466499, -36.501811], zoom_start = 10, tiles="OpenStreetMap")#"Mapbox Bright")

fg_vol = folium.FeatureGroup(name="Volcanoes")
fg_pop = folium.FeatureGroup(name="Population")

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

fg_pop.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig'),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else
'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

for lt, ln, nme, el in zip(lat, lon, name, elev):
    #fg.add_child(folium.Marker(location=[lt, ln], popup=nme + "\n" + str(el) +  " m", icon=folium.Icon(color=color_producer(el))))
    fg_vol.add_child(folium.features.CircleMarker(
        location=[lt, ln],
        radius=5,
        fill_opacity=0.7,
        popup=nme + "\n" + str(el) +  " m",
        color='grey',
        fill_color=color_producer(el)))

map.add_child(fg_pop)
map.add_child(fg_vol)
map.add_child(folium.LayerControl())
map.save("map.html")
