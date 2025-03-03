import streamlit as st
import requests

# OpenWeatherMap API Key (Replace with your key)
API_KEY = "your_openweathermap_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Streamlit UI
st.title("🌤️ Weather Bot")
st.write("Get real-time weather updates for any city!")

# User Input
city = st.text_input("Enter city name", "New York")

if st.button("Get Weather"):
    if city:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            weather = data["weather"][0]["description"].capitalize()
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            st.success(f"🌆 **City**: {city}")
            st.info(f"🌡️ **Temperature**: {temp}°C")
            st.info(f"🌬️ **Wind Speed**: {wind_speed} m/s")
            st.info(f"💧 **Humidity**: {humidity}%")
            st.info(f"🌤️ **Weather**: {weather}")
        else:
            st.error("City not found. Please enter a valid city name!")

# Footer
st.markdown("---")
st.markdown("💡 Made with ❤️ using Streamlit & OpenWeather API")
