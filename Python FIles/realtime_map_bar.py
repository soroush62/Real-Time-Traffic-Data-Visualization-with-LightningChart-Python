# import pandas as pd
# import lightningchart as lc
# import time
# import warnings

# # Suppress warnings
# warnings.filterwarnings("ignore", category=UserWarning)
# warnings.filterwarnings("ignore", category=FutureWarning)

# # Set LightningChart license
# with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
#     mylicensekey = f.read().strip()
# lc.set_license(mylicensekey)

# # Load flight dataset
# file_path = 'Dataset/merged_international_report.xlsx'
# data = pd.read_excel(file_path)

# # Filter data to ensure validity
# data = data[data['Total_Flights'] > 0].dropna(subset=['Total_Flights'])

# # Prepare pivot table for flights by country and year
# pivot_flights = data.pivot_table(index='Year', columns='fg_apt', values='Total_Flights', aggfunc='sum', fill_value=0)
# countries = pivot_flights.columns
# years = pivot_flights.index

# # Create dashboard with two rows: Bar chart and Map chart
# dashboard = lc.Dashboard(theme=lc.Themes.CyberSpace, rows=2, columns=1)
# bar_chart = dashboard.BarChart(row_index=0, column_index=0)
# map_chart = dashboard.MapChart(row_index=1, column_index=0)

# # Update charts for a given year
# def update_charts_for_year(year, data):
#     # Update bar chart
#     bar_chart.set_title(f'Historical Flight Distribution by Country in Year {year}')
#     bar_chart.set_data(data)

#     # Update map chart
#     map_chart.invalidate_region_values([{"ISO_A3": item["category"], "value": item["value"]} for item in data])
#     map_chart.set_title(f'Historical Flight Intensity - Year {year}')

#     # Set color palettes for charts
#     bar_chart.set_palette_colors(
#         steps=[
#             {'value': 0, 'color': lc.Color(0, 0, 255)},      # Blue
#             {'value': 1000, 'color': lc.Color(0, 255, 0)},   # Green
#             {'value': 5000, 'color': lc.Color(255, 255, 0)}, # Yellow
#             {'value': 10000, 'color': lc.Color(255, 165, 0)},# Orange
#             {'value': 50000, 'color': lc.Color(255, 0, 0)},  # Red
#         ],
#         percentage_values=False
#     )

#     map_chart.set_palette_coloring(
#         steps=[
#             {'value': 0, 'color': lc.Color(0, 0, 255)},      # Blue
#             {'value': 1000, 'color': lc.Color(0, 255, 0)},   # Green
#             {'value': 5000, 'color': lc.Color(255, 255, 0)}, # Yellow
#             {'value': 10000, 'color': lc.Color(255, 165, 0)},# Orange
#             {'value': 50000, 'color': lc.Color(255, 0, 0)},  # Red
#         ],
#         look_up_property='value'
#     )

# # Function to update the dashboard with historical data
# def update_dashboard():
#     for year in years:
#         print(f"Updating historical data for year: {year}")
#         year_data = data[data['Year'] == year]
#         data_for_year = [{"category": row['fg_apt'], "value": row['Total_Flights']} for _, row in year_data.iterrows()]
#         update_charts_for_year(year, data_for_year)
#         time.sleep(2)  # Pause for better visualization

# # Start the dashboard
# dashboard.open(live=True)
# update_dashboard()










import pandas as pd
import lightningchart as lc
import time
import warnings

# Suppress warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

# Set LightningChart license
with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

# Load flight dataset
file_path = 'Dataset/merged_international_report.xlsx'  # Update with the actual path
data = pd.read_excel(file_path)

# Filter data to ensure validity
data = data[(data['Total_Flights'] > 0) & (data['Country_ISO'].notna()) & (data['Country_ISO'] != 0)]

# Group data by year and country for aggregation
grouped_data = data.groupby(['Year', 'Country', 'Country_ISO'])['Total_Flights'].sum().reset_index()

# Get unique years
years = grouped_data['Year'].unique()

# Create dashboard with two rows: Bar chart and Map chart
dashboard = lc.Dashboard(theme=lc.Themes.CyberSpace, rows=2, columns=1)
bar_chart = dashboard.BarChart(row_index=0, column_index=0)
map_chart = dashboard.MapChart(row_index=1, column_index=0)

# Update charts for a given year
def update_charts_for_year(year):
    # Filter data for the selected year
    year_data = grouped_data[grouped_data['Year'] == year]

    # Prepare bar chart data
    bar_data = [
        {"category": row['Country'], "value": row['Total_Flights']}
        for _, row in year_data.iterrows()
    ]

    # Prepare map data
    map_data = [
        {"ISO_A3": row['Country_ISO'], "value": row['Total_Flights']}
        for _, row in year_data.iterrows()
        if pd.notna(row['Country_ISO']) and row['Country_ISO'] != 0
    ]

    # Update bar chart
    bar_chart.set_title(f'Annual Flight Distribution by Country - Year {year}')
    bar_chart.set_data(bar_data)

    # Update map chart
    map_chart.invalidate_region_values(map_data)
    map_chart.set_title(f'Flight Intensity - Year {year}')

    # Set color palettes
    bar_chart.set_palette_colors(
        steps=[
            {'value': 0, 'color': lc.Color(0, 0, 255)},      # Blue
            {'value': 1000, 'color': lc.Color(0, 255, 0)},   # Green
            {'value': 5000, 'color': lc.Color(255, 255, 0)}, # Yellow
            {'value': 10000, 'color': lc.Color(255, 165, 0)},# Orange
            {'value': 50000, 'color': lc.Color(255, 0, 0)},  # Red
        ],
        percentage_values=False
    )

    map_chart.set_palette_coloring(
        steps=[
            {'value': 0, 'color': lc.Color(0, 0, 255)},      # Blue
            {'value': 1000, 'color': lc.Color(0, 255, 0)},   # Green
            {'value': 5000, 'color': lc.Color(255, 255, 0)}, # Yellow
            {'value': 10000, 'color': lc.Color(255, 165, 0)},# Orange
            {'value': 50000, 'color': lc.Color(255, 0, 0)},  # Red
        ],
        look_up_property='value'
    )

# Simple visualization loop
def update_dashboard():
    for year in years:
        print(f"Visualizing data for year: {year}")
        update_charts_for_year(year)
        time.sleep(1)  # Pause for better visualization

# Start the dashboard
dashboard.open(live=True)
update_dashboard()
