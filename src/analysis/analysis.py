import pandas as pd
import sys
import os
from pymongo import MongoClient  # Importa MongoClient para conexión a MongoDB
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from decorators.decorators import timeit, logit
from database.database_manager import read_data

@timeit
@logit
def main():
    print("Running analysis...")

if __name__ == "__main__":
    main()
# Configuración de la conexión a MongoDB
mongo_uri = "mongodb+srv://nathalyuvidia:Hsm199525@cluster0.hlglhlv.mongodb.net/curso2024"
client = MongoClient(mongo_uri)
db = client["curso2024"]
collection = db["productos"]

@logit
@timeit
def load_data(data_source):
    if data_source == "csv":
        data_path = "data/raw/products.csv"
        df = pd.read_csv(data_path)
    elif data_source == "mongodb":
        mongo_data = read_data()
        df = pd.DataFrame(mongo_data)
    else:
        raise ValueError("Unsupported data source")
    
    print("Data loaded successfully")
    return df

@logit
@timeit
def clean_data(df):
    df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)
    df["description"] = df["description"].apply(lambda x: x[:50]) 
    print("Data cleaned successfully")
    return df

@logit
@timeit
def analyze_data(df):
    print("Basic Data Analysis:")
    print(df.describe())
    print("\nProducts with highest prices: ")
    highest_prices = df.nlargest(5, "price")
    print(highest_prices)

@logit
@timeit
def save_clean_data(df, output_path):
    if output_path.endswith(".csv"):
        df.to_csv(output_path, index=False)
    elif output_path.endswith(".xlsx"):
        df.to_excel(output_path, index=False)
    else:
        raise ValueError("Unsupported file format")
    print(f"Clean data saved to {output_path}")

def read_data():
    """Lee todos los documentos de la colección."""
    try:
        cursor = collection.find({})
        return list(cursor)
    except Exception as e:
        print(f"Error al leer datos desde MongoDB: {e}")
        return []

if __name__ == "__main__":
    data_source = "mongodb"  # Cambia a "csv" si deseas cargar desde CSV
    output_path = "data/processed/cleaned_products.csv"
    
    df = load_data(data_source)
    df = clean_data(df)
    analyze_data(df)
    os.makedirs("data/processed", exist_ok=True)
    save_clean_data(df, output_path)
