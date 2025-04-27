from apscheduler.schedulers.background import BackgroundScheduler
import pytz
from datetime import datetime


class DailyWeatherNotifier:

    def __init__(self, weather_fetcher, messenger, cities):
        self.weather_fetcher = weather_fetcher
        self.messenger = messenger
        self.cities = cities

    def send_daily_weather_forecast(self):
        current_date = datetime.now().strftime("%B %d, %Y")
        msg = f"🌤️ Weather Report - {current_date}\n\n"
        
        for city in self.cities:
            forecast = self.weather_fetcher.fetch_weather(city)
            msg += f"📍 {city}\n"
            msg += "\n".join(forecast)
            msg += "\n\n"

        self.messenger.send_message(msg)
        print("✅ Forecast sent at", datetime.now().strftime("%Y-%m-%d %I:%M %p"))

    def schedule_daily_notification(self):
        scheduler = BackgroundScheduler(timezone=pytz.timezone("Asia/Kolkata"))
        scheduler.add_job(self.send_daily_weather_forecast, 'cron', hour=8, minute=0)
        scheduler.start()
