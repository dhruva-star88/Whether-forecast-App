import streamlit as st
import plotly.express as px
from backend import get_data
from datetime import datetime

# Add title, select box, slider, city name, sub-header
st.title("Weather Forecast for the Next Days")
place = st.text_input(label="Place", placeholder="Type The City Name...", key="place")
days = st.slider(label="Forecast Days", min_value=1, max_value=5, help="Select the number of days")
option = st.selectbox(label="Select data to view", options=["Temperature", "Sky"],
                      placeholder="Select Any of the Option", index=None)


if place:
    # Get the Temperature/ Sky data
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            st.subheader(f"{option} for the next {days} days in {place}")
            temp_data = [i["main"]['temp'] / 10 for i in filtered_data]
            dates = [i["dt_txt"] for i in filtered_data]
            # Create A plotting graph
            figure = px.line(x=dates, y=temp_data, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clouds": "sky_images/cloud.png", "Clear": "sky_images/clear.png", "Rain": "sky_images/rain.png",
                      "Snow": "sky_images/snow.png"}
            sky_data = [i["weather"][0]["main"] for i in filtered_data]
            image_path = [images[condition] for condition in sky_data]
            # Return images based on the condition
            sky_dates = [dates["dt_txt"] for dates in filtered_data]
            d = [datetime.strptime(i, "%Y-%m-%d %H:%M:%S") for i in sky_dates]
            captions = [i.strftime("%a, %b %d, %H:%M") for i in d]
            st.image(image_path, width=150, caption=captions)

    except KeyError:
        st.info("That Place doesn't Exist")

