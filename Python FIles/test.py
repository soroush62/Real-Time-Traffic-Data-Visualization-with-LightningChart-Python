import lightningchart as lc
from lightningchart.ui import Color
import pandas as pd

# Set LightningChart license
with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

# Create the map chart
chart = lc.MapChart(map_type='Europe', theme=lc.Themes.Light, title="Flight Route Visualization")

# Define flight routes with latitude and longitude
flight_routes = [
    {"from": (48.8566, 2.3522), "to": (52.5200, 13.4050)},  # Paris -> Berlin
    {"from": (41.9028, 12.4964), "to": (48.8566, 2.3522)},  # Rome -> Paris
    {"from": (55.7558, 37.6173), "to": (48.8566, 2.3522)},  # Moscow -> Paris
    {"from": (40.4168, -3.7038), "to": (41.9028, 12.4964)},  # Madrid -> Rome
    {"from": (51.1657, 10.4515), "to": (40.4168, -3.7038)},  # Germany -> Spain
]

# Add flight routes as markers and straight lines
for route in flight_routes:
    # Plot the flight route as a straight line
    chart.add_line_series(
        points=[
            {'latitude': route["from"][0], 'longitude': route["from"][1]},
            {'latitude': route["to"][0], 'longitude': route["to"][1]},
        ],
        color=Color('#FF0000'),  # Red for routes
        width=2,
    )
    
    # Add departure and arrival markers
    chart.add_point_series(latitude=route["from"][0], longitude=route["from"][1], color=Color('blue'), size=7)
    chart.add_point_series(latitude=route["to"][0], longitude=route["to"][1], color=Color('green'), size=7)

# Open the chart
chart.open()
