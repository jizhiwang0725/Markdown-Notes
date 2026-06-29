#include<iostream>
using namespace std;

int main() {
    int n1 = 8, t1 = 30, n2 = 10, t2 = 6; // 题目给出来的数量
    int t3 = 10 ; // 题目要求的时间
    double inc_rate = (1.0 * n1 * t1 - n2 * t2) / (t1 - t2); // 增长速度
    double init_num = n2 * t2 - inc_rate * t2; // 起始数量
    double ans = (init_num + t3 * inc_rate) / t3; // 答案
    return 0;
}