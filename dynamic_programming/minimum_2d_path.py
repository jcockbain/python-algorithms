def minimum_2d_path(grid):
    if grid == []:
        return 0
    h, w = len(grid) - 1, len(grid[0]) - 1
    dp = [[None for r in range(w + 1)] for c in range(h + 1)]
    dp[h][w] = grid[h][w]
    for r in range(h, -1, -1):
        for c in range(w, -1, -1):
            if r == h and c == w:
                continue
            elif r == h:
                dp[r][c] = dp[r][c+1] + grid[r][c]
            elif c == w:
                dp[r][c] = dp[r+1][c] + grid[r][c]
            else:
                dp[r][c] = min(dp[r + 1][c], dp[r][c + 1]) + grid[r][c]
    return dp[0][0]
