#include <stdio.h>
#include <stdint.h>

// 快速幂：计算 (base^exp) % mod，处理负底数
long long mod_pow(long long base, long long exp, int mod) {
    base %= mod;
    if (base < 0) base += mod;
    long long res = 1 % mod;
    long long b = base;
    while (exp > 0) {
        if (exp & 1) res = (res * b) % mod;
        b = (b * b) % mod;
        exp >>= 1;
    }
    return res;
}

int main() {
    int T;
    if (scanf("%d", &T) != 1) return 0;
    while (T--) {
        long long a, b, c, d, e, f, g;
        if (scanf("%lld %lld %lld %lld %lld %lld %lld", &a, &b, &c, &d, &e, &f, &g) != 7) return 0;

        // 三个模
        int mods[3] = {100, 3, 7};
        int ok_all = 1;

        for (int i = 0; i < 3; ++i) {
            int m = mods[i];
            long long ra = mod_pow(a, d, m);
            long long rb = mod_pow(b, e, m);
            long long rc = mod_pow(c, f, m);
            long long sum = (ra + rb) % m;
            sum = (sum + rc) % m;

            long long rg = g % m;
            if (rg < 0) rg += m;

            if (sum != rg) {
                ok_all = 0;
                break;
            }
        }

        if (ok_all) printf("Yes\n");
        else printf("No\n");
    }
    return 0;
}
