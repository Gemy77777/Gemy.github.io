#include <stdio.h>
int main() {
    int a[5], x;
    int *p1, *p2;
    p1 = a;
    p2 = a+2;
    x = p2 - p1;
    printf("%d\n",x);
    return 0;
}