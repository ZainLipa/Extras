# Program of the Day: Simple Weather App

import requests

def get_weather(city):
    # Replace 'YOUR_API_KEY' with your actual API key from a weather service provider
    api_key = 'YOUR_API_KEY'
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'

    complete_url = f'{base_url}q={city}&appid={api_key}&units=metric'

    response = requests.get(complete_url)
    data = response.json()

    if data['cod'] == 200:
        main_data = data['main']
        temperature = main_data['temp']
        humidity = main_data['humidity']
        weather_data = data['weather'][0]
        description = weather_data['description']

        print(f'Weather in {city}:')
        print(f'Temperature: {temperature}°C')
        print(f'Humidity: {humidity}%')
        print(f'Conditions: {description}')
    else:
        print('City not found. Please check the city name.')

# Example usage
city = input('Enter the city name: ')
get_weather(city)
