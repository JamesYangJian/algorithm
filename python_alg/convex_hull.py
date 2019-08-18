import math
import sys
import functools
import matplotlib.pyplot as plt

"""
How to find the convex edge for points in a plane
Actually, the implementation refers to 
https://blog.csdn.net/sinat_36246371/article/details/72808655
https://www.geeksforgeeks.org/tangents-two-convex-polygons/

To be honest, the 1st edition just translated code in the link from c++ to python
Usage divide and conquer for it, the step is:

1. sort the points in X-axis
2. recursive left and right parts
3. if the points number is less than 5, then brute all points to find the convex side and order them in anti-clockwise sequence
    just check all edge, if all points in the same side of the edge, then it's the points in convex list
4. merge left and right part, and order them in anti-clockwise order
    find the upper tangent and lower tangent for the two polygon, then add points from upper to lower to form a new polygon

I compare two ways for 500 points, (D&C, Brute directly), the result is as below:
D&C: 0.007566   O(nlogn)
Brute: 20.843546 O(n3)

That's huge gap!!!! 

This code is not optimized both in coding and efficiency, but the algorithm plays really important roles!!
Also, the mathmatics in such kind of problems is very import, or I can't get any clues for the solution!!

"""

mid = {'x':0, 'y':0}

def cmp_by_x(P1, P2):
    if P1['x'] > P2['x']:
        return 1
    elif P1['x'] == P2['x']:
        return 0
    else:
        return -1

# check the quadriant of the points
def quad(pt):
    x = pt['x']
    y = pt['y']

    if x>=0 and y >= 0:
        return 1

    if x <= 0 and y >= 0:
        return 2

    if x <= 0 and y <= 0:
        return 3

    return 4 


def cmp(pt1, pt2):

    # print('pt1:%s pt2%s' % (str(pt1), str(pt2)))
    p1 = {}
    p1['x'] = pt1['x'] - mid['x']
    p1['y'] = pt1['y'] - mid['y']

    p2 = {}
    p2['x'] = pt2['x'] - mid['x']
    p2['y'] = pt2['y'] - mid['y']

    # print('p1:%s p2%s' % (str(p1), str(p2)))

    q1 = quad(p1)
    q2 = quad(p2)

    # print("q1:%d q2:%d" % (q1, q2))

    if (q1 != q2):
        if q1 > q2:
            ret = 1
        else:
            ret = -1
    else:
        v1 = p1['y'] * p2['x']
        v2 = p2['y'] * p1['x']

        if v1 > v2:
            ret = 1
        elif v1 == v2:
            ret = 0
        else:
            ret = -1

    # print("ret: %d" % ret)

    return ret

def brute_hull(Pts, start, end):
    pt_num = end - start + 1

    convex_hull_set = set()
    convex_hull_list = []

    # print('Total number is :%d' % pt_num)

    for i in range(start, end+1):
        for j in range(i+1, end+1):
            x1 = Pts[i]['x']
            x2 = Pts[j]['x']
            y1 = Pts[i]['y']
            y2 = Pts[j]['y']

            a = y1 - y2
            b = x2 - x1
            c = x1*y2 - x2*y1
            pos = 0
            neg = 0
            for k in range(start, end+1):
                x = Pts[k]['x']
                y = Pts[k]['y']

                if a*x+b*y+c >= 0:
                    pos += 1
                if a*x+b*y+c <= 0:
                    neg += 1

            # All points in one side of the vector, then the two points should in convex point list
            # print("Side: %s %s pos:%d neg:%d" % (str(Pts[i]), str(Pts[j]), pos, neg))
            if pos == pt_num or neg == pt_num:
                convex_hull_set.add(i)
                convex_hull_set.add(j)

    # Sorting the points in the anti-clockwise order
    for pt in convex_hull_set:
        convex_hull_list.append(Pts[pt])

    mid['x'] = 0
    mid['y'] = 0

    num = len(convex_hull_list)
    for i in range(num):
        mid['x'] += convex_hull_list[i]['x']
        mid['y'] += convex_hull_list[i]['y']
        convex_hull_list[i]['x'] *= num
        convex_hull_list[i]['y'] *= num

    convex_hull_list = sorted(convex_hull_list, key=functools.cmp_to_key(cmp))

    for i in range(num):
        convex_hull_list[i]['x'] /= num
        convex_hull_list[i]['y'] /= num

    return convex_hull_list

def orientation(pt1, pt2, pt):
    res = (pt2['y'] - pt1['y']) * (pt['x'] - pt2['x']) - (pt['y'] - pt2['y']) * (pt2['x'] - pt1['x'])

    if res == 0:
        return 0
    if res > 0:
        return 1;
    return -1;


def merge_polygon(convex1, convex2):
    # Suppose convex1 and convex2 are sorted in anti-clockwise order

    # 1. find rightmost point in convex1 and leftmost convex2
    num1 = len(convex1)
    num2 = len(convex2)

    # print("convex1: %s" % str(convex1))
    # print("convex2: %s" % str(convex2))

    idx1 = 0
    for i in range(1, num1):
        if convex1[i]['x'] > convex1[idx1]['x']:
            idx1 = i

    idx2 = 0
    for i in range(1, num2):
        if convex2[i]['x'] < convex2[idx2]['x']:
            idx2 = i

    # 2. find upper tangent
    ind1 = idx1
    ind2 = idx2
    done = False
    while not done:
        done = True
        while (orientation(convex2[ind2], convex1[ind1], convex1[(ind1 + 1)%num1]) >= 0):
            ind1 = (ind1 + 1) % num1

        while (orientation(convex1[ind1], convex2[ind2], convex2[(num2 + ind2 -1)%num2]) <= 0):
            done = False
            ind2 = (num2 + ind2 - 1) % num2

    upper1 = ind1
    upper2 = ind2

    # 3. find lower tangent
    ind1 = idx1
    ind2 = idx2
    done = False
    while not done:
        done = True
        while (orientation(convex1[ind1], convex2[ind2], convex2[(ind2+1) % num2]) >= 0):
            ind2 = (ind2 + 1) % num2

        while (orientation(convex2[ind2], convex1[ind1], convex1[(num1 + ind1 - 1) % num1]) <=0 ):
            done = False
            ind1 = (num1 + ind1 - 1) % num1

    lower1 = ind1
    lower2 = ind2

    # 4. merge the two part into a list
    ret = []
    ind = upper1
    ret.append(convex1[ind])
    while ind != lower1:
        ind = (ind + 1) % num1
        ret.append(convex1[ind])

    ind = upper2
    ret.append(convex2[ind])
    while ind != lower2:
        ind = (num2 + ind - 1) % num2
        ret.append(convex2[ind])

    mid['x'] =0
    mid['y'] =0
    num = len(ret)
    for i in range(num):
        mid['x'] += ret[i]['x']
        mid['y'] += ret[i]['y']
        ret[i]['x'] *= num
        ret[i]['y'] *= num

    ret = sorted(ret, key=functools.cmp_to_key(cmp))

    for i in range(num):
        ret[i]['x'] /= num
        ret[i]['y'] /= num

    return ret
    
def divide_and_conquer_hull(Pts, start, end):
    length = end - start + 1

    if length <= 5:
        return brute_hull(Pts, start, end)

    mid_value = (start + end) // 2

    convex_left = divide_and_conquer_hull(Pts, start, mid_value)
    convex_right = divide_and_conquer_hull(Pts, mid_value+1, end)

    convex_list = [convex_left, convex_right]
    #plot_pts_and_convex(Pts, convex_list)

    ret = merge_polygon(convex_left, convex_right)

    return ret

def plot_pts_and_convex(Pts, convex_list):

    x_list = [p['x'] for p in Pts]
    y_list = [p['y'] for p in Pts]

    plt.plot(x_list, y_list, 'ro')

    for convex in convex_list:
        start_pt = convex[0]
        num = len(convex)
        for i in range(1, num):
            end_pt = convex[i]
            plt.plot([start_pt['x'], end_pt['x']], [start_pt['y'], end_pt['y']])
            start_pt = end_pt

        end_pt = convex[0]
        plt.plot([start_pt['x'], end_pt['x']], [start_pt['y'], end_pt['y']])
    plt.show()


if __name__ == '__main__':
    import random
    import time

    if len(sys.argv) < 2:
        number = 10
    else:
        number = int(sys.argv[1])

    Pts = [ {'x': random.randint(0, 1000), 'y': random.randint(0, 1000)} for i in range(number)]

    Pts = sorted(Pts, key=functools.cmp_to_key(cmp_by_x))

    # print(Pts)


    # convex_hull_list = brute_hull(Pts)
    start = time.time()
    convex_hull_list = divide_and_conquer_hull(Pts, 0, len(Pts)-1)
    usage = time.time() - start
    print("Divide and Conquer: usage: %f" % usage)

    plot_pts_and_convex(Pts, [convex_hull_list])

    # print('------Convex Hull--------')
    # print(convex_hull_list)

    start = time.time()
    convex_hull_list = brute_hull(Pts, 0, len(Pts) - 1)
    usage = time.time() - start
    print('Brute: usage: %f' % usage)
    plot_pts_and_convex(Pts, [convex_hull_list])

