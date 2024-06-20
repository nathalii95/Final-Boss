import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from ..database.database_manager import insert_data  # Importa la función para insertar en MongoDB

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to fetch page: {url}")

def parse_product(product):
    title = product.find("a", class_="title").text.strip()
    description = product.find("p", class_="description").text.strip()
    description = description[:50]
    price = product.find("h4", class_="price").text.strip()
    return {
        "title": title,
        "description": description,
        "price": price,
    }

def scrape(url):
    page_content = fetch_page(url)
    soup = BeautifulSoup(page_content, "html.parser")
    products = soup.find_all("div", class_="thumbnail") 
    products_data = []

    for product in products:
        product_info = parse_product(product)
        products_data.append(product_info)
    return pd.DataFrame(products_data)

# Definimos el url base para el scraping
base_url = "https://webscraper.io/test-sites/e-commerce/allinone"

df = scrape(base_url)
print(df)

# Insertar datos en MongoDB
insert_data(df.to_dict("records"))

# Asegúrate de que el directorio existe antes de guardar el archivo CSV
raw_data_dir = "../../data/raw"
os.makedirs(raw_data_dir, exist_ok=True)
df.to_csv(os.path.join(raw_data_dir, "products.csv"), index=False)