#App 1: Web Mapping with Python: Interactive Mapping of Population and Volcanoes

import pandas
import folium

data = pandas.read_csv("app1: web mapping/Volcano.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%s volcano" target="_blank">%s</a><br>
Height: %s m
"""

def elevation(elevation):
        if elevation < 1500:
            color = "blue"
        elif 1500 <= elevation < 2500:
            color = "orange"
        else:
            color = "red"
        return color

map = folium.Map(location=[40.68, -93.9], zoom_start=5, tiles="Stamen Terrain")

fg_v = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, n in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (n, n, el), width=200, height=100)
    fg_v.add_child(folium.Marker(location=[lt, ln], radius=10, popup=folium.Popup(iframe),
    icon=folium.Icon(color=elevation(el))))

fg_p = folium.FeatureGroup(name="Population")

fg_p.add_child(folium.GeoJson(data=open("app1: web mapping/world.json", "r", encoding="UTF-8-sig").read(), 
style_function=lambda x: {"fillColor": "blue" if x["properties"]["POP2005"] < 10000000 
else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))

map.add_child(fg_v)
map.add_child(fg_p)
map.add_child(folium.LayerControl())

map.save("app1: web mapping/Map1.html")
