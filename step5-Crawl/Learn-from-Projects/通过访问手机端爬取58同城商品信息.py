from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1',
    'Cookie': 'f=n; id58=c5/njVxX0KFx5NhuR0H4Ag==; city=bj; 58home=bj; 58tj_uuid=a06e80b8-1250-4f67-a7f7-89aece13e16c; new_uv=1; utm_source=; spm=; init_refer=; als=0; xxzl_deviceid=kV1ATXiudAWv5zyZcxuABiO67foT3kEok%2FQahFJHx1bAYi79lOMzAMixZqPLQKs3; sessionid=29cee45d-54fb-4071-8db7-64445e223d07; new_session=0; gr_user_id=68904093-7ace-4b7b-9ae9-2e2196334187; gr_session_id_98e5a48d736e5e14=17efbb4b-ce29-409b-9028-ec36f6596201; _ga=GA1.2.803555990.1549259044; _gid=GA1.2.155562628.1549259044; Hm_lvt_e2d6b2d0ec536275bb1e37b421085803=1549259054; final_history=37012114400913; wmda_uuid=d641576fae76e691b9d99f42786c554b; wmda_new_uuid=1; wmda_session_id_1409632296065=1549259055478-7eb9c6c0-63cc-b35b; Hm_lpvt_e2d6b2d0ec536275bb1e37b421085803=1549259538; ppStore_fingerprint=C9371F482F4270E49828E3F45A3ED5A2572F9698D6357955%EF%BC%BF1549259539179; _gat=1; device=m; cookieuid=91b5266f-e186-4729-93ba-662bfe9b1db5; wmda_session_id_1444510081921=1549259578897-1feee481-e0a4-2696; wmda_visited_projects=%3B1409632296065%3B1444510081921; gr_session_id_8154da2f94e51dff=b9687de6-5742-4ba1-8a4e-917f8a1c39c1; qz_gdt=; GA_GTID=0d409654-02fb-3c93-8896-17afff5623d8; Hm_lvt_13822dc0c5601dfc5165fd2b6c48b91d=1549259580; Hm_lpvt_13822dc0c5601dfc5165fd2b6c48b91d=1549259580; gr_session_id_8154da2f94e51dff_b9687de6-5742-4ba1-8a4e-917f8a1c39c1=true; _sale_detail_show_time_=2'
}
url = 'https://bj.58.com/pingbandiannao/37012114400913x.shtml?psid=198261563203064481199563272&entinfo=37012114400913_p&slot=-1&iuType=p_1&PGTID=0d305a36-0000-1f31-4c9d-431e2e1be1a2&ClickID=1'

# .uv
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
