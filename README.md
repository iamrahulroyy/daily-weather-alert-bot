A WhatsApp bot that sends daily weather forecasts for multiple cities using Twilio and OpenWeatherMap APIs.

## Features
- 🌡️ Daily weather forecasts with temperature and conditions
- 📱 Automated WhatsApp messages via Twilio
- 🌆 Support for multiple cities
- ⏰ Scheduled notifications (default: 8 AM daily)
- 🌍 Customizable location settings
- 🌡️ Shows both actual and "feels like" temperatures
- 🕒 Three daily forecasts (Morning, Afternoon, Night)

## Prerequisites

- Python 3.8 or higher
- Twilio Account with WhatsApp capabilities
- OpenWeatherMap API key
- Active internet connection

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/daily-weather-alert-bot.git
cd daily-weather-alert-bot
```

2. Create and activate a virtual environment:
```bash
python -m venv env
.\env\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with your credentials:
```properties
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
YOUR_WHATSAPP_NUMBER=whatsapp:+your_number
OPENWEATHER_API_KEY=your_api_key
CITIES=City1,City2,City3
CHECK_INTERVAL_SECONDS=600
```

## Usage

1. For immediate testing:
```bash
python main.py
```

2. For scheduled daily updates, set `immediate_test = False` in `main.py`

## Project Structure

```
weatherAlert-bot/
│
├── helper/
│   ├── __init__.py
│   ├── config.py            # Configuration and environment variables
│   ├── weather_fetcher.py   # OpenWeatherMap API integration
│   ├── whatsapp_messenger.py# Twilio WhatsApp integration
│   └── daily_weather_notifier.py # Scheduling and notifications
│
├── .env                     # Environment variables (create this)
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## Configuration Options

- `CITIES`: Comma-separated list of city names
- `CHECK_INTERVAL_SECONDS`: Time between API checks
- Forecast times: 9 AM (Morning), 3 PM (Afternoon), 9 PM (Night)
- Time zone: Asia/Kolkata (configurable in daily_weather_notifier.py)

## Sample Output

```
🌤️ Weather Report - April 27, 2025

📍 Mumbai
Morning: 32°C (feels like 36°C), clear sky
Afternoon: 34°C (feels like 38°C), scattered clouds
Night: 29°C (feels like 32°C), partly cloudy

📍 Delhi
Morning: 28°C (feels like 30°C), haze
Afternoon: 35°C (feels like 38°C), clear sky
Night: 30°C (feels like 32°C), clear sky
```

## Error Handling

The application includes robust error handling for:
- Network connectivity issues
- API rate limits
- Invalid city names
- Authentication failures
- Message delivery failures

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments

- OpenWeatherMap API for weather data
- Twilio for WhatsApp messaging capabilities
- APScheduler for task scheduling

## Support

For support, email rahulroy.agtt@gmail.com or open an issue in the repository.



