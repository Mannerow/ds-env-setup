# %%

import folium

# Create a map centered at a specific latitude and longitude
m = folium.Map(location=[48.4284, -123.3656], zoom_start=12)

# Add a marker (optional)
folium.Marker([48.4284, -123.3656], popup="Victoria, BC").add_to(m)

# Save the map to an HTML file
m.save("map.html")

print("Map has been saved to map.html")