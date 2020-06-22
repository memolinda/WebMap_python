'''Create a Webmap in Python using Folium (from the The Python Mega Course)'''


import folium
import pandas as pd

#### Import data from a csv file
data = pd.read_csv("vulcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

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
for lt, ln, el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln], popup=str(el)+ " m",
                    icon=folium.Icon(color='green')))


map.add_child(fg)
 #### Save the map in an htlm file to load it with the browser
map.save("Map1.html")
