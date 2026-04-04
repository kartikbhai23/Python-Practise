# Day 30: Weather CLI dashboard
# weather dashboard getting wttr.in weather lines for any input city

import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    
    try:
        print(f"Loading weather metrics: {city}...")
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            weather_report = response.text.strip()
            print("\nWeather Report:")
            print(weather_report)
            return weather_report
        else:
            print(f"Could not load forecast for '{city}' status: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print("Connection failure:", e)
        return None

def main(mock_inputs=None):
    input_idx = 0
    
    def get_input(prompt):
        nonlocal input_idx
        if mock_inputs is not None:
            if input_idx < len(mock_inputs):
                val = mock_inputs[input_idx]
                input_idx += 1
                print(f"{prompt}{val}")
                return val
            return "exit"
        return input(prompt)

    print("--- Weather Dashboard CLI ---")
    while True:
        city = get_input("Enter city (or 'exit'): ")
        if city.lower() == 'exit':
            print("Close Dashboard.")
            break
        if not city.strip():
            continue
            
        get_weather(city)

if __name__ == "__main__":
    main(mock_inputs=["Delhi", "New York", "exit"])
