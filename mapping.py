'''Create a Webmap in Python using Folium (from the The Python Mega Course)'''


import folium
import pandas as pd

#### Import data from a csv file
data = pd.read_csv("vulcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

###Link on the popup windows
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

#### Color markers depending of the elevation
def color_icons(elev):
    if elev < 1000:
        return 'green'
    elif elev>=1000 and elev<2000:
        return 'orange'
    else:
        return 'red'

 #### Create a base map object with folium centered to the latitude and logitide
 #### with initial zoom of 6 and a layer on top (Stamen Terrain layer)
map = folium.Map(location=[45, -100],
                zoom_start=6, tiles = "Stamen Terrain")

#### Add a child to the map with markers
fg = folium.FeatureGroup(name="My Map") # features creation

### multiple markers
# for coordinates in [[59.1, 18.01], [58.8, 17.5]]:
#     fg.add_child(folium.Marker(location=coordinates, popup="Home",
#                 icon=folium.Icon(color='green')))

### Extract latitude and logitude from the csv
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100) #add the elevation and the link
    fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe),
                    icon=folium.Icon(color=color_icons(el))))


map.add_child(fg)
 #### Save the map in an htlm file to load it with the browser
map.save("Map1.html")
