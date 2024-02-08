import streamlit as st
import requests

st.title("Weather App")

city = st.text_input("Enter city name:")

if st.button("Get Weather"):
    api_url = f"http://localhost:8501//weather?city={city}"
    response = requests.get(api_url)

    if response.status_code == 200:
        weather_data = response.json()
        st.write(f"Weather in {city}: {weather_data['weather'][0]['description']}")
        st.write(f"Temperature: {weather_data['main']['temp']}°C")
    else:
        st.write("City not found.")
