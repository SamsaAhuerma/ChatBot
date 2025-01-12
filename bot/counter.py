from pymongo import MongoClient
from database.mongo import MONGO_URI

# Conexión a la base de datos MongoDB
client = MongoClient(MONGO_URI)
db = client["cluster0"]
counter_collection = db["counters"]

# Función para obtener el contador de un usuario desde la base de datos
def get_user_counter(user_id: int) -> int:
    user_counter = counter_collection.find_one({"user_id": user_id})
    if user_counter:
        return user_counter["counter"]
    else:
        counter_collection.insert_one({"user_id": user_id, "counter": 0})
        return 0

# Función para actualizar el contador en la base de datos
def increment_counter(user_id: int) -> int:
    current_counter = get_user_counter(user_id)
    new_counter = current_counter + 1

    counter_collection.update_one(
        {"user_id": user_id},
        {"$set": {"counter": new_counter}}
    )

    return new_counter
