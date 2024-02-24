import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input(label="Place", placeholder="Type The City Name...", key="place")
days = st.slider(label="Forecast Days", min_value=1, max_value=5, help="Select the number of days")
option = st.selectbox(label="Select data to view", options=["Temperature", "Sky"],
                      placeholder="Select Any of the Option", index=None)
st.subheader(f"{option} for the next {days} days in {place}")


# Here the following function returns two items and it will be stored in tuple, so we use two variables to access the two items in tuple in two diff. variable


def get_plot_data(days):
    date = ["56", "13", "12"]
    temp = [51, 12, 45]
    temp = [days * i for i in temp]
    return date, temp


d, t = get_plot_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
