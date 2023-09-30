# Program of the Day: Web Page Content Scraper

import requests
from bs4 import BeautifulSoup

def scrape_web_page(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find and print the page title
            title = soup.title.string
            print(f"Title: {title}")

            # Find and print the first paragraph (you can modify this to extract specific content)
            first_paragraph = soup.find('p').get_text()
            print(f"First Paragraph: {first_paragraph}")
        else:
            print("Failed to retrieve web page. Check the URL and try again.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage: Scrape content from a web page
url = "https://example.com"  # Replace with the URL of the web page you want to scrape
scrape_web_page(url)
