import streamlit as st
import requests
import time

# Set up the Streamlit app
st.title("Real-Time Traffic Data Dashboard")
st.subheader("Monitoring Traffic Speed, Travel Time, and Road Status")

# Function to fetch data from TomTom's API
def fetch_traffic_data():
    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json"
    params = {
        "key": "IRcY3nKa1v8sG9MynvklZBbcNPKrkSkQ",  # Replace with your API key
        "point": "52.41072,4.84239",
        "unit": "kmph"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch data from the API.")
        return None

# Main loop for real-time data
while True:
    data = fetch_traffic_data()

    if data:
        traffic_data = data["flowSegmentData"]

        # Display traffic data
        st.metric("Current Speed", f"{traffic_data['currentSpeed']} km/h")
        st.metric("Free Flow Speed", f"{traffic_data['freeFlowSpeed']} km/h")
        st.metric("Current Travel Time", f"{traffic_data['currentTravelTime']} seconds")
        st.metric("Free Flow Travel Time", f"{traffic_data['freeFlowTravelTime']} seconds")
        st.metric("Confidence", f"{traffic_data['confidence'] * 100}%")
        st.metric("Road Closure", "Yes" if traffic_data['roadClosure'] else "No")

        # Plot coordinates on a map (optional)
        st.map([{
            "lat": coord["latitude"],
            "lon": coord["longitude"]
        } for coord in traffic_data["coordinates"]["coordinate"]])

    # Refresh data every 60 seconds
    time.sleep(60)
