# 定义一个无穷大值
INF = 9999
# 图的顶点起始索引值
START_INDEX = 0
# 文件保存信息--字符串
OUTPUT_STR = ''

# 矩阵类，存储邻接矩阵有效信息
# category='0'代表无向图、='1'代表有向图
class Matrix(object):

    def __init__(self, vexnum, edge, category):
        self.vexnum   = vexnum
        self.edge     = edge
        self.category = category
        
    def create_matrix(self):
        self.mgraph = [[INF]*vexnum for i in range(vexnum)]
        print('==请依次输入每条边两个顶点以及其权重==')
        print('(如：v' + str(START_INDEX) \
            + '->v' + str(START_INDEX + 1) \
            + ' : 2，则依次输入：' + str(START_INDEX) \
            + ' ' + str(START_INDEX + 1) + ' 2)')
        count = 1
        while count <= self.edge:
            if count == 1:
                print('---')
            start  = int(input('第' + str(count) + '条边第一个顶点：'))
            end    = int(input('第' + str(count) + '条边第二个顶点：'))
            weight = int(input('第' + str(count) + '条边第权重：'))
            print('---')
            self.mgraph[start-START_INDEX][end-START_INDEX] = weight
            # 无向图情况
            if self.category == '0':
                self.mgraph[end-START_INDEX][start-START_INDEX] = weight
            count += 1

    def print_matrix(self):
        global OUTPUT_STR
        print('\n==图的邻接矩阵==')
        OUTPUT_STR = OUTPUT_STR + '==图的邻接矩阵==\n'
        # 行数
        for row in range(self.vexnum):
            # 列数
            for col in range(self.vexnum):
                if self.mgraph[row][col] == INF and row != col:
                    print('∞ ',end='')
                    OUTPUT_STR = OUTPUT_STR + '∞ '
                elif row == col:
                    print('0 ',end='')
                    OUTPUT_STR = OUTPUT_STR + '0 '
                else:
                    print(str(self.mgraph[row][col]) + ' ', end='')
                    OUTPUT_STR = OUTPUT_STR + str(self.mgraph[row][col]) + ' '
            print('')
            OUTPUT_STR = OUTPUT_STR + '\n'

    def print_shortest_dis(self):
        global OUTPUT_STR
        for v in range(self.vexnum):
            self.info = []
            PATH, VALUE, VISIT = 0, 1, 2
            # 从第一个顶点开始到最后一个顶点结束
            for vex in range(self.vexnum):
                # 设置当前路径信息
                path = 'v' + str(v + START_INDEX) + ' -> v' + str(vex + START_INDEX)
                value = self.mgraph[v][vex]
                visit = False
                self.info.append([path, value, visit])
            # 找到自己点
            self.info[v][VISIT] = True

            count = 1
            # 计算剩余顶点的最短路径
            while count != self.vexnum:
                # temp 保存 info 数组中最小的下标
                # minv 记录当前的最小值
                temp = 0
                minv = INF
                for i in range(self.vexnum):
                    if not self.info[i][VISIT] and self.info[i][VALUE] < minv:
                        minv = self.info[i][VALUE]
                        temp = i
                self.info[temp][VISIT] = True
                count += 1
                for i in range(self.vexnum):
                    if not self.info[i][VISIT] and self.mgraph[temp][i] != INF and (self.info[temp][VALUE] + self.mgraph[temp][i]) < self.info[i][VALUE]:
                        self.info[i][VALUE] = self.info[temp][VALUE] + self.mgraph[temp][i]
                        self.info[i][PATH]  = self.info[temp][PATH] + ' -> v' + str(i + 1)
            print('\n==以 v' + str(v + START_INDEX) + ' 为起点到任意点的最短路径==')
            OUTPUT_STR = OUTPUT_STR + '\n==以 v' + str(v + START_INDEX) + ' 为起点到任意点的最短路径==\n'
            for idx in range(self.vexnum):
                if self.info[idx][VALUE] != INF:
                    print(self.info[idx][PATH] + ' = ' + str(self.info[idx][VALUE]))
                    OUTPUT_STR = OUTPUT_STR + \
                        self.info[idx][PATH] + ' = ' + \
                        str(self.info[idx][VALUE]) + '\n'
                else:
                    print(self.info[idx][PATH] + ' 不存在最短路径')
                    OUTPUT_STR = OUTPUT_STR + \
                        self.info[idx][PATH] + ' 不存在最短路径\n'

    def save_result(self, filename):
        with open(filename + '.txt', 'w', encoding='utf-8') as fp:
            fp.write(OUTPUT_STR)
            fp.close()

def checkve(vexnum, edge):
    if  vexnum <=0 \
        or edge <=0 \
        or ((vexnum*(vexnum-1))/2) < edge:
        return False
    return True

if __name__ == "__main__":
    '''
    输入参数：图的相关信息 (顶点数、边数、图的类型)
    顶点个数 i 生成顶点为：v0、v1……vi-1(即顶点下标默认从0开始)
    边与顶点个数关系：((vexnum*(vexnum - 1)) / 2) < edge

    输出结果：邻接矩阵、vi 到除自己点以外任意点的最短距离
    (即任意两点间的最短距离)

    作者：fmw666 (github 用户名)
    代码开源于：https://github.com/fmw666/
    '''
    print('==请输入相关图信息==')
    vexnum = int(input('顶点个数：'))
    edge   = int(input('边的条数：'))
    while not checkve(vexnum, edge):
        print('输入点/边信息有误，请重新输入！')
        vexnum = int(input('顶点个数：'))
        edge   = int(input('边的条数：'))
    ans = input('请确认图的类型：0.无向图  1.有向图\n输入序号：')
    print('\n==请自定义你的顶点下标起始索引==')
    START_INDEX = int(input('(推荐起始索引为 0 或 1)：'))
    OUTPUT_STR = OUTPUT_STR + '==图的相关信息==\n顶点个数：' + str(vexnum)\
        + '\n边的条数：' + str(edge) + '\n图的类型：'
    if ans == '0' or ans == '1' and START_INDEX > 0: 
        print('\n==请确认输入信息==\n顶点个数：' + str(vexnum)\
            + '\n边的条数：' + str(edge))
        if ans == '0':
            print('图的类型：无向图')
            OUTPUT_STR = OUTPUT_STR + '无向图\n'
        elif ans == '1':
            print('图的类型：有向图')
            OUTPUT_STR = OUTPUT_STR + '有向图\n'
        print('起始索引：v' + str(START_INDEX) + '\n')
        OUTPUT_STR = OUTPUT_STR + '起始索引：v' + str(START_INDEX) + '\n\n'
    else:
        print('输入有误，请从给出序号中进行选择！')

    matrix = Matrix(vexnum, edge, ans)

    matrix.create_matrix()
    matrix.print_matrix()
    matrix.print_shortest_dis()
    ifsave = input('\n\n==是否保存当前结果到当前文件夹下？==\n（0.否  1.是）：')
    if ifsave == '1':
        filename = input('\n请输入文件名（默认扩展名为.txt）：')
        matrix.save_result(filename)
        print('保存成功！程序已运行完成，请在当前目录下查看查看保存文件。')
