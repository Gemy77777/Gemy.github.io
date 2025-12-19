#include <stdio.h>
#include <math.h>
// C program to print Fibonacci series up to n terms
// int main(){
//     int n,first = 0,second = 1, next_term;
//     printf("Enter the nth term: ");
//     scanf("%d", &n);
//     for (int i = 1; i <= n; ++i) {
//         printf("%d\n", first);
//         next_term = first + second;
//         first = second;
//         second = next_term;
//     }
// }

// int main(){
//     int grade;
//     printf("Enter your grade: ");
//     scanf("%d", &grade);
//     switch (grade)
//     {
//     case 85 ... 100:
//         printf("Excellent\n");
//         break;
//     case 70 ... 84:
//         printf("Very Good\n");
//         break;
//     case 50 ... 69:
//         printf("Good\n");
//         break;
//     case 0 ... 49:  
//         printf("Fail\n");
//         break;
//     default:
//         printf("Invalid grade\n");
//     }
// }`

// int main(){
//     float num1, num2 , result;
//     char op;
//     printf("Enter first number: ");
//     scanf("%f", &num1);
//     printf("Enter operator (+, -, *, /): ");
//     scanf(" %c", &op);
//     printf("Enter second number: ");
//     scanf("%f", &num2);
//     if (op == '+'){
//         result = num1 + num2;
//         printf("Result: %.2f\n", result);
//     }else if (op == '%'){
//         result = fmod(num1, num2);
//         printf("Result: %.2f\n", result);
//     }else if (op == '-'){
//         result = num1 - num2;
//         printf("Result: %.2f\n", result);
//     }else if (op == '*'){
//         result = num1 * num2;
//         printf("Result: %.2f\n", result);
//     }else if (op == '/'){
//         if (num2 != 0){
//             result = num1 / num2;
//             printf("Result: %.2f\n", result);
//         }else{
//             printf("Error: Division by zero\n");
//         }
//     }else{
//         printf("Invalid operator\n");
//     }
// }

#include <stdio.h>
int main() {
    int num;
    printf("Enter an integer: ");
    scanf("%d", &num);
    if (num % 2 == 0) {
        printf("%d is Even.\n", num);
    } else {
        printf("%d is Odd.\n", num);
    }
    return 0;
}