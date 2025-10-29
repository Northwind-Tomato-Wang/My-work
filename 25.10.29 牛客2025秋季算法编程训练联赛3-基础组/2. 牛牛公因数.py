import sys
from collections import defaultdict

def count_k_composite_factors_up_to(n: int):
    if n < 1:
        return {}
    spf = [0] * (n + 1)        # 最小素因子
    primes = []
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            v = i * p
            if v > n:
                break
            spf[v] = p
            if p == spf[i]:
                break

    tot_div = [0] * (n + 1)    # 因子个数 d(x)
    cnt_pow = [0] * (n + 1)    # 当前最小素因子的幂次
    omega = [0] * (n + 1)      # 不同素因子个数
    tot_div[1] = 1
    cnt_pow[1] = 0
    omega[1] = 0

    for x in range(2, n + 1):
        p = spf[x]
        m = x // p
        if spf[m] == p:
            cnt_pow[x] = cnt_pow[m] + 1
            tot_div[x] = tot_div[m] // (cnt_pow[m] + 1) * (cnt_pow[x] + 1)
            omega[x] = omega[m]
        else:
            cnt_pow[x] = 1
            tot_div[x] = tot_div[m] * 2
            omega[x] = omega[m] + 1

    freq = defaultdict(int)
    # 包含 1
    for x in range(1, n + 1):
        comp = tot_div[x] - 1 - omega[x]
        freq[comp] += 1
    return freq

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    try:
        n = int(next(it))
        p = int(next(it))
    except StopIteration:
        return
    ks = []
    for _ in range(p):
        try:
            ks.append(int(next(it)))
        except StopIteration:
            ks.append(0)
    freq = count_k_composite_factors_up_to(n)
    out_lines = []
    for k in ks:
        out_lines.append(str(freq.get(k, 0)))
    sys.stdout.write("\n".join(out_lines) + "\n")

if __name__ == "__main__":
    main()