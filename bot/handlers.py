from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler
from bot.weather import get_climate
from bot.counter import increment_counter
from bot.utils.openai_utils import analyze_sentiment, generate_response_climate

# Función para manejar el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("I want to know the climate!", callback_data='climate')],
        [InlineKeyboardButton("I want the counter!", callback_data='counter')],
        [InlineKeyboardButton("Analyze my conversation!", callback_data='analyze_sentiment')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to the main menu. What do you want to do?", reply_markup=reply_markup)


# Función para manejar las opciones del menú
async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'climate':
        await query.edit_message_text("Which city would you like a weather forecast for?")
        context.user_data['waiting_for_city'] = True
    elif query.data == 'counter':
        user_id = update.effective_user.id
        new_counter = increment_counter(user_id)
        await query.edit_message_text(f"Your current counter is: {new_counter}")
    elif query.data == 'analyze_sentiment':
        await query.edit_message_text("Please send the text you would like to analyze for sentiment.")
        context.user_data['waiting_for_sentiment'] = True


#Función que maneja los distintos mensajes
async def handle_message(update, context):
    if context.user_data.get('waiting_for_city', False):
        city = update.message.text
        context.user_data['city'] = city 

        climate_info = get_climate(city) 
        context.user_data['last_temperature'] = climate_info  

        curiosities_info = generate_response_climate(city)
        
        combined_response = f"{climate_info}\n\nInteresting facts about {city}:\n{curiosities_info}"
        
        await update.message.reply_text(combined_response)
        
        context.user_data['waiting_for_city'] = False

    elif context.user_data.get('waiting_for_sentiment', False):
        text_s = update.message.text  
        sentiment = analyze_sentiment(text_s)  
        await update.message.reply_text(f"Sentiment analysis: {sentiment}")
        context.user_data['waiting_for_sentiment'] = False  
    
