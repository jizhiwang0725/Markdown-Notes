#include<cstdio>

int main() {
    int a, b, c, d;
    int total_mins;
    scanf("%d%d%d%d", &a, &b, &c, &d);
    total_mins = (c * 60 + d) - (a * 60 + b);
    
    printf("%d %d", total_mins/60, total_mins%60);

    return 0;
}