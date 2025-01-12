import requests
import os
from dotenv import load_dotenv


load_dotenv()
OWM_API_KEY = os.getenv("OWM_API_KEY")

# Obtiene el clima actual de una ciudad usando la API de OpenWeatherMap y genera una recomendación basada en las condiciones.
def get_climate(city: str) -> str:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OWM_API_KEY}&units=metric&lang=en"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        conditions = data["weather"][0]["description"]

        if "rain" in conditions.lower():
            recommendation = "Take an umbrella 🌧️"
        elif "clear sky" in conditions.lower():
            recommendation = "Looks like a great day! 😎"
        elif temperature < 15:
            recommendation = "Dress warmly 🧥"
        else:
            recommendation = "The weather seems nice! 😊"
        return f"🌡️ Temperature: {temperature}°C\n☁️ Conditions: {conditions.capitalize()}\n📌 Recommendation: {recommendation}"
    elif response.status_code == 404:
        return "City not found. Please check the name."
    else:
        return "There was a problem fetching the weather. Please try again later."
    

# Función que maneja el cambio de temperatura y su respuesta personalizada.
async def check_temperature(context):
    city = context.user_data.get('city') 
    if city:
        new_temperature = get_climate(city) 
        
        if new_temperature != context.user_data.get('last_temperature'):
            if new_temperature < 15:  
                message = (
                    f"Watch out! The temperature in {city} changed! It's now {new_temperature}°C.\
                    Bundle up and grab a brolly, it's chilly!"
                )
            else:  
                message = (
                    f"Hey! The temperature in {city} has changed! It's now {new_temperature}°C.\
                    Perfect weather for a stroll!"
                )
            
            await context.bot.send_message(context.job.chat_id, message)
            
            context.user_data['last_temperature'] = new_temperature

