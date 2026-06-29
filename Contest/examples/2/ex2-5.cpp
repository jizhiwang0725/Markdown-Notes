#include<cstdio>  

int main() {
    int a, b;
    scanf("%d%d", &a, &b);
    int total = a*10+b;
    int price = 1 * 10 + 9;
    int amount = int(total/price); 
    printf("%d", amount);
    return 0;

}