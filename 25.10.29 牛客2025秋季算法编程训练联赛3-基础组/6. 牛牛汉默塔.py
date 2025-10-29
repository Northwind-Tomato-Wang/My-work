import sys
from functools import lru_cache

pegs = ('A', 'B', 'C')
pairs_order = [('A','B'), ('A','C'), ('B','A'), ('B','C'), ('C','A'), ('C','B')]

@lru_cache(maxsize=None)
def counts(n, src, dst):
    """返回一个元组，按 pairs_order 顺序给出把 n 个盘从 src 移到 dst 时
    每种方向的移动次数（A->B, A->C, B->A, B->C, C->A, C->B）。"""
    # use tuple for immutability
    if n == 0:
        return (0,0,0,0,0,0)
    if n == 1:
        # one move src->dst
        cnt = [0]*6
        try:
            idx = pairs_order.index((src, dst))
            cnt[idx] = 1
        except ValueError:
            pass
        return tuple(cnt)
    # find aux peg
    aux = next(p for p in pegs if p != src and p != dst)
    left = counts(n-1, src, aux)
    right = counts(n-1, aux, dst)
    # combine left + one src->dst + right
    res = [0]*6
    for i in range(6):
        res[i] = left[i] + right[i]
    # add the single move src->dst
    try:
        idx = pairs_order.index((src, dst))
        res[idx] += 1
    except ValueError:
        pass
    return tuple(res)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    # We want moves when moving n disks from A to C (standard)
    res = counts(n, 'A', 'C')
    # Print in required format
    names = ["A->B","A->C","B->A","B->C","C->A","C->B"]
    for name, val in zip(names, res):
        print(f"{name}:{val}")
    total = (1<<n) - 1  # 2^n - 1
    print(f"SUM:{total}")

if __name__ == "__main__":
    main()