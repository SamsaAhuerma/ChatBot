import openai
from openai import OpenAI

client = OpenAI()
from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")



def analyze_sentiment(text_s):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an assistant that responds only in English."},
            {"role": "user", "content": f"Analyze the sentiment of the following text in Spanish and classify it as positive, neutral, or negative. Provide the classification, a brief justification, and a motivational suggestion. Format the response in simple items, without using bullet points or special symbols, and ensure it does not exceed 30 words:\n\n{text_s}"}
        ],
        max_tokens=50
    )
    sentiment = response.choices[0].message.content
    return sentiment

# Función que maneja la respuesta para el clima
def generate_response_climate(city):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Give 3 tips about the city: {city}. Use only 20 words, formatted in bullet points for clarity."}
        ],
        max_tokens=50
    )
    curiosity = response.choices[0].message.content
    return curiosity

