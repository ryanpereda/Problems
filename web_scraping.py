import requests
from bs4 import BeautifulSoup

url = 'https://www.reddit.com/r/CODZombies/wiki/origins/#wiki_storyline'
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'lxml') # or instead of lxml 'html.parser', make sure lxml is installed

print(soup.prettify())
print(soup.find_all('h2'))
