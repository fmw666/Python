import requests
from bs4 import BeautifulSoup

url = 'https://search.bilibili.com/all?keyword=python'
html = requests.get(url)
Soup = BeautifulSoup(html.text, 'lxml')
images = Soup.select('#server-search-app > div.contain > div.body-contain > div > div.result-wrap.clearfix > ul > li > a > div > div.lazy-img > img')
titles = Soup.select('#server-search-app > div.contain > div.body-contain > div > div.result-wrap.clearfix > ul > li > div > div.headline.clearfix > a')
urls = Soup.select('#server-search-app > div.contain > div.body-contain > div > div.result-wrap.clearfix > ul > li > a')

fp = open('crawl/text-pro2/result.txt', 'a', encoding='utf-8')
fp.seek(0)
fp.truncate()
order = 1
for title,url,image in zip(titles,urls,images):
    data = {
        'title' : title.get_text(),
        'url'   : 'https:' + url.get('href'),
        'image' : image.get('src')
    }
    fp.write(str(order)+'.'+data['title']+ \
         '\n' + '  ' + data['url']+data['image']+'\n')
    order += 1
fp.close()
    
