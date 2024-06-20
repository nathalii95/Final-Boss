##### Final Boss Python
###### Proyecto final con el tutor santine Ursino
###### Tipti

# Scraping Web de Productos.

Este proyecto se realizó con scraping de datos de productos de un sitio web, limpia y analiza los datos, los guarda en archivos CSV y en la base de dato MongoDB.

## Requerimientos 
- Python 3.7+
- Pandas
- BeautifulSoup4
- Requests
- Matplotlib
- Logging
- Pymongo
- Tkinter
- FPDF


## Instalacion

Para instalar las dependencias creamos un archivo txt el cual guardamos todas las dependencia para una rapida instalacion.
su mettodo de unso e sutilizando pip y es con el comando siguiente.

````bash
pip install -r .\dep.txt
````

## Estructura de las carpetas
````bash
Final-Boss/
│
├── data/
│   ├── raw/ 
│   │   └── products.csv
│   ├── processed/  
│   │   └── cleaned_products.csv
│   ├── output/  
│   │   └── data_report.pdf
│
├── notebooks/
│   └── exploration.ipynb
│
├── src/
│   ├── analysis/ 
│   │   ├── __init__.py         
│   │   ├── analysis.py
│   ├── database/
│   │   ├── __init__.py         
│   │   ├── database_manager.py
│   ├── decorators/ 
│   │   ├── __init__.py         
│   │   ├── decorators.py  
│   ├── scraping/ 
│   │   ├── __init__.py         
│   │   ├── scraper.py
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── app.py
│
├── dep.txt
├── README.md
````




## Ejecución del Programa
Para ejecutar el scraper, utiliza el siguiente comando:

`````bash
python -m src.scraping.scraper
`````
Esto generará un archivo CSV en la carpeta raw dentro de data llamado products.csv y almacenará los datos en MongoDB.


## Ejecucion para el analisis de datos

Para ejecutar el script para analisis de datos, utiliza el siguiente comando:

````bash
python -m src.analysis.analysis
````

Esto generará un archivo CSV en la carpeta processed dentro de data llamado cleaned_products.csv y realizará el análisis de los datos.


## Interfaz Gráfica de Usuario (GUI)

Para ejecutar la aplicación GUI, utiliza el siguiente comando:

````bash
python -m src.gui.app
````
La GUI permite:

Realizar scraping de datos y guardarlos en CSV y MongoDB.
Realizar análisis de datos y guardar los resultados en CSV.
Ver los datos almacenados en MongoDB y exportarlos a un archivo PDF.


## Funcionalidades Adicionales
## MongoDB
El scraper utiliza MongoDB para almacenar los datos scrapeados. Puedes instalar MongoDb en tu
máquina local o utilizar una instancia en la nube.


Los datos de los productos también se almacenan en la base de datos MongoDB para una mejor gestión y consulta. La conexión a MongoDB se realiza con la siguiente cadena de conexión:

````bash
mongodb+srv://nathalyuvidia:Hsm199525@cluster0.hlglhlv.mongodb.net/curso2024
````

## Exportación a PDF

La GUI permite exportar los datos a un archivo PDF con las columnas title, description (truncada a 50 caracteres) y price.

## Ejemplo de Uso de la GUI

## Realizar Scraping: Haz clic en el botón "Realizar Scraping" para obtener los datos del sitio web y guardarlos en MongoDB y CSV.
## Realizar Análisis: Haz clic en el botón "Realizar Análisis" para limpiar y analizar los datos, guardando los resultados en un archivo CSV.
## Ver Datos: Haz clic en el botón "Ver Datos" para mostrar los datos de MongoDB en una tabla. Desde esta ventana, puedes exportar los datos a PDF.

### Nathaly Uvidia 
### Tipti 2023 - 2024