from bs4 import BeautifulSoup
import pandas as pd

# Load the HTML file
html_file_path = 'Data Analysis with Python Projects - Medical Data Visualizer _ Learn _ freeCodeCamp.org.html'

# Read the HTML content with explicit encoding
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all tables in the HTML
tables = soup.find_all('table')

# Iterate over each table found
for index, table in enumerate(tables, start=1):
    # Convert table to DataFrame
    df = pd.read_html(str(table))[0]

    # Define the filename for the Excel file
    excel_file_name = f"table_{index}.xlsx"

    # Write DataFrame to Excel file
    df.to_excel(excel_file_name, index=False)

    print(f"Table {index} data saved to {excel_file_name}")
