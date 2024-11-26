# import lightningchart as lc
# import pandas as pd
# import trimesh
# import asyncio

# # Set LightningChart license
# with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
#     mylicensekey = f.read().strip()
# lc.set_license(mylicensekey)

# # Load the dataset
# file_path = 'Dataset/merged_international_report.xlsx'
# data = pd.read_excel(file_path)

# # Filter and preprocess data
# data = data[(data['Scheduled_Passengers'] > 0) & (data['Charter_Passengers'] > 0)]
# grouped_data = data.groupby('Year').agg({
#     'Scheduled_Passengers': 'sum',
#     'Charter_Passengers': 'sum'
# }).reset_index()

# # Ensure all values are converted to native Python types
# grouped_data['Year'] = grouped_data['Year'].astype(float).map(float)
# grouped_data['Scheduled_Passengers'] = grouped_data['Scheduled_Passengers'].map(int)
# grouped_data['Charter_Passengers'] = grouped_data['Charter_Passengers'].map(int)

# # Create the 3D Chart
# chart = lc.Chart3D(title="Dynamic 3D Passenger Visualization", theme=lc.Themes.Dark)

# # Add 3D Line Series
# scheduled_series = chart.add_line_series().set_line_color(lc.Color(255, 0, 0))
# scheduled_series.set_name("Scheduled Passengers").set_line_thickness(3)

# charter_series = chart.add_line_series().set_line_color(lc.Color(0, 0, 255))
# charter_series.set_name("Charter Passengers").set_line_thickness(3)

# # Add airplane models
# airplane_scheduled = chart.add_mesh_model().set_color(lc.Color(255, 0, 0))
# airplane_charter = chart.add_mesh_model().set_color(lc.Color(0, 0, 255))

# # Load airplane model
# airplane_obj_path = 'Dataset/AirplaneForFreeobj.obj'  # Replace with actual path
# airplane_scene = trimesh.load(airplane_obj_path)

# if isinstance(airplane_scene, trimesh.Scene):
#     airplane_mesh = airplane_scene.dump(concatenate=True)
# else:
#     airplane_mesh = airplane_scene

# airplane_vertices = airplane_mesh.vertices.flatten().tolist()
# airplane_indices = airplane_mesh.faces.flatten().tolist()
# airplane_normals = airplane_mesh.vertex_normals.flatten().tolist()

# # Set airplane geometry
# for airplane in [airplane_scheduled, airplane_charter]:
#     airplane.set_model_geometry(vertices=airplane_vertices, indices=airplane_indices, normals=airplane_normals)
#     airplane.set_scale(0.001).set_model_rotation(0, 90, 0)

# # Initialize data structures
# years = grouped_data['Year'].tolist()
# scheduled_data = [{'x': year, 'y': 0, 'z': 0} for year in years]
# charter_data = [{'x': year, 'y': 0, 'z': 1} for year in years]

# scheduled_series.add(scheduled_data)
# charter_series.add(charter_data)



# # Axis titles
# chart.get_default_x_axis().set_title('Year')
# chart.get_default_y_axis().set_title('Passengers')
# z_axis = chart.get_default_z_axis().set_title('Series').set_tick_strategy('Empty')  

# flight_lables=['Scheduled_Passengers', 'Charter_Passengers']
# for i, month_name in enumerate(flight_lables, start=0):
#     custom_tick = z_axis.add_custom_tick()
#     custom_tick.set_value(i)
#     custom_tick.set_text(month_name)

# # Animation Function
# async def animate_chart():
#     for i, year in enumerate(years):
#         print(f"Animating year: {year}")

#         # Update values for Scheduled and Charter Passengers
#         scheduled_value = int(grouped_data.loc[grouped_data['Year'] == year, 'Scheduled_Passengers'].values[0])
#         charter_value = int(grouped_data.loc[grouped_data['Year'] == year, 'Charter_Passengers'].values[0])

#         # Update data
#         scheduled_data[i]['y'] = scheduled_value
#         charter_data[i]['y'] = charter_value

#         # Clear and re-add data to simulate smooth line following airplanes
#         scheduled_series.clear()
#         charter_series.clear()
#         scheduled_series.add(scheduled_data[:i + 1])  # Line follows the airplane
#         charter_series.add(charter_data[:i + 1])

#         # Update airplane positions
#         airplane_scheduled.set_model_location(year, scheduled_value, 0)
#         airplane_charter.set_model_location(year, charter_value, 1)

#         # Pause for visualization
#         await asyncio.sleep(1)

# # Open Chart
# chart.open(live=True)

# # Run Animation
# asyncio.run(animate_chart())








# import lightningchart as lc
# import pandas as pd
# import trimesh
# import asyncio

# # Set LightningChart license
# with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
#     mylicensekey = f.read().strip()
# lc.set_license(mylicensekey)

# # Load the dataset
# file_path = 'Dataset/merged_international_report.xlsx'
# data = pd.read_excel(file_path)

# # Filter and preprocess data
# data = data[data['Total_Passengers'] > 0]
# grouped_data = data.groupby(['Year', 'usg_apt']).agg({'Total_Passengers': 'sum'}).reset_index()

# # Ensure all values are converted to native Python types
# grouped_data['Year'] = grouped_data['Year'].astype(float)
# grouped_data['Total_Passengers'] = grouped_data['Total_Passengers'].astype(int)

# # Selected airports
# selected_airports = ['AEX', 'ABE', 'CID', 'CHS']

# # Create the 3D Chart
# chart = lc.Chart3D(title="Passenger Traffic by Airport", theme=lc.Themes.Dark)

# # Add 3D Line Series for each airport
# airport_series = {}
# for airport in selected_airports:
#     series = chart.add_line_series().set_line_color(lc.Color(255, 255, 0)).set_line_thickness(3)
#     series.set_name(airport)
#     airport_series[airport] = series

# # Add airplane models for each airport
# airplane_models = {}
# airplane_obj_path = 'Dataset/AirplaneForFreeobj.obj'  # Replace with actual path
# airplane_scene = trimesh.load(airplane_obj_path)

# if isinstance(airplane_scene, trimesh.Scene):
#     airplane_mesh = airplane_scene.dump(concatenate=True)
# else:
#     airplane_mesh = airplane_scene

# airplane_vertices = airplane_mesh.vertices.flatten().tolist()
# airplane_indices = airplane_mesh.faces.flatten().tolist()
# airplane_normals = airplane_mesh.vertex_normals.flatten().tolist()

# for airport in selected_airports:
#     airplane = chart.add_mesh_model().set_color(lc.Color(0, 255, 0))
#     airplane.set_model_geometry(vertices=airplane_vertices, indices=airplane_indices, normals=airplane_normals)
#     airplane.set_scale(0.001).set_model_rotation(0, 90, 0)
#     airplane_models[airport] = airplane

# # Initialize data structures
# years = sorted(grouped_data['Year'].unique())
# airport_data = {}
# for airport in selected_airports:
#     airport_data[airport] = [{'x': year, 'y': 0, 'z': selected_airports.index(airport)} for year in years]
#     airport_series[airport].add(airport_data[airport])

# # Axis titles
# chart.get_default_x_axis().set_title('Year')
# chart.get_default_y_axis().set_title('Passengers').set_interval(0, 28000, stop_axis_after=True)
# z_axis = chart.get_default_z_axis().set_title('Airports').set_tick_strategy('Empty')

# for i, airport in enumerate(selected_airports):
#     custom_tick = z_axis.add_custom_tick()
#     custom_tick.set_value(i)
#     custom_tick.set_text(airport)

# # Animation Function
# async def animate_chart():
#     for i, year in enumerate(years):
#         print(f"Animating year: {year}")
#         for airport in selected_airports:
#             # Get total passengers for the current airport and year
#             airport_traffic = grouped_data[
#                 (grouped_data['usg_apt'] == airport) & (grouped_data['Year'] == year)
#             ]
            
#             if not airport_traffic.empty:
#                 total_value = int(airport_traffic['Total_Passengers'].values[0])
#             else:
#                 total_value = 0  # Default to 0 if no data exists for the airport-year

#             # Debugging print statements
#             print(f"Airport: {airport}, Year: {year}, Passengers: {total_value}")

#             # Update airport data
#             airport_data[airport][i]['y'] = total_value

#             # Clear and re-add data for the series
#             print(f"Clearing and adding data for {airport}")
#             airport_series[airport].clear()
#             airport_series[airport].add(airport_data[airport][:i + 1])

#             # Update airplane position
#             airplane_models[airport].set_model_location(year, total_value, selected_airports.index(airport))
#             print(f"Airplane for {airport} moved to Year={year}, Passengers={total_value}")

#         # Pause for visualization
#         await asyncio.sleep(1)

# # Open Chart
# chart.open(live=True)

# # Run Animation
# asyncio.run(animate_chart())












import lightningchart as lc
import pandas as pd
import trimesh
import asyncio

# Set LightningChart license
with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

# Load the dataset
file_path = 'Dataset/merged_international_report.xlsx'
data = pd.read_excel(file_path)

# Filter and preprocess data
data = data[data['Total_Passengers'] > 0]
grouped_data = data.groupby(['Year', 'usg_apt']).agg({'Total_Passengers': 'sum'}).reset_index()

# Ensure all values are converted to native Python types
grouped_data['Year'] = grouped_data['Year'].astype(float)
grouped_data['Total_Passengers'] = grouped_data['Total_Passengers'].astype(int)

# Selected airports
selected_airports = ['AEX', 'ABE', 'CID', 'CHS']

# Create the 3D Chart
chart = lc.Chart3D(title="Passenger Traffic by Airport", theme=lc.Themes.Dark)

# Add 3D Line Series and airplane models for each airport
airport_series = {}
airplane_models = {}
airplane_obj_path = 'Dataset/AirplaneForFreeobj.obj'  # Replace with actual path
airplane_scene = trimesh.load(airplane_obj_path)

if isinstance(airplane_scene, trimesh.Scene):
    airplane_mesh = airplane_scene.dump(concatenate=True)
else:
    airplane_mesh = airplane_scene

airplane_vertices = airplane_mesh.vertices.flatten().tolist()
airplane_indices = airplane_mesh.faces.flatten().tolist()
airplane_normals = airplane_mesh.vertex_normals.flatten().tolist()

# Function to generate unique colors
def generate_color(index, total):
    hue = index / total  # Generate a value between 0 and 1
    red = int(255 * (1 - hue))
    green = int(255 * hue)
    blue = int(255 * (0.5 - abs(hue - 0.5)))
    return lc.Color(red, green, blue)

# Create series and airplane models with unique colors
for i, airport in enumerate(selected_airports):
    # Assign specific colors for the first two airports
    if i == 0:  # First airport: Yellow
        color = lc.Color(255, 255, 0)  # Yellow
    elif i == 1:  # Second airport: Orange
        color = lc.Color(255, 165, 0)  # Orange
    elif i == 2:  # Second airport: Orange
        color = lc.Color(255, 0, 0)  # Red
    else:  # Remaining airports use dynamically generated colors
        color = generate_color(i, len(selected_airports))

    # Create and configure line series
    series = chart.add_line_series().set_line_color(color).set_line_thickness(3)
    series.set_name(airport)
    airport_series[airport] = series

    # Create and configure airplane models
    airplane = chart.add_mesh_model().set_color(color)
    airplane.set_model_geometry(vertices=airplane_vertices, indices=airplane_indices, normals=airplane_normals)
    airplane.set_scale(0.001).set_model_rotation(0, 90, 0)
    airplane_models[airport] = airplane

# Initialize data structures
years = sorted(grouped_data['Year'].unique())
airport_data = {}
for airport in selected_airports:
    airport_data[airport] = [{'x': year, 'y': 0, 'z': selected_airports.index(airport)} for year in years]
    airport_series[airport].add(airport_data[airport])

# Axis titles
chart.get_default_x_axis().set_title('Year')
chart.get_default_y_axis().set_title('Passengers').set_interval(0, 28000, stop_axis_after=True)
z_axis = chart.get_default_z_axis().set_title('Airports').set_tick_strategy('Empty')

for i, airport in enumerate(selected_airports):
    custom_tick = z_axis.add_custom_tick()
    custom_tick.set_value(i)
    custom_tick.set_text(airport)

# Animation Function
async def animate_chart():
    for i, year in enumerate(years):
        print(f"Animating year: {year}")
        for airport in selected_airports:
            # Get total passengers for the current airport and year
            airport_traffic = grouped_data[
                (grouped_data['usg_apt'] == airport) & (grouped_data['Year'] == year)
            ]
            
            if not airport_traffic.empty:
                total_value = int(airport_traffic['Total_Passengers'].values[0])
            else:
                total_value = 0  # Default to 0 if no data exists for the airport-year

            # Debugging print statements
            print(f"Airport: {airport}, Year: {year}, Passengers: {total_value}")

            # Update airport data
            airport_data[airport][i]['y'] = total_value

            # Clear and re-add data for the series
            print(f"Clearing and adding data for {airport}")
            airport_series[airport].clear()
            airport_series[airport].add(airport_data[airport][:i + 1])

            # Update airplane position
            airplane_models[airport].set_model_location(year, total_value, selected_airports.index(airport))
            print(f"Airplane for {airport} moved to Year={year}, Passengers={total_value}")

        # Pause for visualization
        await asyncio.sleep(1)

# Open Chart
chart.open(live=True)

# Run Animation
asyncio.run(animate_chart())


