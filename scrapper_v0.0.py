from bs4 import BeautifulSoup
import urllib3

url = 'your url'
http = urllib3.PoolManager()
response = http.request('GET', url)
soup = BeautifulSoup(response.data)

# soup = BeautifulSoup(, 'html.parser')
print(soup.prettify())
