#include <stdio.h>

#define MAX_OPERATIONS 4

int main(void) {
    float num1, num2;
    int choice;
    const float TAX_RATE = 0.08;
    float result = 0.0;
    int valid_operation = 1; 

    printf("Enter first number (float): ");
    scanf("%f", &num1);
    printf("Enter second number (float): ");
    scanf("%f", &num2);
    
    printf("Calculator Menu:\n");
    printf("1. Addition\n");
    printf("2. Subtraction\n");
    printf("3. Multiplication\n");
    printf("4. Division\n");

    printf("Choose operation in range between 1 and %d: ", MAX_OPERATIONS);
    scanf(" %d", &choice);

    (choice == 1) && (result = num1 + num2);
    (choice == 2) && (result = num1 - num2);
    (choice == 3) && (result = num1 * num2);

    (choice == 4) && (num2 != 0) && (result = num1 / num2);
    (choice == 4) && (num2 == 0) && (printf("Error: Division by zero is not allowed.\n"), valid_operation = 0);

    (choice < 1 || choice > MAX_OPERATIONS) && (printf("Error: Invalid choice.\n"), valid_operation = 0);

    (valid_operation) && (
        result = result * (1 + TAX_RATE), 
        printf("The final result (with tax) is: %.2f\n", result)
    );

    return 0;
}