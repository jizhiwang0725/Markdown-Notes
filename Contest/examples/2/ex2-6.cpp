#include<cstdio>
#include<cmath>

int main() {
    int m, t, s;
    scanf("%d%d%d", m, t, s);
    int ate = (s / t);
    int left = ((m - ate) + abs(m - ate)) / 2;
    printf("%d", left);
    return 0;
}