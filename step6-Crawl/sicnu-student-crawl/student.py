import requests
from bs4 import BeautifulSoup


def get_student_detail(card_code):
    url = "http://202.115.194.53:2222/"
    querystring = {"CardType": "StudentCard",
                   "stdCardID": "", "cardCode": card_code}
    headers = {
        'Connection': "keep-alive",
        'Cache-Control': "no-cache",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Postman-Token': "d60c2ab9-a273-4e3b-a0b3-000d92884325"
    }
    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    soup = BeautifulSoup(response.text, "html.parser")
    student_number = soup.find("span", id="lblStdNum")
    student_name = soup.find("span", id="lblName")
    student_class = soup.find("span", id="lblClass")
    college = soup.find("span", id="lblCollege")
    major = soup.find("span", id="lblMajor")
    gender = soup.find("span", id="lblSex")
    nation = soup.find("span", id="lblNation")
    student_pic_url = soup.find("img", id="usePhoto")
    student = {}
    if student_number and student_name.text is not '':
        student['name'] = student_name.text
        student['number'] = student_number.text
        student['class'] = student_class.text
        student['college'] = college.text
        student['major'] = major.text
        student['gender'] = gender.text
        student['nation'] = nation.text
        if student_pic_url:
            student['pic_url'] = "http://202.115.194.53:2222/" + \
                student_pic_url['src']
        return student
    else:
        return None

