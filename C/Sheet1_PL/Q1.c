#include <stdio.h>  
int main(){
char operator;
float n1, n2, result;
while (1)
{
printf("Enter the first number: ");
scanf("%f", &n1);
printf("Enter the operator (+, -, *, /): ");
scanf(" %c", &operator);
printf("Enter the second number: ");
scanf("%f", &n2);
if (operator == '+') {
    result = n1 + n2;
} else if (operator == '-') {
    result = n1 - n2;
} else if (operator == '*') {
    result = n1 * n2;
} else if (operator == '/') {
    if (n2 != 0) {
        result = n1 / n2;
    } else {
        printf("Error: Division by zero is not allowed.\n");
        return 1;
    }
} else {
    printf("Error: Invalid operator.\n");
    return 1;
}
printf("Result: %.2f\n", result);
printf("Do you want to perform another calculation? (y/n): ");
char choice;
scanf(" %c", &choice);
if (choice != 'y' && choice != 'Y') {
    printf("Exiting the calculator. Goodbye!\n");
    break;
}
}
return 0;
}
