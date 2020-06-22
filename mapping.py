import folium

 #### Create a map centered to the latitude and logitide with initial zoom of 6
map = folium.Map(location=[59.263794608921565, 18.021744513185972], zoom_start=6)

 #### Save the map in an htlm file to load it with the browser
map.save("Map1.html")
