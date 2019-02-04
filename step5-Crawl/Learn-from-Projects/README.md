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
- ***通过访问手机端爬取58同城商品信息***
  ```python
  from bs4 import BeautifulSoup
  import requests

  headers = {
      'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1',
      'Cookie': 'f=n; id58=c5/njVxX0KFx5NhuR0H4Ag==; city=bj; 58home=bj; 58tj_uuid=a06e80b8-1250-4f67-a7f7-89aece13e16c; new_uv=1; utm_source=; spm=; init_refer=; als=0; xxzl_deviceid=kV1ATXiudAWv5zyZcxuABiO67foT3kEok%2FQahFJHx1bAYi79lOMzAMixZqPLQKs3; sessionid=29cee45d-54fb-4071-8db7-64445e223d07; new_session=0; gr_user_id=68904093-7ace-4b7b-9ae9-2e2196334187; gr_session_id_98e5a48d736e5e14=17efbb4b-ce29-409b-9028-ec36f6596201; _ga=GA1.2.803555990.1549259044; _gid=GA1.2.155562628.1549259044; Hm_lvt_e2d6b2d0ec536275bb1e37b421085803=1549259054; final_history=37012114400913; wmda_uuid=d641576fae76e691b9d99f42786c554b; wmda_new_uuid=1; wmda_session_id_1409632296065=1549259055478-7eb9c6c0-63cc-b35b; Hm_lpvt_e2d6b2d0ec536275bb1e37b421085803=1549259538; ppStore_fingerprint=C9371F482F4270E49828E3F45A3ED5A2572F9698D6357955%EF%BC%BF1549259539179; _gat=1; device=m; cookieuid=91b5266f-e186-4729-93ba-662bfe9b1db5; wmda_session_id_1444510081921=1549259578897-1feee481-e0a4-2696; wmda_visited_projects=%3B1409632296065%3B1444510081921; gr_session_id_8154da2f94e51dff=b9687de6-5742-4ba1-8a4e-917f8a1c39c1; qz_gdt=; GA_GTID=0d409654-02fb-3c93-8896-17afff5623d8; Hm_lvt_13822dc0c5601dfc5165fd2b6c48b91d=1549259580; Hm_lpvt_13822dc0c5601dfc5165fd2b6c48b91d=1549259580; gr_session_id_8154da2f94e51dff_b9687de6-5742-4ba1-8a4e-917f8a1c39c1=true; _sale_detail_show_time_=2'
  }
  url = 'https://bj.58.com/pingbandiannao/37012114400913x.shtml?psid=198261563203064481199563272&entinfo=37012114400913_p&slot=-1&iuType=p_1&PGTID=0d305a36-0000-1f31-4c9d-431e2e1be1a2&ClickID=1'

  def get_item_info(url):
      html = requests.get(url, headers=headers)
      soup = BeautifulSoup(html.text, 'lxml')
      data = {
          'title': soup.title.text.strip(),
          'price': soup.select('div.titleArea-price')[0].get_text().strip(),
          'date': soup.select('p.time')[0].get_text().strip(),
          'area': soup.select('.icon-location')[0].get_text().strip()
      }
      print(data)

  get_item_info(url)
  ```
