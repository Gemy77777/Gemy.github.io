#include <stdio.h>
int global_sum;
float global_average;
void calculateSumAndAverage(int a, int b) {
    global_sum = a + b;
    global_average = (a + b) / 2.0;
}
int main() {
    int num1, num2;
    printf("Enter two integers: ");
    scanf("%d %d", &num1, &num2);
    calculateSumAndAverage(num1, num2);
    printf("The Sum Of %d and %d: %d\n", num1, num2, global_sum);
    printf("The Average Of %d and %d: %.1f\n", num1, num2, global_average);
    return 0;
}