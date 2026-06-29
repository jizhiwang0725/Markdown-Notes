#include <cstdio>   // 提供 scanf 和 printf 函数
#include <cmath>    // 提供 sqrt() 函数

using namespace std;

int main() {
    double a, b, c;
    
    // 使用 scanf 读取三个 double 类型的浮点数
    // %lf 是 double 类型的占位符，注意变量前要加取地址符 &
    scanf("%lf %lf %lf", &a, &b, &c);
    
    // 计算半周长 p
    double p = (a + b + c) / 2.0;
    
    // 使用海伦公式计算面积
    double area = sqrt(p * (p - a) * (p - b) * (p - c));
    
    // 使用 printf 输出结果
    // %.1f 表示输出浮点数，并保留 1 位小数（自动四舍五入）
    printf("%.1f\n", area);
    
    return 0;
}