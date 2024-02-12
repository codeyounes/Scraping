import requests
from bs4 import BeautifulSoup

# URL of the webpage containing the table
url = 'https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/demographic-data-analyzer'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the <pre> tag with class "language-markdown"
    pre_tag = soup.find('pre', class_='language-markdown')

    # Check if pre_tag is not None before proceeding
    if pre_tag:
        # Navigate to the <code> tag inside <pre>
        code_tag = pre_tag.find('code', class_='language-markdown')

        # Extract the text content inside the <code> tag
        if code_tag:
            markdown_content = code_tag.get_text()

            # Parse the Markdown content using BeautifulSoup
            soup_markdown = BeautifulSoup(markdown_content, 'html.parser')

            # Find all table rows (excluding the first row which contains headers)
            rows = soup_markdown.find_all('tr')[1:]

            # Extract headers from the first row
            headers = [header.text.strip() for header in rows[0].find_all('th')]

            # Extract table data from rows
            table_data = []
            for row in rows[1:]:
                row_data = [data.text.strip() for data in row.find_all('td')]
                table_data.append(row_data)

            # Now you have the table headers in `headers` and table data in `table_data`
            # You can use them as needed in your code
            print('Headers:', headers)
            print('Table Data:', table_data)
        else:
            print("Code tag not found inside <pre> tag.")
    else:
        print("Pre tag with class 'language-markdown' not found.")
else:
    print('Failed to fetch the webpage. Status code:', response.status_code)
