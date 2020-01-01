def cover(board, lab=1, top=0, left=0, side=None):
    if not side:
        side = len(board)
    s = side//2

    offsets= (0, -1), (side-1, 0)

    for dy_outer, dy_inner in offsets:
        for dx_outer, dx_inner in offsets:
            if not board[top+dy_outer][left+dx_outer]:
                board[top+s+dy_inner][left+s+dx_inner] = lab

    lab += 1
    if s > 1:
        for dy in [0,s]:
            for dx in [0, s]:
                lab = cover(board, lab, top+dy, left+dx, s)

    return lab