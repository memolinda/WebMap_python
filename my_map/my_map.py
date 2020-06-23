import folium
import json

home_data = json.load(open("my_data/Home.json"))
home_city = home_data['City']
home_country = home_data['Country']
home_desc = home_data['Description']
home_lat = home_data['Lat']
home_lon = home_data['Lon']

### Map centered in Berlin
map = folium.Map(location=[52.528917, 13.331167],
                zoom_start=4, tiles= 'Stamen Watercolor')

### Addresses for the pop up windows: City name, description, pictures
html = """<div style="Font-family: arial;">
<strong>%s</strong> (%s): <br>
%s. <br>
Pictures:<br>
<a href="https://www.google.com/search?q=%%22%s%%22&tbm=isch&ved" target="_blank">%s</a></div>
"""


ff_home = folium.FeatureGroup(name="Home")
for name, country, desc, lat, lon in zip(home_city, home_country, home_desc, home_lat, home_lon):
    iframe = folium.IFrame(html=html % (name, country, desc, name, name), width=200, height=100)
    ff_home.add_child(folium.Marker(location=[lat,lon], popup=folium.Popup(iframe), icon=folium.Icon(color='red', icon='home', prefix='fa')))

map.add_child(ff_home)
map.add_child(folium.LayerControl())

map.save("My_map.html")
