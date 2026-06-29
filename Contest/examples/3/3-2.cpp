#include<iostream> 
using namespace std; 

int main() {
    int x; bool p1, p2;
    cin >> x;
    p1 = x%2 == 0;
    p2 = 4 < x && x <= 12;
    cout << (p1 && p2) << ' '; // 两个性质同时成立
    cout << (p1 || p2) << ' '; // 两个性质至少有一个成立
    cout << (p1 ^ p2) << ' '; // 两个性质正好有一个成立
    cout << (!p1 && !p2) << ' '; // 两个性质同时不成立 !(p1 || p2)
    return 0;
}