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
