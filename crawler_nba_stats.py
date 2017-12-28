import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'http://www.nba.com/players'

def getHtml(url):
    html = requests.get(url).text
    return html

def getList(html):
    soup = BeautifulSoup(html, 'html.parser')
    player_list = []
    for player in soup.find_all('a',{'class':'row playerList'}):
        player_list.append(player.get('title'))
    player_data_frame = pd.DataFrame();
    player_data_frame['player name'] = player_list
    player_data_frame.to_csv('/Users/chenguangliu/Documents/crawlers/tables/nba_player.csv')

if __name__ == '__main__':
    html = getHtml(url)
    getList(html)