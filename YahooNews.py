
import requests
from bs4 import BeautifulSoup

url = 'https://www.yahoo.com/news/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('h3', class_='Mb(5px)')
count = 1

print('Top 10 Yahoo News:\n')
for article in articles[:10]:
    link = article.a.get('href')
    title = article.text
    print(str(count) + '. ' + title + '\n' + link + '\n')
    count += 1
