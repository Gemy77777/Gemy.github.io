#include <stdio.h>
//Q4: 
// program 1
int main() {
    printf("Hello, World!\n");
    return 0;
}
// program 2
#include <stdio.h>
int main() {
    float num1, num2, sum;
    printf("Enter first number: ");
    scanf("%f", &num1);
    printf("Enter second number: ");
    scanf("%f", &num2);
    sum = num1 + num2;
    printf("The sum is: %.2f\n", sum);
    return 0;
}

// program 3
#include <stdio.h>

int main() {
    float length, width, area;
    printf("Enter the length of the rectangle: ");
    scanf("%f", &length);
    printf("Enter the width of the rectangle: ");
    scanf("%f", &width);
    area = length * width;
    printf("The area of the rectangle is: %.2f\n", area);
    return 0;
}
// program 4
#include <stdio.h>

int main() {
    float celsius, fahrenheit;
    printf("Enter temperature in Celsius: ");
    scanf("%f", &celsius);
    fahrenheit = (celsius * 9.0 / 5.0) + 32;
    printf("%.2f Celsius is equal to %.2f Fahrenheit\n", celsius, fahrenheit);
    return 0;
}
// program 5

#include <stdio.h>
int main(){
    int num1, num2, temp;
    printf("Enter first number: ");
    scanf("%d", &num1);
    printf("Enter second number: ");
    scanf("%d", &num2);
    temp = num1;
    num1 = num2;
    num2 = temp;
    printf("After swapping: num1 = %d, num2 = %d\n", num1, num2);
    return 0;
}

// program 6

#include <stdio.h>
int main(){
    int num1, num2;
    printf("Enter first number: ");
    scanf("%d", &num1);
    printf("Enter second number: ");
    scanf("%d", &num2);
    num1 = num2;
    num2 = num1;
    printf("After swapping: num1 = %d, num2 = %d\n", num1, num2);
    return 0;
}
//program7
#include <stdio.h>

int main() {
    int a, b, c;
    int max;
    printf("Enter three numbers: ");
    scanf("%d %d %d", &a, &b, &c);
    int max_ab = (a > b) * a + (b >= a) * b;
    max = (max_ab > c) * max_ab + (c >= max_ab) * c;
    printf("The maximum number is: %d\n", max);
    return 0;
}