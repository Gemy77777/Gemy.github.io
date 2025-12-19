#include <stdio.h>

int main() {
    for (int i = 1; i < 11; i++) {
        printf("%d\n", i);
    }
    return 0;
}

int main() {
    int i = 2;
    while (i <= 20) {
        printf("%d\n", i);
        i += 2;
    }
}

int main() {
    int i = 1;
    int sum = 0;
    do {
        sum += i;
        i++;
    } while (i <= 50);
    printf("Sum: %d\n", sum);
    return 0;
}

int main() {
    int i = 1;
    int n;
    int Factorial = 1;
    printf("enter your number: ");
    scanf("%d", &n);
    for (i = 1; i <= n; i++) {
        Factorial *= i;
    }
    printf("Factorial: %d\n", Factorial);
    return 0;
}

int main() {
    int n;
    int sum = 0;
    printf("enter you a number (enter 0 to stop): ");
    scanf("%d", &n);
    while (n != 0) {
        sum += n;
        printf("enter you a number (enter 0 to stop): ");
        scanf("%d", &n);
    }
    printf("Sum: %d\n", sum);
    return 0;
}

int main() {
    int average = 0;
    int count = 0;
    int result = 0;
    int n;
    do {
        printf("enter your number (enter -ve number to stop): ");
        scanf("%d", &n);
        if (n >= 0) {
            average += n;
            count++;
            result = average / count;
        }
    } while (n >= 0);
    printf("Average: %d\n", result);
    return 0;
}

int main() {
    int n;
    printf("enter your number: ");
    scanf("%d", &n);
    for (int i = 1; i <= 10; i++) {
        printf("%d x %d = %d\n", n, i, n * i);
    }
    return 0;
}

int main() {
    int i = 2;
    int j = 1;
    while (i <= 50) {
        if (i / i == 1 && i / j == i) {
            printf("%d\n", i);
            j++;
        }
        i++;
    }
    return 0;
}

#include <math.h>

int main(void) {
    int num = 2; /* start checking from 2 */
    printf("Prime numbers between 1 and %d:\n", 50);
    while (num <= 50) {
        int is_prime = 1;
        int i = 2;
        int limit = (int)sqrt((double)num);

        /* check divisors using a while loop */
        while (i <= limit) {
            if (num % i == 0) {
                is_prime = 0;
                break;
            }
            i++;
        }

        if (is_prime) {
            printf("%d\n", num);
        }
        num++;
    }
    return 0;
}

int main(void) {
    int n = 0;
    int reversed = 0;

    printf("Enter a number: ");
    scanf("%d", &n);

    int temp = n;
    if (temp < 0) {
        temp = -temp;
    }

    do {
        reversed = reversed * 10 + (temp % 10);
        temp /= 10;
    } while (temp > 0);

    if (n < 0) {
        reversed = -reversed;
    }

    printf("Reversed: %d\n", reversed);
    return 0;
}

int main() {
    int rows = 4;
    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}

int main(void) {
    int n = 0;
    int original = 0;
    int reversed = 0;
    int temp = 0;

    printf("Enter a number: ");
    scanf("%d", &n);

    original = n;
    temp = n;

    /* Handle negative numbers */
    if (temp < 0) {
        temp = -temp;
    }

    /* Use while loop to reverse the number */
    while (temp > 0) {
        reversed = reversed * 10 + (temp % 10);
        temp /= 10;
    }

    /* Check if original and reversed are equal */
    if (original == reversed) {
        printf("%d is a palindrome.\n", original);
    } else {
        printf("%d is not a palindrome.\n", original);
    }

    return 0;
}

int main() {
    printf("enter the nth term: ");
    int n;
    scanf("%d", &n);

    int first = 0;
    int second = 1;
    int next;

    for (int i = 0; i < n; i++) {
        if (i <= 1) {
            next = i;
        } else {
            next = first + second;
            first = second;
            second = next;
        }
        printf("%d\n", next);
    }
}

#include <stdio.h>

int main(void) {
    int a = 0;
    int b = 0;
    int gcd = 0;

    printf("Enter two numbers: ");
    if (scanf("%d %d", &a, &b) != 2) {
        fprintf(stderr, "Invalid input.\n");
        return 1;
    }

    /* Handle negative numbers */
    if (a < 0) {
        a = -a;
    }
    if (b < 0) {
        b = -b;
    }

    /* Use while loop to find GCD using Euclidean algorithm */
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }

    gcd = a;
    printf("GCD: %d\n", gcd);
    return 0;
}

int main(void) {
    int choice = 0;
    float n1 = 0.0f;
    float n2 = 0.0f;
    float result = 0.0f;

    do {
        printf("\nCalculator Menu:\n");
        printf("1. Addition\n");
        printf("2. Subtraction\n");
        printf("3. Multiplication\n");
        printf("4. Division\n");
        printf("0. Exit\n");
        printf("Choose operation: ");
        scanf("%d", &choice);

        if (choice == 0) {
            printf("Exiting the calculator.\n");
            break;
        }

        printf("Enter first number: ");
        scanf("%f", &n1);
        printf("Enter second number: ");
        scanf("%f", &n2);

        switch (choice) {
            case 1:
                result = n1 + n2;
                printf("Result: %.2f\n", result);
                break;
            case 2:
                result = n1 - n2;
                printf("Result: %.2f\n", result);
                break;
            case 3:
                result = n1 * n2;
                printf("Result: %.2f\n", result);
                break;
            case 4:
                if (n2 != 0.0f) {
                    result = n1 / n2;
                    printf("Result: %.2f\n", result);
                } else {
                    printf("Error: Division by zero is not allowed.\n");
                }
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }

    } while (choice != 0);

    return 0;
}


#include <stdio.h>

int main(void)
{
    int rows = 0;
    /* Ask user how many rows to print */
    printf("Enter number of rows: ");
    if (scanf("%d", &rows) != 1 || rows <= 0) {
        fprintf(stderr, "Invalid input.\n");
        return 1;
    }
    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%d", i);
        }
        printf("\n");
    }
    return 0;
}


int main() {
int i, j;
for(i = 1; i <= 4; i++) {
for(j = 1; j <= i; j++) {
printf("%d", i);
}
printf("\n");
}
return 0;
}

#include <stdlib.h>
#include <time.h>
int main() {
int guess, number, attempts = 0;
srand(time(NULL));
number = rand() % 100 + 1;
printf("Welcome to the Guessing Game!\n");
while(1) {
printf("Enter your guess (between 1 and 100): ");
scanf("%d", &guess);
attempts++;
if(guess < number)
printf("Too low. Try again.\n");
else if(guess > number)
printf("Too high. Try again.\n");
else {
printf("Congratulations! You guessed the correct number (%d) in %d attempts.\n",
number, attempts);
break;
}
}
return 0;
}

int main() {
int i;
for(i = 65; i <= 90; i++) {
printf("ASCII value: %d, Character: %c\n", i, i);
}
return 0;
}

int main() {
int n, sum = 0;
printf("Enter an integer: ");
scanf("%d", &n);
while(n != 0) {
sum += n % 10;
n /= 10;
}
printf("The sum of digits is: %d\n", sum);
return 0;
}

int main() {
int i, j;
for(i = 0; i < 4; i++) {
for(j = 0; j < 5; j++) {
printf("*");
}
printf("\n");
}
return 0;
}

int main() {
int i, j;
for(i = 1; i <= 5; i++) {
for(j = 1; j <= 5; j++) {
printf("%3d", i * j);
}
printf("\n");
}
return 0;
}

int main() {
int i;
for(i = 1; i <= 10; i++) {
if(i % 2 == 0)
continue;
printf("%d ", i);
}
return 0;
}


int main() {
int choice;
float a, b;
while(1) {
printf("Calculator Menu:\n");
printf("1. Add\n");
printf("2. Subtract\n");
printf("3. Multiply\n");
printf("4. Divide\n");
printf("0. Exit\n");
printf("Enter your choice: ");
scanf("%d", &choice);
switch(choice) {
case 1:
printf("Enter two numbers: ");
scanf("%f %f", &a, &b);
printf("Result: %.2f\n", a + b);
break;
case 2:
printf("Enter two numbers: ");scanf("%f %f", &a, &b);
printf("Result: %.2f\n", a - b);
break;
case 3:
printf("Enter two numbers: ");
scanf("%f %f", &a, &b);
printf("Result: %.2f\n", a * b);
break;
case 4:
printf("Enter two numbers: ");
scanf("%f %f", &a, &b);
if(b == 0)
printf("Error: Division by zero is not allowed.\n");
else
printf("Result: %.2f\n", a / b);
break;
case 0:
printf("Exiting the calculator. Goodbye!\n");
return 0;
default:
printf("Invalid choice. Please enter a number between 0 and 4.\n");
}
}
}