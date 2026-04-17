#include <stdio.h>
int main(void){
const int SIZE = 10;
int str[SIZE];
int sum_even = 0;
int sum_odd = 0;
int *ptr = str;
for (int i = 0; i < SIZE; i++){
    printf("Enter a number: ");
    scanf("%d", (ptr + i));
}
for (int i = 0; i < SIZE; i++){
    if (*(ptr + i) % 2 == 0){
        sum_even += *(ptr + i);
    } else {
        sum_odd += *(ptr + i);
    }
}
printf("Sum of even numbers: %d\n", sum_even);
printf("Sum of odd numbers: %d\n", sum_odd);
return 0;
}