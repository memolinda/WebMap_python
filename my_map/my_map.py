import folium
import json
import pandas as pd

### Create DataFrame from json files
df_home = pd.read_json("my_data/Home.json")
df_life = pd.read_json("my_data/Life.json")
df_work = pd.read_json("my_data/Work.json")

### Map centered in Berlin
map = folium.Map(location=[52.528917, 13.331167],
                zoom_start=4, tiles= 'Stamen Watercolor')

### Addresses for the pop up windows: City name, description, pictures
html_home = """<div style="Font-family: arial;">
<strong>%s</strong> (%s): <br>
%s. <br>
Pictures:<br>
<a href="https://www.google.com/search?q=%%22%s%%22&tbm=isch&ved" target="_blank">%s</a></div>
"""

html_life = """<div style="Font-family: arial;">
<strong>%s</strong> (%s): <br>
Pictures:<br>
<a href="https://www.google.com/search?q=%%22%s%%22&tbm=isch&ved" target="_blank">%s</a></div>
"""

ff_home = folium.FeatureGroup(name="Home")
ff_life = folium.FeatureGroup(name="Life")
ff_work = folium.FeatureGroup(name="Work")


for index, row in df_home.iterrows():
    iframe = folium.IFrame(html=html_home % (row['City'], row['Country'], row['Description'], row['City'], row['City']), width=200, height=100)
    ff_home.add_child(folium.Marker(location=[row['Lat'],row['Lon']], popup=folium.Popup(iframe), icon=folium.Icon(color='red', icon='home', prefix='fa')))

for index, row in df_life.iterrows():
    iframe = folium.IFrame(html=html_life % (row['City'], row['Country'], row['City'], row['City']), width=200, height=100)
    ff_life.add_child(folium.Marker(location=[row['Lat'],row['Lon']], popup=folium.Popup(iframe), icon=folium.Icon(color='green', icon='gratipay', prefix='fa')))

for index, row in df_work.iterrows():
    iframe = folium.IFrame(html=row['Site'], width=200, height=100)
    ff_work.add_child(folium.Marker(location=[row['Lat'],row['Lon']], popup=folium.Popup(iframe), icon=folium.Icon(color='blue', icon='briefcase', prefix='fa')))

map.add_child(ff_home)
map.add_child(ff_life)
map.add_child(ff_work)


map.add_child(folium.LayerControl())

map.save("My_map.html")
