import streamlit as st


st.title("Weather Forecast for the Next Days")
place = st.text_input(label="Place", placeholder="Type The City Name...", key="place")
days = st.slider(label="Forecast Days", min_value=1, max_value=5, help="Select the number of days")
option = st.selectbox(label="Select data to view", options=["Temperature", "Sky"], placeholder="Select Any of the Option", index=None)
st.subheader(f"{option} for the next {days} days in {place}")

