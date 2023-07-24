import dotenv
import os
import requests
from datetime import datetime

dotenv.load_dotenv()
USERNAME = os.getenv('USER')
BOTNAME = os.getenv('BOTNAME')

def greet_user(): 
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        return (f"Buenos días {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        return (f"Buenas tardes {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        return (f"Buenas noches {USERNAME}")
    return (f"Yo soy {BOTNAME}. ¿Cómo puedo asistirle?")

def get_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address
