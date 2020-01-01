# -*- coding: utf-8 -*-

'''
sudoku的一个解法：
1. 数据结构：
total: nxn矩阵，每一个点保存当前点可能的取值，最开始每个点都是1-9
confirmed_set: 集合，每一个元素为三元组，（row， col， value），表示一个确定的点及其取值
actual： 九宫格内容， 根据total和confirmed确定的当前九宫格的取值，确定的填入，不确定的填0

2. 计算过程
2.1 循环以下过程
  a). 根据传入的confirmed_set, 排除total中每个点不可能出现的数字
  b). 根据新的total表，找出新的能够确认的点，加入到confirmed_set列表
  c). 如果没有新的确认点了，推出循环，否则继续循环

3.1 依照从上到下，从左到右的方式试验每一个点可能的取值， 从第一个点开始
  a). 取当前点可能的取值列表，进行迭代
  b). 拷贝total和confirmed_set的快照new_total, new_confirmed_set
  c). 将(row, col, possible_v)加入new_confirmed_set
  d). 使用new_total和new_confirmed_set进行步骤2.1，计算加入新点之后可能的引起的变化
  e). 如果new_confirmed_set长度为nxn了，说明成功，返回True
  f). 使用new_total, new_confirmed_set，并找到下一个值不确定的点，递归调用guess (3.1)
  g). 如果递归调用返回False，说明本次猜测失败，取下一个可能值，从a)开始执行
  h). 如果递归调用返回True， 说明本次猜测成功，将new_confirmed_set和new_total拷贝回confirmed_set和total，返回True
  j). 如果可能的点都迭代完了，则返回False，说明上一轮的猜测失败了

3.2 如果猜测失败，说明这局数独输入错误，如果猜测成功，则该局已经解开，打印actual即可

'''

import numpy as np
import copy
import sys
import time


class SudokuSolution(object):
    def __init__(self, level, confirmed_set):
        self.level = level
        self.length = level*level
        self.set_confirmed_set(confirmed_set)

    def set_confirmed_set(self, confirmed_set):
        self.confirmed_set = confirmed_set
        self.total = [[[i for i in range(1, self.length+1)] for j in range(self.length)] for k in range(self.length)]
        self.parse_actual(self.total, self.confirmed_set)

    def get_matrix_row_num(self, x):
        return int(x/self.level)

    def get_matrix_col_num(self, y):
        return int(y/self.level)

    def parse_actual(self, total, confirmed_set):
        self.actual = [[0 for i in range(self.length)] for j in range(self.length)]

        for confirmed in confirmed_set:
            r, c, v = confirmed
            self.actual[r][c] = v

            total[r][c] = [v]


    def check_valid(self, r, c, v):
        # check by col
        for col in range(self.length):
            if col != c and self.actual[r][col] == v:
                return False

        # check by row
        for row in range(self.length):
            if row != r and self.actual[row][c] == v:
                return False

        # check by sub-matrix
        sub_matrix_row = self.get_matrix_row_num(r)
        sub_matrix_col = self.get_matrix_col_num(c)

        x_start = sub_matrix_row * self.level
        y_start = sub_matrix_col * self.level
        for row in range(x_start, x_start+self.level):
            for col in range(y_start, y_start+self.level):
                if row != r and col != c and self.actual[row][col] == v:
                    return False

        return True

    def apply_confirmed(self, r, c, v, total):
        # apply by row
        for col in range(self.length):
            if col != c and v in total[r][col]:
                total[r][col].remove(v)

        # apply by col
        for row in range(self.length):
            if row != r and v in total[row][c]:
                total[row][c].remove(v)

        # apply by sub-matrix
        sub_matrix_row = self.get_matrix_row_num(r)
        sub_matrix_col = self.get_matrix_col_num(c)
        row_start = sub_matrix_row * self.level
        col_start = sub_matrix_col * self.level

        for row in range(row_start, row_start+self.level):
            for col in range(col_start, col_start+self.level):
                if row != r and col != c and v in total[row][col]:
                    total[row][col].remove(v)

    def find_new_confirmed(self, total, confirmed_set):
        new_confirmed_found = False
        # find in each row
        for row in range(self.length):
            for v in range(1, self.length+1):
                ret = [total[row].index(b) for b in total[row] if v in b]
                if len(ret) == 1:
                    new_tuple = (row, ret[0], v)
                    if len(total[row][ret[0]]) > 1 and new_tuple not in confirmed_set and self.check_valid(row, ret[0], v):
                        confirmed_set.add(new_tuple)
                        new_confirmed_found = True

        #find in each col
        for col in range(self.length):
            for v in range(1, self.length+1):
                ret = []
                for row in range(self.length):
                    if v in total[row][col]:
                        ret.append(row)
                if len(ret) == 1:
                    new_tuple = (ret[0], col, v)
                    if len(total[ret[0]][col]) > 1 and new_tuple not in confirmed_set and self.check_valid(ret[0], col, v):
                        confirmed_set.add(new_tuple)
                        new_confirmed_found = True

        # find in each sub-matrix
        row_start = 0
        col_start = 0
        for row_start in range(self.level):
            for col_start in range(self.level):
                for v in range(1, self.length+1):
                    ret = []
                    matrix_row_start = row_start * self.level
                    matrix_col_start = col_start * self.level
                    #print("row:{r}, col:{c}, v:{v}".format(r=row_start, c=col_start, v=v))
                    for r in range(matrix_row_start, matrix_row_start+self.level):
                        for c in range(matrix_col_start, matrix_col_start+self.level):

                            if v in total[r][c]:
                                ret.append((r, c))

                    if len(ret) == 1:
                        row, col = ret[0]
                        new_tuple = (row, col, v)
                        if len(total[row][col]) > 1 and new_tuple not in confirmed_set and self.check_valid(row, col, v):
                            confirmed_set.add(new_tuple)
                            new_confirmed_found = True

        return new_confirmed_found



    def exclude_useless_value(self, total, confirmed_set):
        self.parse_actual(total, confirmed_set)

        for confirmed in confirmed_set:
            r, c, v = confirmed
            self.apply_confirmed(r, c, v, total)

    def find_next_guess_point(self, row, col):
        for c in range(col, self.length):
            if self.actual[row][c] == 0:
                return row, c

        for r in range(row+1, self.length):
            for c in range(self.length):
                if self.actual[r][c] == 0:
                    return r, c

        return -1, -1

    def guess(self, row, col, total, confirmed):
        possibles = total[row][col]
        

        for v in possibles:
            print("row:{} col:{} possibles:{} v:{}".format(row, col, possibles, v))
            self.parse_actual(total, confirmed)
            if not self.check_valid(row, col, v):
                continue
            new_confirmed_set = copy.deepcopy(confirmed)
            new_total = copy.deepcopy(total)
            new_confirmed_set.add((row, col, v))

            while True:
                self.exclude_useless_value(new_total, new_confirmed_set)
                found = self.find_new_confirmed(new_total, new_confirmed_set)
                self.parse_actual(new_total, new_confirmed_set)
                if not found:
                    break

            if len(new_confirmed_set) == self.length * self.length:
                total = copy.deepcopy(new_total)
                confirmed_set = copy.deepcopy(new_confirmed_set)
                print("return when all value confirmed")
                return True
            else:
                next_row, next_col = self.find_next_guess_point(row, col)
                # print("next_row:{} next_col:{}".format(next_row, next_col))
                ret = self.guess(next_row, next_col, new_total, new_confirmed_set)
                if ret:
                    total = copy.deepcopy(new_total)
                    confirmed_set = copy.deepcopy(new_confirmed_set)
                    print("return when recursive return True")
                    return True
                else:
                    print("recursive return false")
        return False

    def sovle_puzzel(self):
        while True:
            self.exclude_useless_value(self.total, self.confirmed_set)
            found = self.find_new_confirmed(self.total, self.confirmed_set)
            self.parse_actual(self.total, self.confirmed_set)
            print("found new confirmed: {}, total confirmed:{}".format(found, len(self.confirmed_set)))
            if not found:
                break

        guess_row, guess_col = self.find_next_guess_point(0, 0)
        ret = self.guess(guess_row, guess_col, self.total, self.confirmed_set)

        if not ret:
            print("Can't find a valid solution for it??")
        else:
            self.print_matrix()

    def print_matrix(self):
        for row in range(self.length):
            print(self.actual[row])

def load_confirmed_data_from_file(filename):
    confirmed_set = set()
    try:
        with open(filename, 'r') as f:
            while True:
                line = f.readline()
                if not line or not line.rstrip():
                    break
                else:
                    
                    values = line.split()
                    confirmed_set.add((int(values[0]), int(values[1]), int(values[2])))

        return confirmed_set
    except Exception as e:
        print("File format is invalid: %s" % str(e))
        return None

def print_help():
    print("test --- automatically generate a test input")
    print("show --- view current matrix")
    print("l filename --- load data from specified file")
    print("d row col value --- delete a point")
    print("row col value --- input a row/col/value tuple")
    print("end --- finish input and begin to caculate")
    print("h --- print this message")
    print("q --- exit program")



if __name__ == '__main__':

    confirmed_set = set()
    solution = SudokuSolution(3, confirmed_set)

    while True:
        para_string = input("Input (h for help):")
        
        if para_string == "end":
            break
        elif para_string == 'q':
            sys.exit(0)
        elif para_string == 'h':
            print_help()
            continue
        elif para_string == 'test':
            confirmed_set = {(0, 3, 5), (1, 0, 3), (1, 1, 6), (2, 3, 9), (2, 4, 2), (2, 8, 1),
                    (3, 2, 9), (4, 0, 5), (4, 5, 7), (4, 6, 3), (4, 7, 6), (5, 7, 8), (6, 2, 2), (6, 8, 9),
                    (7, 5, 6), (8, 2, 8), (8, 3, 1) }
            break
        elif para_string == "show":
            solution.set_confirmed_set(confirmed_set)
            solution.print_matrix()
            continue
        elif para_string.startswith('d'):
            paras = para_string.split()
            try:
                confirmed_set.remove((int(paras[1]), int(paras[2]), int(paras[3])))
                continue
            except Exception as e:
                print("Invalid input %s" % str(e))
        elif para_string.startswith('l'):
            paras = para_string.split()
            if len(paras) < 2:
                print("Invalid command: %s!" % para_string)
                continue
            confirmed_set = load_confirmed_data_from_file(paras[1])
            if not confirmed_set:
                continue
            else:
                break
        else:
            paras = para_string.split()
            if len(paras) != 3:
                print("Invalid input!")
            else:
                try:
                    confirmed_set.add((int(paras[0]), int(paras[1]), int(paras[2])))
                except Exception as e:
                    print("Invalid input %s" % str(e))

    solution.set_confirmed_set(confirmed_set)
    print("Initial Matrix:")
    solution.print_matrix()
    start = time.time()
    solution.sovle_puzzel()
    end = time.time()
    usage = end - start
    print("Usage:{}".format(usage))

