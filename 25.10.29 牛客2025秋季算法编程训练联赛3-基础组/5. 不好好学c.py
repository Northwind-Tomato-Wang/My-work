import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    T = next(it)
    out_lines = []
    for _ in range(T):
        try:
            n = next(it); m = next(it); p = next(it)
        except StopIteration:
            break
        size = n * m
        # 模拟全局数组的线性内存，初值为0
        mem = [0] * (size if size>0 else 0)
        ub_flag = False  # 有越界但未非法访问（即存在 x 或 y 不在正常范围，但 idx 合法）
        runtime_error = False
        for _op in range(p):
            try:
                x = next(it); y = next(it); val = next(it)
            except StopIteration:
                x = y = val = 0
            # 计算线性下标 idx = m*x + y
            idx = m * x + y
            # 检查是否非法访问
            if idx < 0 or idx >= size:
                runtime_error = True
                # 读完剩余输入项但不处理（需要把迭代器推进到下一个测试用例）
                # 我们仍需消费剩余操作输入 for this test case (already consumed p lines)
                # but since we're iterating, simply continue to read remaining ops to move iterator.
                # However we can break and skip consumption because outer loop will continue with next test case;
                # but we must advance the iterator for remaining operations in this test case.
                # To simplify, consume remaining ops here:
                # (we already read current op's three ints)
                # consume remaining operations for this test case:
                rem = (p - _op - 1) * 3
                for _r in range(rem):
                    try:
                        _ = next(it)
                    except StopIteration:
                        break
                break
            # idx in valid memory range
            # check whether this was textual array-bounds violation (UB)
            if not (0 <= x < n and 0 <= y < m):
                ub_flag = True
            # perform write
            mem[idx] = val
        # 输出 according to flags
        if runtime_error:
            out_lines.append("Runtime error")
        else:
            # print n lines each with m numbers
            # mem length may be zero if n*m == 0, but constraints n,m >=1 so safe
            for i in range(n):
                row = mem[i*m:(i+1)*m]
                out_lines.append(" ".join(str(v) for v in row))
            if ub_flag:
                out_lines.append("Undefined Behaviour")
            else:
                out_lines.append("Accepted")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()