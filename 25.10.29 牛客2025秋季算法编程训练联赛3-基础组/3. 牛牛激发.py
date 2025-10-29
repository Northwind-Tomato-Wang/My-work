import sys

MOD = 10**9 + 7

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        print(0)
        return
    # 首项是 n（但我们只需要保证有足够的字符）
    try:
        n = int(data[0])
    except:
        print(0)
        return
    # 之后可能在同一行或下一行给出01串，可能分成多个token，合并剩余并取前n字符
    rest = "".join(data[1:])
    s = rest[:n]
    # 保证长度 n；若不足则用 '0' 补齐（也可报错）
    if len(s) < n:
        s = s.ljust(n, '0')

    positions = []
    # indices are 1-based according to problem statement
    for i, ch in enumerate(s, start=1):
        if ch == '1':
            positions.append(i)
    k = len(positions)
    if k <= 1:
        print(0)
        return

    ans = 0
    # compute sum p_t * (2*t - k - 1)
    # t runs from 1..k
    for idx, p in enumerate(positions, start=1):
        coef = 2 * idx - k - 1
        # coef may be negative; handle modulo safely
        ans = (ans + (coef % MOD) * (p % MOD)) % MOD

    print(ans % MOD)

if __name__ == "__main__":
    main()