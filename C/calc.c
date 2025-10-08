#include <stdio.h>
#include <cs50.h>

int main(void){
    long num1 = get_long("enter the first number: ");
    long num2 = get_long("enter the second number: ");
    printf("the sum is: %li\n", num1 + num2);
}
