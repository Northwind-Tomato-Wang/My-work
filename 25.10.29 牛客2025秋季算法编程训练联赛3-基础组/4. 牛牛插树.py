import sys

def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    n = data[0]
    vals = data[1:1 + n]
    # 1-based array
    arr = [None] + vals
    # 记录每个节点值所在的位置（下标）
    pos = {}
    for idx in range(1, len(arr)):
        v = arr[idx]
        if v != -1:
            pos[v] = idx
    if not pos:
        print("The size of the tree is 0")
        print("Node -1 is the root node of the tree")
        return
    size = max(pos.keys())  # 节点值从1..size连续
    root = arr[1] if len(arr) > 1 else -1

    print(f"The size of the tree is {size}")
    print(f"Node {root} is the root node of the tree")
    for i in range(1, size + 1):
        idx = pos.get(i, None)
        if idx is None:
            father = -1
            left = -1
            right = -1
        else:
            # 父节点
            pidx = idx // 2
            father = arr[pidx] if pidx >= 1 and pidx < len(arr) and arr[pidx] != -1 else -1
            # 左孩子
            lidx = idx * 2
            left = arr[lidx] if lidx < len(arr) and arr[lidx] != -1 else -1
            # 右孩子
            ridx = idx * 2 + 1
            right = arr[ridx] if ridx < len(arr) and arr[ridx] != -1 else -1
        print(f"The father of node {i} is {father}, the left child is {left}, and the right child is {right}")

if __name__ == "__main__":
    main()