# src/database/database_manager.py
import pymongo

# Configuración de la conexión a MongoDB
mongo_uri = "mongodb+srv://nathalyuvidia:Hsm199525@cluster0.hlglhlv.mongodb.net/curso2024"
client = pymongo.MongoClient(mongo_uri)
db = client["curso2024"]
collection = db["productos"]

def insert_data(data):
    """Inserta los datos en la colección de MongoDB."""
    try:
        collection.insert_many(data)
        print("Datos insertados correctamente en MongoDB")
    except Exception as e:
        print(f"Error al insertar datos en MongoDB: {e}")

def read_data():
    """Lee todos los documentos de la colección."""
    try:
        cursor = collection.find({})
        return list(cursor)
    except Exception as e:
        print(f"Error al leer datos desde MongoDB: {e}")
        return []
