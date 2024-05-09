class Weather:
    def __init__(self):
        self.weather = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
                        }

    def get_weather(self, city):
        return self.weather.get(city)
    
    def display_weather(self, city):
        weather_conditions = self.get_weather(city)
        if weather_conditions:
            print(f"The weather conditions in {city} are as follows: {weather_conditions}")
        else:
            print("City not found. please try again")


def main():
    weather_conditons = Weather()
    while True:
        try:
            city = input("please input the name of the city you wish to view: ").title()
            if city.lower() == 'quit':
                break
            weather_conditons.display_weather(city)
        except ValueError:
            print("please enter a valid input and try agian")
            return
        
if __name__ == "__main__":
    main()