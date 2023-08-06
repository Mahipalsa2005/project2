import requests

# Function to fetch weather data using API
def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Fetch temperature in Celsius
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Check for any request errors
        weather_data = response.json()

        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]

        return temperature, description

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

# Main program
if __name__ == "__main__":
    api_key = "d48469ed608cbdc41b08731530b5ddc4"
    city_name = input("Enter the city name: ")

    weather_info = get_weather(city_name, api_key)
    if weather_info:
        temperature, description = weather_info
        print(f"The temperature in {city_name} is {temperature:.2f}°C.")