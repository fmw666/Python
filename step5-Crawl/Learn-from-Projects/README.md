# [🐍爬虫](#)、[🌥数据清洗](#)与[👀可视化](#)-实战

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
