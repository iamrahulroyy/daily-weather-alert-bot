from helper.config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_WHATSAPP_NUMBER,
    YOUR_WHATSAPP_NUMBER,
    OPENWEATHER_API_KEY,
    CITIES,
)
from helper.weather_fetcher import WeatherFetcher
from helper.whatsapp_messenger import WhatsAppMessenger
from helper.daily_weather_notifier import DailyWeatherNotifier


def main():
    weather_fetcher = WeatherFetcher(OPENWEATHER_API_KEY)
    messenger = WhatsAppMessenger(
        TWILIO_ACCOUNT_SID,
        TWILIO_AUTH_TOKEN,
        TWILIO_WHATSAPP_NUMBER,
        YOUR_WHATSAPP_NUMBER,
    )
    notifier = DailyWeatherNotifier(weather_fetcher, messenger, CITIES)

    immediate_test = True  # Change this to True to test immediately

    if immediate_test:
        notifier.send_daily_weather_forecast()
    else:
        notifier.schedule_daily_notification()


if __name__ == "__main__":
    main()
