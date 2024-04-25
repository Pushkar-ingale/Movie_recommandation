import requests
from bs4 import BeautifulSoup

url = 'https://www.tutorialspoint.com/index.htm'  # Replace with the URL of the TutorialsPoint page you want to scrape

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Extracting all the links on the page
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))

    # You can modify the code to extract other information based on the HTML structure of the page.

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
