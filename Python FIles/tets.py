# import pandas as pd
# import matplotlib.pyplot as plt
# import time
# from datetime import datetime

# # Define the path to the CSV file
# csv_file_path = 'Dataset/748580849261105152.csv'

# # Initialize the plot with a larger figure size
# plt.ion()  # Enable interactive mode
# fig, ax1 = plt.subplots(figsize=(10, 6))  # Increase figure size

# # Function to load and plot data
# def load_and_plot_data():
#     # Load the traffic data from the CSV file
#     traffic_data = pd.read_csv(csv_file_path)

#     # Define column names or adjust based on available columns
#     timestamp_column = 'timestamp' if 'timestamp' in traffic_data.columns else None
#     traffic_volume_column = 'traffic_volume' if 'traffic_volume' in traffic_data.columns else traffic_data.columns[0]
#     speed_column = 'speed' if 'speed' in traffic_data.columns else traffic_data.columns[1]

#     # Debugging output
#     print(f"Timestamp Column: {timestamp_column}")
#     print(f"Traffic Volume Column: {traffic_volume_column}")
#     print(f"Speed Column: {speed_column}")
#     print("Sample Data:")
#     print(traffic_data[[traffic_volume_column, speed_column]].head())

#     # Generate timestamps if missing
#     if timestamp_column is None:
#         traffic_data['timestamp'] = pd.to_datetime('now') + pd.to_timedelta(traffic_data.index, 'm')
#         timestamp_column = 'timestamp'
#     else:
#         traffic_data['timestamp'] = pd.to_datetime(traffic_data[timestamp_column])

#     # Clear and update the plot
#     ax1.clear()
#     ax1.set_xlabel('Time')
#     ax1.set_ylabel('Traffic Volume', color='tab:blue')
#     ax1.plot(traffic_data[timestamp_column], traffic_data[traffic_volume_column], color='tab:blue')
#     ax1.tick_params(axis='y', labelcolor='tab:blue')

#     # Secondary axis for speed
#     ax2 = ax1.twinx()
#     ax2.set_ylabel('Speed (km/h)', color='tab:red')
#     ax2.plot(traffic_data[timestamp_column], traffic_data[speed_column], color='tab:red')
#     ax2.tick_params(axis='y', labelcolor='tab:red')

#     # Title and layout adjustments
#     plt.title('Real-Time Traffic Volume and Speed Monitoring')
#     fig.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
#     plt.draw()
#     plt.pause(0.1)  # Pause to allow for real-time update

# # Main loop for real-time monitoring
# try:
#     while True:
#         print(f"Updating data at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
#         load_and_plot_data()
#         time.sleep(60)  # Update every 60 seconds
# except KeyboardInterrupt:
#     print("Real-time monitoring stopped.")
#     plt.ioff()
#     plt.show()



# import requests

# # Your API Key for TomTom Traffic Flow API
# API_KEY = "IRcY3nKa1v8sG9MynvklZBbcNPKrkSkQ"

# # Base URL for the Traffic Flow API
# base_url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json"

# # Define coordinates (latitude and longitude) of the location to monitor
# latitude = 52.41072
# longitude = 4.84239
# point = f"{latitude},{longitude}"

# # Parameters for the API request
# params = {
#     "key": API_KEY,
#     "point": point,
#     "unit": "kmph"  # Set unit to km/h, change to "mph" if needed
# }

# # Make a request to the API
# try:
#     response = requests.get(base_url, params=params)
#     response.raise_for_status()  # Check if the request was successful
#     data = response.json()
    
#     # Extract and print traffic flow data
#     flow_data = data.get("flowSegmentData", {})
    
#     # Print key traffic data
#     print("Traffic Flow Data:")
#     print(f"Location: {point}")
#     print(f"Current Speed: {flow_data.get('currentSpeed', 'N/A')} km/h")
#     print(f"Free Flow Speed: {flow_data.get('freeFlowSpeed', 'N/A')} km/h")
#     print(f"Current Travel Time: {flow_data.get('currentTravelTime', 'N/A')} seconds")
#     print(f"Free Flow Travel Time: {flow_data.get('freeFlowTravelTime', 'N/A')} seconds")
#     print(f"Traffic Confidence Level: {flow_data.get('confidence', 'N/A')}")
#     print(f"Road Closure: {'Yes' if flow_data.get('roadClosure') else 'No'}")

#     # Print segment coordinates (if available)
#     coordinates = flow_data.get("coordinates", {}).get("coordinate", [])
#     if coordinates:
#         print("\nSegment Coordinates:")
#         for coord in coordinates:
#             print(f" - Latitude: {coord.get('latitude')}, Longitude: {coord.get('longitude')}")
    
# except requests.exceptions.RequestException as e:
#     print(f"An error occurred: {e}")

# import requests
# import time
# import lightningchart as lc

# with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
#     mylicensekey = f.read().strip()
# lc.set_license(mylicensekey)

# # Replace with your actual TomTom API key
# API_KEY = "IRcY3nKa1v8sG9MynvklZBbcNPKrkSkQ"

# # Fetch real-time traffic data from TomTom API
# def fetch_traffic_data():
#     url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json"
#     params = {
#         "key": API_KEY,  # Your API key
#         "point": "52.41072,4.84239",  # Coordinates of the location you want to monitor
#         "unit": "kmph"  # Set to 'kmph' for kilometers per hour
#     }
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print("Failed to fetch data")
#         return None

# # Initialize LightningChart for real-time visualization
# chart = lc.ChartXY()
# chart.set_title("Real-Time Traffic Monitoring")

# # Create series for Speed, Travel Time, and Confidence Level
# speed_series = chart.add_line_series().set_name("Current Speed (km/h)")
# travel_time_series = chart.add_line_series().set_name("Travel Time (seconds)")
# confidence_series = chart.add_line_series().set_name("Confidence Level (%)")

# # Set Y-axis ranges
# chart.get_default_y_axis().set_title("Speed (km/h)").set_interval(0, 100)
# travel_time_axis = chart.add_y_axis(opposite=True).set_title("Travel Time (seconds)").set_interval(0, 300)
# confidence_axis = chart.add_y_axis().set_title("Confidence (%)").set_interval(0, 100)

# # Open the chart in a live window
# chart.open(live=True)

# # Run the monitoring loop
# try:
#     while True:
#         # Fetch traffic data
#         data = fetch_traffic_data()
        
#         if data:
#             traffic_data = data["flowSegmentData"]

#             # Extract metrics
#             current_speed = traffic_data["currentSpeed"]
#             travel_time = traffic_data["currentTravelTime"]
#             confidence = traffic_data["confidence"] * 100
#             road_status = "Closed" if traffic_data["roadClosure"] else "Open"

#             # Add data points to each series
#             timestamp = time.time()  # Current timestamp for x-axis
#             speed_series.add(timestamp, current_speed)
#             travel_time_series.add(timestamp, travel_time)
#             confidence_series.add(timestamp, confidence)

#             # Update the chart title to reflect road status
#             chart.set_title(f"Real-Time Traffic Monitoring - Road Status: {road_status}")

#             # Print current metrics for logging
#             print(f"Current Speed: {current_speed} km/h | Travel Time: {travel_time} seconds | Confidence: {confidence}% | Road Status: {road_status}")

#             # Check for alerts
#             if current_speed < 20:
#                 print("Alert: Speed dropped below 20 km/h!")
#             if traffic_data["roadClosure"]:
#                 print("Alert: The road is closed!")

#             # Pause for the next update (adjust frequency as needed)
#             time.sleep(60)  # Update every 60 seconds
#         else:
#             print("Error: No data available. Retrying in 60 seconds...")
#             time.sleep(60)

# except KeyboardInterrupt:
#     print("Real-time monitoring stopped.")






import requests
import time
import lightningchart as lc
from datetime import datetime

# Read license key
with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

# Replace with your actual TomTom API key
API_KEY = "IRcY3nKa1v8sG9MynvklZBbcNPKrkSkQ"

# Fetch real-time traffic data from TomTom API
def fetch_traffic_data():
    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json"
    params = {
        "key": API_KEY,
        "point": "52.41072,4.84239",
        "unit": "kmph"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return None

# Initialize LightningChart for real-time visualization
chart = lc.ChartXY()
chart.set_title("Real-Time Traffic Monitoring")

# Configure x-axis to display time in DateTime format
x_axis = chart.get_default_x_axis()
x_axis.set_title("Time")
time_origin = int(time.time() * 1000)  # Current timestamp in milliseconds as origin
x_axis.set_tick_strategy("DateTime", time_origin=time_origin)

# Create series for Speed, Travel Time, and Confidence Level
speed_series = chart.add_line_series(x_axis=x_axis).set_name("Current Speed (km/h)")
travel_time_series = chart.add_line_series(x_axis=x_axis).set_name("Travel Time (seconds)")
confidence_series = chart.add_line_series(x_axis=x_axis).set_name("Confidence Level (%)")

# Set Y-axis ranges
chart.get_default_y_axis().set_title("Speed (km/h)").set_interval(0, 100)
travel_time_axis = chart.add_y_axis(opposite=True).set_title("Travel Time (seconds)").set_interval(0, 300)
confidence_axis = chart.add_y_axis().set_title("Confidence (%)").set_interval(0, 100)

# Open the chart in a live window
chart.open(live=True)

# Run the monitoring loop
try:
    while True:
        # Fetch traffic data
        data = fetch_traffic_data()
        
        if data:
            traffic_data = data["flowSegmentData"]

            # Extract metrics
            current_speed = traffic_data["currentSpeed"]
            travel_time = traffic_data["currentTravelTime"]
            confidence = traffic_data["confidence"] * 100
            road_status = "Closed" if traffic_data["roadClosure"] else "Open"

            # Get current time for x-axis as formatted timestamp
            timestamp = int(time.time() * 1000)  # Current timestamp in milliseconds

            # Add data points to each series
            speed_series.add(timestamp, current_speed)
            travel_time_series.add(timestamp, travel_time)
            confidence_series.add(timestamp, confidence)

            # Update the chart title to reflect road status
            chart.set_title(f"Real-Time Traffic Monitoring - Road Status: {road_status}")

            # Print current metrics for logging
            print(f"Current Speed: {current_speed} km/h | Travel Time: {travel_time} seconds | Confidence: {confidence}% | Road Status: {road_status}")

            # Check for alerts
            if current_speed < 20:
                print("Alert: Speed dropped below 20 km/h!")
            if traffic_data["roadClosure"]:
                print("Alert: The road is closed!")

            # Pause for the next update (adjust frequency as needed)
            time.sleep(60)  # Update every 60 seconds
        else:
            print("Error: No data available. Retrying in 60 seconds...")
            time.sleep(60)

except KeyboardInterrupt:
    print("Real-time monitoring stopped.")
