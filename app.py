import streamlit as st
import datetime
import pandas as pd
import numpy as np
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time'''

pickup_date = st.date_input(
    "Select a Data:",
     #  datetime.date.today()
    )

pickup_time = st.time_input(
    "Select a Time:",
    # datetime.datetime.now().time()
)

# Combine date and time into a single datetime object
# combined_datetime = datetime.datetime.combine(date, time)

# st.write("You selected:", combined_datetime)

'''
- pickup longitude
- pickup latitude'''

# Add a longitude input
pickup_lon = st.number_input(
    "Enter Pickup Longitude:",
    min_value=-180.0,  # Minimum longitude
    max_value=180.0,   # Maximum longitude
    value=0.0,         # Default value
    step=0.01          # Increment step
)

# Add a longitude input
pickup_lat = st.number_input(
    "Enter Pickup Latitude:",
    min_value=-180.0,  # Minimum longitude
    max_value=180.0,   # Maximum longitude
    value=0.0         # Default value
)


'''
- dropoff longitude
- dropoff latitude
- passenger count
'''
dropoff_lon = st.number_input(
    "Enter Dropoff Longitude:",
    min_value=-180.0,  # Minimum longitude
    max_value=180.0,   # Maximum longitude
    value=0.0,         # Default value
    step=0.01          # Increment step
)

# Add a longitude input
dropoff_lat = st.number_input(
    "Enter Dropoff Latitude:",
    min_value=-180.0,  # Minimum longitude
    max_value=180.0,   # Maximum longitude
    value=0.0,         # Default value
    step=0.01          # Increment step
)

def get_select_box_data():

    return pd.DataFrame({
          'first column': list(range(1, 9))
        })

df = get_select_box_data()

passenger_count = st.selectbox('Number of passengers', df['first column'])

''' # Test for metrics display'''
col1, col2, col3 = st.columns(3)
col1.metric("SPDR S&P 500", "$437.8", "-$1.25")
col2.metric("FTEC", "$121.10", "0.46%")
col3.metric("BTC", "$46,583.91", "+4.87%")

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''Prepare my datetime: '''

# Combine them into a single datetime string
datetime_str = f"{pickup_date} {pickup_time}"
st.write("Combined datetime as a string:", datetime_str)

# Parse the combined string into a datetime object
combined_datetime = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
# Convert datetime to string (to send in query params)
pickup_datetime_str = combined_datetime.strftime("%Y-%m-%d %H:%M:%S")  # Format it as a string


st.write("Combined datetime as datetime:", pickup_datetime_str)

# Build my request dict
request_dict = dict(
        pickup_datetime=[combined_datetime],
        pickup_longitude=[pickup_lon],
        pickup_latitude=[pickup_lat],
        dropoff_longitude=[dropoff_lon],
        dropoff_latitude=[dropoff_lat],
        passenger_count=[passenger_count],
    )

response = requests.get(url, request_dict)
response_data = response.json()


'''

2. Let's build a dictionary containing the parameters for our API...

Print my dictionary:
'''


'''
3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
st.write("here is my prediction:")
st.write(f"$ {round(response_data['fare'],2)}")
