#include<iostream>
#include<cmath>
using namespace std;

int main() {
    // 2
    int l = (24 + 4) / 2; 
    int w = (24 - 4) / 2;
    int area = w * l;
    cout << area << endl;

    // 3
    int a = 480.0/2.4 ;
    int umi = 1.4 * a;
    cout << a << " " << umi << endl;

    // 4
    int x1 = 3, x2 = 4, l1 = 11, l2 = -1 ;
    int diff = x2 - x1; // 每人分配数量差
    int apple_diff = l1 - l2; // 亏盈总差额
    int ppl = apple_diff / diff; 
    int apple = ppl * x1 + 11;
    cout << ppl << " " << apple << endl;

    // 5
    int a_cpm = 120, umi_cpm = 80;
    int adv = 12; 
    int cpm_diff = a_cpm - umi_cpm; 

    int ans = (umi_cpm * adv) / cpm_diff; // Umi需要多长时间才能把多出来的字数追赶上
    cout << ans << endl;

    // 6
    int total = 35, legs = 94;
    int r_l = 4, c_l = 2;
    
    int all_r = 35 * 4; // 假设全部都是兔子
    int extra_legs = all_r - legs; // 多出来的腿
    int l_diff = r_l - c_l; // 每把一只兔子换成一只鸡就会少两个腿
    int c_num = extra_legs / c_l; // 所以需要这么多只鸡才能减少这么多的腿
    int r_num = total - c_num;

    cout << c_num << " " << r_num << endl;

    // 7
    double int_1 = 0.035, int_4 = 0.04;
    double a_init = 10000.0, umi_init = 10000.0;
    double umi_final = umi_init + umi_init * int_4 * 5;
    double a_final = a_init * pow((1 + int_1), 5);
    cout << umi_final << " " << a_final << endl;




    return 0;
}