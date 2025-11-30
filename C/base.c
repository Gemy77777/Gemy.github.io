#include <stdio.h>
int main(void){
int a,b,res;
printf("Enter two numbers: ");
scanf("%d %d", &a, &b);
if (a > b){
    res = a - b;
    printf("The difference is: %d\n", res);
} else {
    res = b - a;
    printf("The difference is: %d\n", res);
}
return 0;
}
