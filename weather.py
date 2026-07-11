# weather.py
import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raises error if request failed
        data = response.json()

        temp = data["current_condition"][0]["temp_C"]
        feels_like = data["current_condition"][0]["FeelsLikeC"]
        description = data["current_condition"][0]["weatherDesc"][0]["value"]

        print(f"\n🌍 Weather in {city.title()}")
        print(f"🌡️  Temperature: {temp}°C")
        print(f"🤔 Feels like: {feels_like}°C")
        print(f"☁️  Condition: {description}")

        # Friendly message
        
        temp = int(temp)
        if temp >= 25:
            print("😎 It's hot outside, stay hydrated!")
        elif temp >= 15:
            print("🙂 Nice weather, enjoy your day!")
        elif temp >= 5:
            print("🧥 A bit cold, grab a jacket!")
        else:
            print("🥶 Very cold, wrap up warm!")

    except requests.exceptions.ConnectionError:
        print("❌ No internet connection!")
    except requests.exceptions.Timeout:
        print("❌ Request timed out, try again!")
    except requests.exceptions.HTTPError:
        print("❌ City not found!")

def main():
    while True:
        city = input("\nEnter city (or 'quit' to exit): ").strip()
        if city.lower() == "quit":
            print("Goodbye!")
            break
        elif city == "":
            print("Please enter a city name!")
        else:
            get_weather(city)

main()


