###DeltoBot

Descripción

DeltoBot es un bot de Telegram que interactúa con los usuarios proporcionando información sobre el clima, analiza el sentimiento de los comentarios del usuario y ofrece respuestas inteligentes utilizando la API de OpenAI. Además, cuenta con una funcionalidad libre que avisa sobre cambios en el clima para mejorar la planificación diaria de los usuarios.

Funcionalidades
Menú Principal
¡Quiero saber el clima!: El bot proporciona la temperatura actual y condiciones climáticas en una ciudad específica, utilizando la API de OpenWeatherMap. Además, incluye una recomendación basada en el clima (por ejemplo, "Lleva un paraguas" si está lloviendo).
¡Quiero contar!: Un contador que incrementa en uno cada vez que el usuario interactúa con esta opción. El contador es único para cada usuario y persiste incluso después de que el bot se reinicie.

Análisis de Sentimiento

El bot permite enviar una conversación del usuario para analizar el sentimiento de la misma utilizando la API de OpenAI. La respuesta se clasifica como Positiva, Neutral o Negativa con una breve justificación y sugerencias motivacionales.

Respuesta Inteligente
Cuando el usuario consulta el clima, el bot también ofrece una respuesta adicional generada por OpenAI, mejorando la experiencia del usuario con consejos adicionales o información interesante sobre la ciudad consultada, como lo son curiosidades sobre la ciudad.

Funcionalidad Libre: Notificación de Cambio Climático
El bot está configurado para notificar al usuario si el clima cambia en su ciudad de interés. Esto es útil para aquellos que planifican su día en función del clima, ya que las condiciones pueden cambiar rápidamente. Esta funcionalidad ayuda a que los usuarios tomen decisiones más informadas y se ajusten a cambios inesperados en el clima.

Tecnologías Utilizadas
Python: Lenguaje principal para el desarrollo del bot y la integración con las APIs.
API de Telegram: Utilizada para la interacción con los usuarios a través de mensajes.
API de OpenWeatherMap: Para obtener información sobre el clima.
API de OpenAI: Para analizar el sentimiento de los mensajes y generar respuestas inteligentes.
MongoDB Atlas: Base de datos utilizada para almacenar información sob
re los usuarios y mantener el contador persistente.
Librerías de Telegram en Python: Para interactuar con la API de Telegram y gestionar los mensajes del bot.

Uso de React (Opcional)
Aunque React es una excelente opción para crear interfaces de usuario dinámicas y reactivas, no lo utilicé en este proyecto debido a que el enfoque principal fue desarrollar un bot en Telegram que interactúa con las APIs de OpenWeatherMap y OpenAI usando Python. Debido a las limitaciones de tiempo, entre el trabajo, el estudio y otras responsabilidades, decidí centrarme en la funcionalidad del bot y no expandir el proyecto a una interfaz web.

Me encantaría poder integrar React en el futuro, especialmente si se decidiera expandir el proyecto a una aplicación web. React podría mejorar la experiencia de usuario al proporcionar una interfaz gráfica más interactiva, donde los usuarios puedan ingresar fácilmente las ciudades para consultar el clima y ver los resultados de manera más visual.

Dicho esto, sigue

Instalación

Clona este repositorio:
bash
Copy code
git clone https://github.com/tu-usuario/deltobot.git

Instala las dependencias necesarias:
bash
Copy code
pip install -r requirements.txt

Configura las variables de entorno:
TELEGRAM_API_KEY: La clave de API de tu bot de Telegram.
OPENWEATHERMAP_API_KEY: La clave de API de OpenWeatherMap.
OPENAI_API_KEY: La clave de API de OpenAI.
MONGODB_URI: URI de conexión a MongoDB Atlas.

Ejecuta el bot:
bash
Copy code
python bot/main.py

Cómo Funciona
Cuando el usuario inicia una conversación con el bot, se presenta un menú con dos opciones: consultar el clima o interactuar con el contador.
Si elige consultar el clima, el bot solicita la ciudad y luego proporciona la temperatura actual, las condiciones climáticas y una recomendación.
Si elige interactuar con el contador, el bot incrementa el contador único del usuario.
Además, el bot analiza el sentimiento de los mensajes enviados por el usuario y ofrece respuestas adicionales generadas por OpenAI.
Justificación de la Funcionalidad Libre
He añadido la funcionalidad de notificación sobre cambios climáticos para mejorar la experiencia del usuario. Dado que el clima puede variar rápidamente, muchas personas planifican su día en función de la previsión meteorológica. Esta característica ayuda a los usuarios a ajustarse a cambios repentinos en el clima, garantizando que su planificación diaria sea más precisa. Aqui debo agregar *nota importante* debido al uso del ingles en el código encontraran cosas como: 'Watch out!', 'Hey!' , que lejos de ser erradas expresiones o alucinaciones del lenguaje son jerga oculta del argentinismo mas puro, traduzcase, por favor, como: ¡OJO! y ¡CHE! , respectivamente.

Recomendaciones para Mejorar la Experiencia
Considerar la integración con otras APIs de clima para ofrecer información más detallada, como pronósticos a largo plazo.
Ampliar la funcionalidad de análisis de sentimiento para incluir una clasificación más detallada de las emociones, como "tristeza", "alegría", etc.
Contribuciones
Si deseas contribuir a este proyecto, por favor haz un fork del repositorio, realiza tus cambios y abre un pull request. Cualquier mejora o sugerencia será bienvenida.

Licencia
Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.

Saludo general:
A pesar de los tiempos ajustados, disfruté mucho trabajando en este proyecto y, en el futuro, estaría encantada de explorar más funcionalidades, incluyendo la integración de React(no me olvido yo).
¡¡Gracias!!