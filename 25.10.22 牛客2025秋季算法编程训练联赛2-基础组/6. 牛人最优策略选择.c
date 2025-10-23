#include <stdio.h>
#include <stdlib.h>

typedef struct {
    long long a, b;
    int id;
} Item;

int cmp(const void *x, const void *y) {
    const Item *i = (const Item*)x;
    const Item *j = (const Item*)y;
    long long v1 = i->a + i->b;
    long long v2 = j->a + j->b;
    if (v1 != v2) return v2 - v1; // 按a+b降序
    return i->id - j->id;         // 编号小的优先
}

int main() {
    int n;
    scanf("%d", &n);

    Item *arr = malloc(sizeof(Item) * n);
    for (int i = 0; i < n; i++) scanf("%lld", &arr[i].a);
    for (int i = 0; i < n; i++) {
        scanf("%lld", &arr[i].b);
        arr[i].id = i + 1;
    }

    qsort(arr, n, sizeof(Item), cmp);

    // 牛牛拿偶数位（先手）
    for (int i = 0; i < n; i += 2) {
        printf("%d", arr[i].id);
        if (i + 2 < n) printf(" "); // 控制空格
    }
    printf("\n");

    // 牛可乐拿奇数位（后手）
    for (int i = 1; i < n; i += 2) {
        printf("%d", arr[i].id);
        if (i + 2 < n) printf(" ");
    }
    printf("\n");

    free(arr);
    return 0;
}
