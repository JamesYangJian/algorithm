import numpy as np
from copy import deepcopy


class dfsSearch:
    def __init__(self):
        self.result_set = []
        self.directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]

    def pt_in_list(self, pt):
        for result in self.result_set:
            if pt in result:
                return True

        return False

    def find_serials_from_start_point(self, m, pt, result):
        result.append(pt)
        end_point = True
        
        for k in xrange(0, len(self.directions)):
            next_pt = map(lambda (pt1, pt2):pt1+pt2, zip(pt, self.directions[k]))
            if next_pt[0] < 0 or next_pt[0] >= m.shape[0]:
                continue
            elif next_pt[1] < 0 or next_pt[1] >= m.shape[1]:           
                continue
            elif m[next_pt[0]][next_pt[1]] - m[pt[0]][pt[1]] != 1:           
                continue
            else:
                end_point = False
                self.find_serials_from_start_point(m, next_pt, result)
                result.pop(len(result) - 1)

        if end_point and len(result) > 1 and not result in self.result_set:
            tmp_ret = deepcopy(result)
            self.result_set.append(tmp_ret)



    def find_max_continous_serial(self, m):
        x, y = m.shape
        
        for row in xrange(0, x):
            for col in xrange(0, y):
                start_point = True
                pt = [row, col]
                for k in xrange(0, len(self.directions)):
                    next_pt = map(lambda (pt1, pt2):pt1+pt2, zip(pt, self.directions[k]))
                    if next_pt[0] < 0 or next_pt[0] >= m.shape[0]:
                        continue
                    elif next_pt[1] < 0 or next_pt[1] >= m.shape[1]:             
                        continue
                    if m[pt[0]][pt[1]] - m[next_pt[0]][next_pt[1]] == 1:
                        # it's not the start point, skip it
                        start_point = False
                        break
                if start_point and not self.pt_in_list(pt):
                    result = []
                    self.find_serials_from_start_point(m, pt, result)


if __name__ == '__main__':
    m = np.array([[1,  2,  3,  5,  11, 12, 7,  3 ],
                  [2,  9,  8,  7,  6,  5,  12, 13],
                  [0,  3,  2,  6,  4,  7,  11, 14],
                  [7,  6,  5,  4,  1,  9,  10, 9 ],
                  [19, 20, 28, 27, 31, 8,  7,  4],
                  [5,  17, 33, 40, 82, 5,  0,  3],
                  [3,  8,  32, 9,  7,  8,  5,  3],
                  [2,  1,  31, 30, 6,  5,  4,  1]])

    print m
    print m.shape

    search = dfsSearch()
    search.find_max_continous_serial(m)

    print 'Total result: %d' % (len(search.result_set))

    max_len = 0
    max_path = ''

    num = 0
    for result in search.result_set:
        path = ''
        num += 1
        for pt in result:
            path = (path + ' ' + str(m[pt[0]][pt[1]]))
        length = len(result)
        if length > max_len:
            max_len = length
            max_path = path
            max_pt_set = deepcopy(result)
        print '------Result set number: %d--------' % num
        print result
        print path

    print '-------max_length is %d---------' % (max_len)
    print max_path
    print max_pt_set