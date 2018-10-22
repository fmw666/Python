# -*- coding: utf-8 -*-  

import csv

def get_college_list():
    with open('college_list.csv',encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        college_list = []
        for row in readCSV:
            college = {}
            college['code'] = row[0]
            college['name'] = row[1]
            college_list.append(college)
        return college_list

