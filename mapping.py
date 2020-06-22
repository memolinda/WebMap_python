'''Create a Webmap in Python using Folium (from the The Python Mega Course)'''


import folium

 #### Create a base map object with folium centered to the latitude and logitide
 #### with initial zoom of 6 and a layer on top (Stamen Terrain layer)
map = folium.Map(location=[59.263794608921565, 18.021744513185972], zoom_start=6,
                tiles = "Stamen Terrain")

#### Add a child to the map with markers
map.add_child(folium.Marker(location=[59.10, 18.1], popup="Hi!!", icon=folium.Icon(color='green')))

 #### Save the map in an htlm file to load it with the browser
map.save("Map1.html")
