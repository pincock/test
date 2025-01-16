import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Add headers to mimic a browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.content, 'html.parser')
        # Get text content without HTML tags
        text_content = soup.get_text(separator='\n', strip=True)
        return text_content
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    website_url = input("Please enter the website URL: ")
    content = scrape_website(website_url)
    print(content)
