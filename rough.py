from bs4 import BeautifulSoup
import requests
import lxml

base_url = 'https://coursehunter.net/course/understanding-typescript'

page = requests.get(base_url).text

soup = BeautifulSoup(page, 'lxml')

title = soup.find('p', class_= 'hero-description').text

# !mkdir title

links = soup.find_all('li', 'lessons-item')

for link in links:

  url = link.find('link', attrs = {'itemprop': 'url'})['href']

  title = link.find('div', class_= 'lessons-name').text + '.mp4'

  # print(url)

  with requests.get(url) as data:
    with open(title, 'wb') as f:

      f.write(data.content)
      f.close()

