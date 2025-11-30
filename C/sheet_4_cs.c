#include <stdio.h>

// Question 2.1: Even or Odd (using an if statement)
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
/*
Sample Output (Input: 14):
Enter an integer: 14
14 is Even.
*/


// Question 2.2: Even or Odd (using a conditional/ternary operator)
int main() {
    int num;
    printf("Enter an integer: ");
    scanf("%d", &num);
    (num % 2 == 0) ? printf("%d is Even.\n", num) : printf("%d is Odd.\n", num);
    return 0;
}
/*
Sample Output (Input: 7):
Enter an integer: 7
7 is Odd.
*/


// Question 2.3: Leap Year Checker (using an if statement)
int main() {
    int year;
    printf("Enter a year: ");
    scanf("%d", &year);
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        printf("%d is a Leap Year.\n", year);
    } else {
        printf("%d is NOT a Leap Year.\n", year);
    }
    return 0;
}
/*
Sample Output (Input: 2023):
Enter a year: 2023
2023 is NOT a Leap Year.
*/


// Question 2.4: Leap Year Checker (using a conditional/ternary operator)
int main() {
    int year;
    printf("Enter a year: ");
    scanf("%d", &year);
    ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) ? printf("%d is a Leap Year.\n", year) : printf("%d is NOT a Leap Year.\n", year);
    return 0;
}
/*
Sample Output (Input: 2024):
Enter a year: 2024
2024 is a Leap Year.
*/


// Question 2.5: Find the Maximum Number (using if–else statements)
int main() {
    int n1, n2, n3, max;
    printf("Enter three numbers: ");
    scanf("%d %d %d", &n1, &n2, &n3);
    if (n1 >= n2 && n1 >= n3) {
        max = n1;
    } else if (n2 >= n1 && n2 >= n3) {
        max = n2;
    } else {
        max = n3;
    }
    printf("The maximum number is: %d\n", max);
    return 0;
}
/*
Sample Output (Input: 10 50 30):
Enter three numbers: 10 50 30
The maximum number is: 50
*/


// Question 2.6: Find the Maximum Number (using a conditional/ternary operator)
int main() {
    int n1, n2, n3, max;
    printf("Enter three numbers: ");
    scanf("%d %d %d", &n1, &n2, &n3);
    max = (n1 > n2) ? ((n1 > n3) ? n1 : n3) : ((n2 > n3) ? n2 : n3);
    printf("The maximum number is: %d\n", max);
    return 0;
}
/*
Sample Output (Input: 150 20 100):
Enter three numbers: 150 20 100
The maximum number is: 150
*/


// Question 2.7: Simple Calculator (using if–else statements)
int main() {
    int n1, n2;
    char op;
    printf("Enter operator (+, -, *, %%, /): ");
    scanf(" %c", &op);
    printf("Enter two integers: ");
    scanf("%d %d", &n1, &n2);
    if (op == '+') {
        printf("Result: %d\n", n1 + n2);
    } else if (op == '-') {
        printf("Result: %d\n", n1 - n2);
    } else if (op == '*') {
        printf("Result: %d\n", n1 * n2);
    } else if (op == '%') {
        if (n2 != 0)
            printf("Result: %d\n", n1 % n2);
        else
            printf("Error: Modulo by zero.\n");
    } else if (op == '/') {
        if (n2 != 0)
            printf("Result: %.2f\n", (float)n1 / n2);
        else
            printf("Error: Division by zero.\n");
    } else {
        printf("Invalid operator.\n");
    }
    return 0;
}
/*
Sample Output (Input: * and 12, 5):
Enter operator (+, -, *, %%, /): *
Enter two integers: 12 5
Result: 60
*/


// Question 2.8: Simple Calculator (using a switch–case statement)
int main() {
    int n1, n2;
    char op;
    printf("Enter operator (+, -, *, %%, /): ");
    scanf(" %c", &op);
    printf("Enter two integers: ");
    scanf("%d %d", &n1, &n2);
    switch (op) {
        case '+':
            printf("Result: %d\n", n1 + n2);
            break;
        case '-':
            printf("Result: %d\n", n1 - n2);
            break;
        case '*':
            printf("Result: %d\n", n1 * n2);
            break;
        case '%':
            if (n2 != 0)
                printf("Result: %d\n", n1 % n2);
            else
                printf("Error: Modulo by zero.\n");
            break;
        case '/':
            if (n2 != 0)
                printf("Result: %.2f\n", (float)n1 / n2);
            else
                printf("Error: Division by zero.\n");
            break;
        default:
            printf("Invalid operator.\n");
    }
    return 0;
}
/*
Sample Output (Input: / and 10, 4):
Enter operator (+, -, *, %%, /): /
Enter two integers: 10 4
Result: 2.50
*/


// Question 2.9: Determine the Letter Grade (using a switch–case statement)
int main() {
    int mark;
    printf("Enter your mark (0-100): ");
    scanf("%d", &mark);
    switch (mark) {
        case 85 ... 100:
            printf("Grade: Excellent\n");
            break;
        case 75 ... 84:
            printf("Grade: Very Good\n");
            break;
        case 65 ... 74:
            printf("Grade: Good\n");
            break;
        case 50 ... 64:
            printf("Grade: Pass\n");
            break;
        case 0 ... 49:
            printf("Grade: Fail\n");
            break;
        default:
            printf("Invalid mark. Please enter a value between 0 and 100.\n");
    }
    return 0;
}
/*
Sample Output (Input: 78):
Enter your mark (0-100): 78
Grade: Very Good
*/