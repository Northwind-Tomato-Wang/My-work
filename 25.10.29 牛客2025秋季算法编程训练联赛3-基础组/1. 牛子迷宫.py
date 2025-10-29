import sys

MOD = 10**9 + 7

def main():
    data_lines = sys.stdin.read().splitlines()
    if not data_lines:
        return
    # 找到第一行非空并解析 n, m （注意题目顺序为 n m）
    idx = 0
    while idx < len(data_lines) and data_lines[idx].strip() == "":
        idx += 1
    if idx >= len(data_lines):
        return
    first = data_lines[idx].strip().split()
    if len(first) < 2:
        return
    n = int(first[0])   # 行数
    m = int(first[1])   # 列数
    idx += 1

    grid = []
    # 读取接下来的 n 个有效行作为网格行
    while len(grid) < n and idx < len(data_lines):
        line = data_lines[idx]
        idx += 1
        if line.strip() == "":
            continue
        # 去掉行内空格（以兼容输入中间有空格的情况）
        row = ''.join(line.split())
        # 如果长度不足 m，则用 'B' 补齐（也可以改为报错）
        if len(row) < m:
            row = row.ljust(m, 'B')
        else:
            row = row[:m]
        grid.append(row)

    # 若输入行不足，用全 'B' 补齐剩余行（一般不会发生）
    while len(grid) < n:
        grid.append('B' * m)

    # dp[r][c] 到达 (r,c) 的路径数（取模）
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1 % MOD

    for r in range(n):
        for c in range(m):
            ways = dp[r][c]
            if ways == 0:
                continue
            ch = grid[r][c]
            # 向右
            if (ch == 'R' or ch == 'B') and c + 1 < m:
                dp[r][c + 1] = (dp[r][c + 1] + ways) % MOD
            # 向下
            if (ch == 'D' or ch == 'B') and r + 1 < n:
                dp[r + 1][c] = (dp[r + 1][c] + ways) % MOD

    print(dp[n - 1][m - 1] % MOD)

if __name__ == "__main__":
    main()