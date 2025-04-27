import requests
from datetime import datetime

class WeatherFetcher:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_weather(self, city):
        try:
            url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={self.api_key}'
            response = requests.get(url)
            response.raise_for_status()  
            data = response.json()
            
            if 'list' not in data:
                print(f"⚠️ Warning: No forecast data available for {city}")
                return []
                
            return self._parse_forecast_data(data)
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching weather for {city}: {str(e)}")
            return []

    def _parse_forecast_data(self, data):
        """Parse weather data and return important daily forecasts."""
        forecast = []
        today = datetime.now().date()
        
        try:
            city_name = data['city']['name']  
            country = data['city']['country']
            
            for item in data['list']:
                dt = datetime.utcfromtimestamp(item['dt'])
                if dt.date() == today:
                    hour = dt.hour
                    temp = round(item['main']['temp'])
                    weather = item['weather'][0]['description']
                    feels_like = round(item['main']['feels_like'])
                    
                    if hour in [9, 15, 21]:  # 9 AM, 3 PM, 9 PM
                        time_label = "Morning" if hour == 9 else "Afternoon" if hour == 15 else "Night"
                        forecast.append(f"{time_label}: {temp}°C (feels like {feels_like}°C), {weather}")

            return forecast

        except KeyError as e:
            print(f"❌ Error parsing weather data: {str(e)}")
            return []