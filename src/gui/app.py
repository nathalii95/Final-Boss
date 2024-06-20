import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from src.scraping.scraper import scrape
from src.analysis.analysis import load_data, clean_data, analyze_data
from src.database.database_manager import read_data
from fpdf import FPDF

def perform_scraping():
    base_url = "https://webscraper.io/test-sites/e-commerce/allinone"
    df = scrape(base_url)
    df.to_csv("data/raw/products.csv", index=False)
    messagebox.showinfo("Info", "Scraping completado y datos guardados en products.csv")

def perform_analysis():
    df = load_data("mongodb")
    df = clean_data(df)
    analyze_data(df)
    df.to_csv("data/processed/cleaned_products.csv", index=False)
    messagebox.showinfo("Info", "Análisis completado y datos guardados en cleaned_products.csv")

def view_data():
    data = read_data()
    df = pd.DataFrame(data)
    display_table(df)

def display_table(df):
    table_window = tk.Toplevel(app)
    table_window.title("Datos en MongoDB")
    
    frame = ttk.Frame(table_window)
    frame.pack(fill=tk.BOTH, expand=True)
    
    cols = ["title", "description", "price"]
    tree = ttk.Treeview(frame, columns=cols, show='headings')
    
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.W)

    for _, row in df[cols].iterrows():
        tree.insert("", tk.END, values=list(row))
    
    tree.pack(fill=tk.BOTH, expand=True)
    
    export_button = tk.Button(table_window, text="Exportar a PDF", command=lambda: export_to_pdf(df[cols]))
    export_button.pack(pady=10)

def export_to_pdf(df):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Column widths
    col_widths = {"title": 45, "description": 114, "price": 24}

    # Add table header
    cols = ["title", "description", "price"]
    for col in cols:
        pdf.cell(col_widths[col], 10, col, 1)
    pdf.ln()
    
    # Add table rows
    for _, row in df.iterrows():
        for col in cols:
            cell = row[col]
            if isinstance(cell, str) and len(cell) > 50:
                cell = cell[:50]  # Truncar a 50 caracteres
            pdf.cell(col_widths[col], 10, str(cell), 1)
        pdf.ln()
    
    pdf_file_path = "data/output/data_report.pdf"
    pdf.output(pdf_file_path)
    messagebox.showinfo("Info", f"Datos exportados a {pdf_file_path}")

app = tk.Tk()
app.title("Interfaz Gráfica de Usuario")

frame = tk.Frame(app)
frame.pack(pady=20)

scrape_button = tk.Button(frame, text="Realizar Scraping", command=perform_scraping)
scrape_button.pack(pady=10)

analyze_button = tk.Button(frame, text="Realizar Análisis", command=perform_analysis)
analyze_button.pack(pady=10)

view_button = tk.Button(frame, text="Generar Reporte Pdf", command=view_data)
view_button.pack(pady=10)

app.mainloop()