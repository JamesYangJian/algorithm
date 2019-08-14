import math
import sys
import functools
import matplotlib.pyplot as plt
"""
Find the nearest two points in a plane, only run on Python3

1. Sort the point list in x-axis
2. Divide the list into two parts and recurse 
3. Find the minimal distance in left part
4. Find the minimal distance in right part
5. Find the minimal distance in center part (within the minimal distance so far around the mid)
6. return the minimal distance and point

refer to: https://www.cnblogs.com/zyxStar/p/4591897.html

It's a typical Divide-Conqurer-Merge with 2T(n/2) + f(n)

But I am not sure if f(n) is approaching O(n), since it will iterate all points to find the minimal distance,
Although I limited the x-distance between two points must be less than m

From the matplotlib figure, the code runs well
But it seems a little bit complex

"""

def cmp_by_x(P1, P2):
    if P1['x'] > P2['x']:
        return 1
    elif P1['x'] == P2['x']:
        return 0
    else:
        return -1

def calc_distance(P1, P2):
    distance = math.sqrt((P1['x'] - P2['x']) ** 2 + (P1['y'] - P2['y']) ** 2)

    return distance 

def find_points_nearer_than_m(pts, pt_lists, m):
    min_dis = m
    min_pts = []

    if len(pt_lists) <= 1:
        return min_dis, min_pts

    sorted_pt_lists = sorted(pt_lists)


    for i in range(len(sorted_pts)):
        for j in range(i+1, len(sorted_pts)):
            if abs(pts[i]['x'] - pts[j]['x']) > m:
                break
            elif abs(pts[i]['y'] - pts[j]['y']) > m:
                continue

            distance = calc_distance(pts[i], pts[j])
            if distance < min_dis:
                min_dis = distance
                min_pts = [i, j]

    return min_dis, min_pts


def search_nearest_points(pts, start, end):

    nearest_pts = []
    if start == end:
        nearest_pts = [start, end]
        return sys.maxsize, nearest_pts
    elif start == (end - 1):
        nearest_pts = [start, end]
        return calc_distance(pts[start], pts[end]), nearest_pts


    # divide
    mid = (start + end) // 2
    left_min, left_pts = search_nearest_points(pts, start, mid)
    right_min, right_pts = search_nearest_points(pts, mid+1, end)

    # merge
    (min_dis, min_pts) = (left_min, left_pts) if left_min < right_min else (right_min, right_pts)

    mid_pt_sets = []
    left_idx = mid
    right_idx = mid + 1
    x_mid = pts[mid]['x']
    while left_idx >= start:
        if abs(pts[left_idx]['x'] - x_mid) <= min_dis:
            mid_pt_sets.append(left_idx)
            left_idx -= 1
        else:
            break

    while right_idx <= end:
        if abs(pts[right_idx]['x'] - x_mid) <= min_dis:
            mid_pt_sets.append(right_idx)
            right_idx += 1
        else:
            break

    mid_dis, mid_pts = find_points_nearer_than_m(pts, mid_pt_sets, min_dis)

    if mid_dis < min_dis:
        min_dis = mid_dis
        min_pts = mid_pts

    return min_dis, min_pts



if __name__ == '__main__':
    import random

    if len(sys.argv) < 2:
        number = 10
    else:
        number = int(sys.argv[1])

    Pts = [ {'x': random.randint(0, 100), 'y': random.randint(0, 100)} for i in range(number)]

    x_list = [p['x'] for p in Pts]
    y_list = [p['y'] for p in Pts]

    plt.plot(x_list, y_list, 'ro')


    print(Pts)

    sorted_pts = sorted(Pts, key=functools.cmp_to_key(cmp_by_x))

    print(sorted_pts)

    dis, points = search_nearest_points(sorted_pts, 0, len(sorted_pts)-1)

    pt1 = sorted_pts[points[0]]
    pt2 = sorted_pts[points[1]]

    print('The smallest distance is:%f' % dis)
    print("Point1 %s" % str(pt1))
    print("Point2 %s" % str(pt2))

    plt.plot([pt1['x'], pt2['x']], [pt1['y'], pt2['y']])
    plt.show()

