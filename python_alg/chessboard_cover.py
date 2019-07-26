# -*- coding: utf-8 -*-  
import sys

"""
---------------------------------
|   |   |   |   |   |   |   | -1|
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------


问题: 8x8的棋盘，-1表示缺了一角，用L形砖填满这个棋盘
 
递归解决该问题：
由于是正方形，而且边长是2的幂次方，可以将正方形分成四个子正方形，并且在四个正方形交界的四个点放入L形砖块，这样可以让每个子正方形都缺一个角块
然后对四个子正方形递归，直到边长为1返回
这样整个图形都会被L形砖块填满

注意，该图形必须是边长为2的n次方的正方形，且缺的一块一定在角上，才能用这种方法解决
"""

def cover(board, lab=1, top=0, left=0, side=None):
    if side is None:
        side = len(board)

    s = side//2
    offsets = (0, -1), (side-1, 0)

    for dy_outer, dy_inner in offsets:
        for dx_outer, dx_inner in offsets:
            # 如果这个子正方形的角块没有被填充，则用当前砖块的编号填充中间交接点，
            # 四个正方形中必定只有一个角块已被填充，所以L形砖一定能填到中间交接的正方形中
            if not board[top+dy_outer][left+dx_outer]:
                board[top+s+dy_inner][left+s+dx_inner] = lab
                
    lab += 1
    if s > 1:
        for dy in [0, s]:
            for dx in [0, s]:
                lab = cover(board, lab, top+dy, left+dx, s)
                
    return lab
    
    
if __name__ == '__main__':

    w = 8
    if len(sys.argv) >= 2:
        w = int(sys.argv[1])
        
        # 判断w是否是2的幂次方
        if w & (w-1):
            print('Width of the board must be nth power of 2')
            sys.exit(0)
            
    board = [[0]*w for i in range(w)]
    board[w-1][w-1] = -1
    
    cover(board)
    
    for row in board:
        print(" %2i"*w % tuple(row))
