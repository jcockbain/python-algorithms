def numIslands(grid):

    def bfs(mark, grid, x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        m = len(mark)
        n = len(mark[0])
        Q = []
        Q.append([x, y])
        mark[x][y] = 1
        while Q:
            temp = Q.pop(0)
            x = temp[0]
            y = temp[1]
            for i in range(4):
                newx = dx[i] + x
                newy = dy[i] + y
                if newx < 0 or newx >= m or newy >= n or newy < 0:
                    continue
                if mark[newx][newy] == 0 and grid[newx][newy] == '1':
                    # Put the new location into the queue
                    Q.append([newx, newy])
                    mark[newx][newy] = 1

    res = 0
    if len(grid) == 0:
        return res
    m = len(grid)
    n = len(grid[0])

    mark = [[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            if mark[i][j] == 0 and grid[i][j] == '1':
                bfs(mark, grid, i, j)
                res += 1
    return res
