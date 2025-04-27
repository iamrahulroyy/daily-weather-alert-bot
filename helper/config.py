from dotenv import load_dotenv
import os

load_dotenv(override=True)

print(f"🔍 Loading environment variables...")

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_MESSAGING_SERVICE_SID = os.getenv('TWILIO_MESSAGING_SERVICE_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER')
YOUR_WHATSAPP_NUMBER = os.getenv('YOUR_WHATSAPP_NUMBER')
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

cities_str = os.getenv('CITIES')
print(f"📍 Raw CITIES from .env: '{cities_str}'")

if not cities_str:
    print("⚠️ Warning: No cities found in .env file. Using default: Kolkata")
    CITIES = ['Kolkata']
else:
    CITIES = [city.strip() for city in cities_str.split(',') if city.strip()]
    print(f"🌆 Configured cities: {', '.join(CITIES)}")