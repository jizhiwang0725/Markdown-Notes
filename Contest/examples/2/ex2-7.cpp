#include<cstdio> 

int main() {
    // 任意4个顶点 -> 唯一1个内交点
    // 这个问题可以简化为从n个顶点中任意选出4个顶点的组合数量
    int n;
    scanf ("%d", &n);
    int combinations = n * (n - 1) * (n - 2) * (n - 3); // 假设我们要选择四个顶点会有多少种组合
    int repetition = 4 * 3 * 2 * 1; // 由于选择顶点的顺序不重要，比如说ABCD和ACBD都是同一批点
    printf("%d", combinations/repetition);
    return 0;
}