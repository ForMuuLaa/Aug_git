'''
1. Refactoring a Weather Forecast Application into Classes and Modules
Objective: The aim of this assignment is to refactor an existing Python script for a weather forecast application into a more structured, object-oriented, and modular format. The focus will be on identifying parts of the script that can be encapsulated into classes and organizing these classes into appropriate modules to enhance code readability, maintainability, and scalability.

Task 1: Identifying and Creating Classes Analyze the provided script and identify distinct functionalities that can be encapsulated into classes. Create classes that represent different aspects of the weather forecast application, such as fetching data, parsing data, and user interaction.

Problem Statement: The existing script for the weather forecast application is written in a procedural style and lacks organization.

Code Example: Before Refactoring:

# Weather Forecast Application Script

def fetch_weather_data(city):
    # Simulated function to fetch weather data for a given city
    print(f"Fetching weather data for {city}...")
    # Simulated data based on city
    weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
    }
    return weather_data.get(city, {})

def parse_weather_data(data):
    # Function to parse weather data
    if not data:
        return "Weather data not available"
    city = data["city"]
    temperature = data["temperature"]
    condition = data["condition"]
    humidity = data["humidity"]
    return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

def get_detailed_forecast(city):
    # Function to provide a detailed weather forecast for a city
    data = fetch_weather_data(city)
    return parse_weather_data(data)

def display_weather(city):
    # Function to display the basic weather forecast for a city
    data = fetch_weather_data(city)
    if not data:
        print(f"Weather data not available for {city}")
    else:
        weather_report = parse_weather_data(data)
        print(weather_report)

def main():
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = get_detailed_forecast(city)
        else:
            forecast = display_weather(city)
        print(forecast)

if __name__ == "__main__":
    main()
Expected Outcome:

Clear definitions of classes such as `WeatherDataFetcher`, `DataParser`, and `UserInterface`, each handling specific parts of the application.
'''


class WeatherDataFetcher:
    def __init__(self):
        # Simulated data storage
        self.weather_data = {
            "new york": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "london": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }

    def fetch(self, city):
        # """Fetch weather data for a given city."""
        print(f"Fetching weather data for {city}...")
        
        return self.weather_data.get(city, {})

class DataParser:
    @staticmethod
    def parse(data):
        # """Parse weather data into a readable format."""
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"



class UserInterface:
    def __init__(self):
        self.fetcher = WeatherDataFetcher()
        self.parser = DataParser()

    def display_weather(self, city):
        # """Display basic weather information."""
        data = self.fetcher.fetch(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            print(self.parser.parse(data))

    def get_detailed_forecast(self, city):
        """Provide a detailed weather forecast for a city."""
        data = self.fetcher.fetch(city)
        return self.parser.parse(data)

    def run(self):
        #"""Run the weather forecast application."""
        while True:
            try:
                city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
                if city.lower() == 'exit':
                    break
                detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
                if detailed == 'yes':
                    print(self.get_detailed_forecast(city))
                else:
                    self.display_weather(city)
            except Exception as e:
                print("An error has occurred:", e)



if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
