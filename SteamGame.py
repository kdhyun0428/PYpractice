import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

url = 'https://store.steampowered.com/search/?filter=topsellers'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

games = soup.find_all('div', {'class': 'col search_name ellipsis'})
game_titles = []
for game in games[:10]:
    title = game.find('span').text
    game_titles.append(title)

game_sales = []
sales = soup.find_all('div', {'class': 'col search_released responsive_secondrow'})
for sale in sales[:10]:
    game_sales.append(sale.text.strip())

plt.barh(game_titles[::-1], game_sales[::-1], color='red')
plt.xlabel('Sales')
plt.ylabel('Game Title')
plt.title('Top 10 Best-Selling Steam Games')
plt.show()