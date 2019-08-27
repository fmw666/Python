'''
从excel总表中取得自己班同学成绩，并算出学分加权的平均成绩

ATTENTION：
1. '2019-2020第二学期2017级学生成绩汇总表.xls' 为学院发的年级总成绩表（请勿乱改格式）
2. '班级同学信息表.xls' 为班级成绩表，请预先自己创建该表
    并且要注意：3A-4A-5A-...为班级同学学号、3B-4B-5B-...为班级同学姓名，请预先完成
'''
import numpy as np
from xlrd import open_workbook
from xlutils.copy import copy

# 待完成的班级成绩表，后称表1
xls1 = open_workbook('班级同学信息表.xls',)
excel = copy(xls1)
stu_info = xls1.sheets()[0]  # 表1子表Sheet0，可读取
xls1_sheet = excel.get_sheet(0)  # 表1子表Sheet0，不可读取

# 年级总成绩表（源数据提取表），后称表2
xls2 = open_workbook('2019-2020第二学期2017级学生成绩汇总表.xls')
score_info = xls2.sheets()[0]  # 表2子表Sheet0，可读取

# 填补信息提示
xls1_sheet.write(0, 1, '对应学分')
xls1_sheet.write(1, 0, '学号')
xls1_sheet.write(1, 1, '姓名')

'''
需自行修改列表科目名
'''
course_list = [
    '单片机接口与技术',
    '传感器技术',
    '操作系统',
    '数据库原理',
    '计算机组成原理',
    '大学体育4',
    '形势与政策2',
    '马克思主义基本原理概论',
]  # 一共8门课

# 总学分
total_credit = 0

# 填补课程信息
for i in range(len(course_list)):
    course = course_list[i]
    xls1_sheet.write(1, 2+i, course)
    for j in range(len(score_info.col_values(7))):
        if course == str(score_info.col_values(7)[j]):
            credit = float(score_info.col_values(10)[j])
            total_credit += credit
            xls1_sheet.write(0, 2 + i, credit)
            break

# 填补加权“平均分”分栏
xls1_sheet.write(1, 2+len(course_list), '平均分')

for stu in range(stu_info.nrows-2):
    # 0-63
    stu_id = int(stu_info.col_values(0)[stu + 2])
    # 所有学生
    id_list = score_info.col_values(11)
    # 一共8个科目
    total = 0
    # 每个学生加权分
    credit_score = 0
    # 查询每个学生在学生列表中情况
    for i in range(1,len(id_list)):
        # 查到当前学生列
        if stu_id == int(id_list[i]):
            # 得到当前列的科目，并判断是否和我的科目相同
            if str(score_info.col_values(7)[i]) == course_list[total]:
                # 相同则得到该科成绩
                score = float(score_info.col_values(18)[i])
                # 得到 学分x成绩
                credit_score += score * score_info.col_values(10)[i]
                # 写入对应位置
                xls1_sheet.write(stu+2,total+2,score)
                # 可以进行下一科了
                total += 1
                # 完成所有科目查询
                if total == len(course_list):
                    average_score = credit_score/total_credit
                    xls1_sheet.write(stu+2,total+2,average_score)
                    # 退出
                    break

excel.save('2019-2020第二学期计科2017级1班期末成绩.xls')