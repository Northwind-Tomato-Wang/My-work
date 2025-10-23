#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>

int main() {
    long long n;
    if (scanf("%lld", &n) != 1) return 0;
    long long R = (long long)floor(sqrt((double)n));

    int lim = (int)R;
    if (lim < 1) { printf("0\n"); return 0; }

    // allocate
    char *is_comp = (char*)calloc(lim+1, sizeof(char));
    int *primes = (int*)malloc((lim+1) * sizeof(int));
    int *mu = (int*)malloc((lim+1) * sizeof(int));
    int pc = 0;

    mu[1] = 1;
    for (int i = 2; i <= lim; ++i) mu[i] = 0;

    for (int i = 2; i <= lim; ++i) {
        if (!is_comp[i]) {
            primes[pc++] = i;
            mu[i] = -1; // prime -> mu = -1
        }
        for (int j = 0; j < pc; ++j) {
            long long v = 1LL * i * primes[j];
            if (v > lim) break;
            is_comp[v] = 1;
            if (i % primes[j] == 0) {
                mu[v] = 0; // squared prime factor -> mu = 0
                break;
            } else {
                mu[v] = -mu[i];
            }
        }
    }
    mu[1] = 1;

    // function to compute f(m) = sum_{x=1..m} floor(m/x)
    auto f_sum = [](long long m) -> long long {
        long long res = 0;
        long long l = 1;
        while (l <= m) {
            long long t = m / l;
            long long r = m / t;
            res += t * (r - l + 1);
            l = r + 1;
        }
        return res;
    };

    long long ans = 0;
    for (int u = 1; u <= lim; ++u) {
        if (mu[u] == 0) continue; // not squarefree
        long long m = R / u;
        if (m <= 0) continue;
        ans += f_sum(m);
    }

    printf("%lld\n", ans);

    free(is_comp);
    free(primes);
    free(mu);
    return 0;
}
