"""GIS Application that takes a txt file as input contating coordinates of Volcanoes in US and outputs their
locations on the world map"""

""Author: Rissalat A. Kapdi
  Date: 25/12/18"""

#imported libraries
import folium #folium builds on the data wrangling strengths of the Python ecosystem and the mapping strengths of the Leaflet.js library. Manipulate your data in Python, then visualize it in a Leaflet map via folium.
import pandas #pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#folium does not have native functionality to create dynamic color so the program uses python
#colour functionality to create color tags in the following function
#The function differentiates elevation by cateogrizing into particular colors based on elevation
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'
map = folium.Map(location=[48.463669, -123.312113], zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
        fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el) + " m",
        fill_color = color_producer(el), color  ='grey', fill_opacity= 0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
 style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000
 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
