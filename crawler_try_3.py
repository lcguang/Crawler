import requests
import time
from bs4 import BeautifulSoup

# get pictures from specific url
url = 'http://alotofadultcontent.tumblr.com/'

def getHtml(url):
    html = requests.get(url).text
    return html


def getImg(html):
    soup = BeautifulSoup(html, 'html.parser')
    imglist = []
    for photourl in soup.find_all('img'):
        imglist.append(photourl.get('src'))
    x = 0
    total = len(imglist)
    for imgurl in imglist:
        x += 1
        print "Downloading picture", x, "/", total
        if imgurl == None:
            continue
        with open('/Users/chenguangliu/Documents/crawlers/pics/%s.gif' % x, 'wb') as file:
            file.write(requests.get(imgurl).content)
            time.sleep(0.1)

if __name__ == '__main__':
    html = getHtml(url)
    getImg(html)