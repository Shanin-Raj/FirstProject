# Import necessary libraries
import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# Explicitly find the .env file's path
script_dir = Path(__file__).parent
dotenv_path = script_dir / ".env"
load_dotenv(dotenv_path=dotenv_path)

def get_kochi_weather():
    """
    Calls the OpenWeatherMap API to get the current weather for Kochi.
    """
    try:
        # Step 1: Get API Key and Set Up API Call Details
        api_key = os.getenv("OPENWEATHER_API_KEY")
        if not api_key:
            print("Error: OPENWEATHER_API_KEY not found in .env file.")
            return

        url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": "Kochi,IN",
            "appid": api_key,
            "units": "metric"
        }

        # Step 2: Make the API Request
        print("Requesting weather data for Kochi...")
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status() 

        # Step 3: Print the Raw JSON Response
        weather_data = response.json()
        print("\n--- Raw API Response ---")
        print(weather_data)
        print("------------------------\n")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred with the API request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function when the script is executed
if __name__ == "__main__":
    get_kochi_weather()