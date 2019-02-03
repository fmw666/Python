# 爬虫-实战项目源码

这里插一张图片吧~

## 使用 requests 库请求网站
- ***爬取百度页面 html 信息***
  ```python
  import requests

  url = 'https://www.baidu.com/'
  html = requests.get(url)
  print(html.text)
  ```
## 使用 Beautiful Soup 解析网页
- ***爬取纽约市景点信息***
  ```python
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
  ```
- ***爬取斗鱼LOL直播信息***
  ```python
  from bs4 import BeautifulSoup
  import requests

  url = 'https://www.douyu.com/g_LOL'
  html = requests.get(url)
  soup = BeautifulSoup(html.text, 'lxml')
  data = soup.select('#live-list-contentbox > li > a > div.mes > div > h3')
  href = soup.select('#live-list-contentbox > li > a')
  print(len(data))
  for i in range(120):
      item_data = data[i]
      item_href = href[i]
      link = url[:21] + item_href.get('href')
      result = {
          'title': item_data.get_text().strip(),
          'link': link
      }
      print(result)
  ```
- ***爬取猫眼电影Top100,并存入文本***
  ```python
  import requests
  from multiprocessing import Pool
  from requests.exceptions import RequestException
  import re
  import json

  def get_one_page(url):
      try:
          response = requests.get(url)
          if response.status_code == 200:
              return response.text
          return None
      except RequestException:
          return None

  def parse_one_page(html):
      pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                           + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                           + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
      items = re.findall(pattern, html)
      for item in items:
          yield {
              'index': item[0],
              'image': item[1],
              'title': item[2],
              'actor': item[3].strip()[3:],
              'time' : item[4].strip()[5:],
              'score': item[5] + item[6]
          }

  def clear_file(file):
      with open(file, 'w', encoding='utf-8') as f:
          f.seek(0)
          f.truncate()
          f.close()

  def write_to_file(content):
      with open('maoyanTop100.txt', 'a', encoding='utf-8') as f:
          # clear_file('maoyanTop100.txt')
          f.write(json.dumps(content, ensure_ascii=False) + '\n')
          f.close()

  def main(offset):
      url = 'https://maoyan.com/board/4?offset=' + str(offset)
      html = get_one_page(url)
      for item in parse_one_page(html):
          print(item)
          write_to_file(item)

  if __name__ == '__main__':
      pool = Pool()
      pool.map(main, [i*10 for i in range(10)])
  ```
- ***爬取bilibili单页视频信息***
  ```python
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
  ```
- ***爬取白蛇缘起豆瓣影评***
  ```python
  from bs4 import BeautifulSoup
  import requests
  import time

  # 爬取前5页(100条)评论
  urls = ['https://movie.douban.com/subject/30331149/comments?start={}&limit=20&sort=new_score&status=P'.format(str(i)) for i in range(0, 100, 20)] 
  # 全局变量索引
  index = 1

  def get_info_to_txt(url,data=None):
      html = requests.get(url)
      soup = BeautifulSoup(html.text,'lxml')
      users = soup.select('span.comment-info > a')
      dates = soup.select('span.comment-info > span.comment-time')
      conts = soup.select('div.comment > p > span')

      global index
      with open('白蛇缘起豆瓣影评.txt','w',encoding='utf-8') as f:
          page = index // 20 + 1
          for user, date, cont in zip(users, dates, conts):
              user_name = user.get_text()
              user_id = user.get('href')[30:].rstrip('/')
              date_time = date.get_text().strip()
              content = cont.get_text().strip()

              f.write(user_name+' ('+user_id+')\n'+date_time+'\n'+content+'\n'+'-------------'+'\n')
              print('爬取第{}条'.format(index))
              index += 1
              time.sleep(1)
          print('----------爬取第{}页完成----------'.format(page))

          f.close()

  for url in urls:
      get_info_to_txt(url)
  ```
