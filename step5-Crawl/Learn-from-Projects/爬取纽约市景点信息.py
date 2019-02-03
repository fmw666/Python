from bs4 import BeautifulSoup
import requests
'''
爬取网址：
https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html
'''
url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')
titles = soup.select('div.listing_title > a[target="_blank"]')
imgs = soup.select('img[width="180"]')

for title,img in zip(titles,imgs):
    data = {
        'title' : title.get_text(),
        'img' : img.get('src')
    }
    print(data)