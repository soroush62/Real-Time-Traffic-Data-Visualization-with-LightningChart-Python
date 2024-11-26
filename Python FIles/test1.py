import lightningchart as lc
import random

with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

# Create a map chart
map_chart = lc.MapChart(map_type='World', theme=lc.Themes.Light)

# Add region data to color regions based on some values (optional)
region_data = [
    {'ISO_A3': 'USA', 'value': 350},
    {'ISO_A3': 'BRA', 'value': 180},
    {'ISO_A3': 'IND', 'value': 220},
    {'ISO_A3': 'CHN', 'value': 300},
    {'ISO_A3': 'RUS', 'value': 200},
    {'ISO_A3': 'ZAF', 'value': 100},
]
map_chart.invalidate_region_values(region_data)

# Set a palette for region coloring (optional)
map_chart.set_palette_coloring(
    steps=[
        {'value': 0, 'color': lc.Color('blue')},
        {'value': 200, 'color': lc.Color('yellow')},
        {'value': 350, 'color': lc.Color('red')},
    ],
    look_up_property='value',
    percentage_values=False
)

# Create a ChartXY to overlay scatter points or bubbles
bubble_chart = lc.ChartXY(theme=lc.Themes.Light)
# bubble_chart.set_background_fill_style(lc.emptyFill)
# bubble_chart.set_background_stroke_style(lc.emptyLine)
bubble_chart.get_default_x_axis().dispose()  # Hide X-axis
bubble_chart.get_default_y_axis().dispose()  # Hide Y-axis

# Add a bubble series for points on the map
bubble_series = bubble_chart.add_point_series(sizes=True)
bubble_series.set_palette_point_coloring(
    steps=[
        {'value': 0, 'color': lc.Color('green')},
        {'value': 100, 'color': lc.Color('yellow')},
        {'value': 200, 'color': lc.Color('red')},
    ],
    look_up_property='value',
    percentage_values=False
)

# Generate random bubble data (latitude, longitude, size, and intensity)
bubble_data = [
    {'x': -100, 'y': 40, 'size': 50, 'value': 150},  # Example: USA
    {'x': -60, 'y': -10, 'size': 40, 'value': 100},  # Example: Brazil
    {'x': 78, 'y': 20, 'size': 30, 'value': 200},  # Example: India
    {'x': 116, 'y': 40, 'size': 60, 'value': 300},  # Example: China
    {'x': 37, 'y': 55, 'size': 20, 'value': 180},  # Example: Russia
    {'x': 22, 'y': -30, 'size': 25, 'value': 90},  # Example: South Africa
]

# Map data points to the bubble series
bubble_series.add(
    x=[point['x'] for point in bubble_data],
    y=[point['y'] for point in bubble_data],
    sizes=[point['size'] for point in bubble_data],
    lookup_values=[point['value'] for point in bubble_data],
)

# Open both charts
map_chart.open()
bubble_chart.open()
