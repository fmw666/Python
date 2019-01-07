import requests
from bs4 import BeautifulSoup
from urllib import request
import os
import json
import csv

from student import get_student_detail

from college_list import get_college_list
college_list = get_college_list()

for college in college_list[11:13]:
    for year_num in range(2015, 2018):
        students = []
        college_code = college['code']
        for class_num in range(1, 20):
            if class_num <= 10:
                class_code = str(year_num) + college_code + \
                    "0" + str(class_num)
            else:
                class_code = str(year_num) + college_code + str(class_num)
            file_path = "%s/%s/%s" % (college['name'], year_num, class_num)
            for num in range(1, 100):
                card_code = ''
                if num < 10:
                    card_code = class_code + "0" + str(num)
                else:
                    card_code = class_code + str(num)
                student = get_student_detail(card_code)
                if student is None:
                    break
                if os.path.exists(file_path) is False:
                    os.makedirs(file_path)
                if 'pic_url' in student:
                    try:
                        request.urlretrieve(
                            student['pic_url'], "./%s/%s-%s.jpg" % (file_path,  student['number'], student['name']))
                    except:
                        print("urlretrieve pic error,url:" +
                              student['pic_url'])
                students.append(student)
            print("爬取%s结束！" % (file_path))
        if students is None:
            continue
        with open("%s/%s.csv" % (college['name'], str(year_num)), 'w+', newline='', encoding="utf8") as csv_file:
            fieldnames = ['college', 'class', 'major',
                          'number', 'name', 'gender', 'nation', 'pic_url']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
