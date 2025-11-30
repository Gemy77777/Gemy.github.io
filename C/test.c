#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <math.h>

// int main(void){
//     long num1 = get_long("x: ");
//     long num2 = get_long("y: ");
//     if (num1 > num2)
//     {
//         printf("x is greater than y\n");
//     }
//     else if (num1 < num2)
//     {
//         printf("x is less than y\n");
//     }
//     else
//     {
//         printf("x is equal to y\n");
//     }
//     return 0;
// }



// int main(void){
//     long num1 = get_long("x: ");
//     if (num1%2 == 0)
//     {
//         printf("x is even\n");
//     }
//     else
//     {
//         printf("x is odd\n");
//     }
    
// }



// int main(void){
//     char name = get_char("Do you agree?: " );
//     if (name == 'y' || name == 'Y')
//     {
//         printf("Agreed\n");
//     }
//     else if (name == 'n' || name == 'N')
//     {
//         printf("Denied\n");
//     }
//     else
//     {
//         printf("Invalid input\n");
//     }
// }



// int main(void){
//     for (int i = 0; i < 3; i++)
//     {
//         printf("hello\n");
//     }   
// }



// int main(void){
//     int i = 0;
//     while (i < 3)
//     {
//         printf("hello\n");
//         i++;
//     }
// }


// int main(void){
//     for (int i = 0; i <= 10; i += 2)
//     {
//         printf("%i\n", i);
//     }
    
// }

// void sum(int x, int y){
//     printf("%i\n", x + y);
// }
// int main(void){
//     sum(5, 5);
// }


// float discount(float price, int percent){
//     return price * (100 - percent) / 100.0;
// }

// int main(void){
//     float regular = get_float("enter regular price: ");
//     int percent = get_int("enter discount percentage: ");
//     float sale = discount(regular, percent);
//     printf("sale price: %.1f\n", sale);
//     return 0;
// }


// int main(void){
//     printf("Name:\tAhmed\n");
//     printf("Age:\t20\n");
//     printf("Country:\tEgypt\n");
//     return 0;
// }


// section cs 3!!
// int main(void){
//     float length,width,area;
//     printf("Enter the length: ");
//     scanf("%f", &length);
//     printf("Enter the width: ");
//     scanf("%f", &width);
//     area = length * width;
//     printf("the area is: %f\n", area);
//     return 0;
// }

// int main(void){
//     int n,first,second;
//     first = 0;
//     second = 1;
//     printf("Enter the nth term: ");
//     scanf("%d", &n);
//     printf("%d\n", first);
//     printf("%d\n", second);
// }




// #include <stdio.h>

// // 3. Macro for Maximum Operations 
// #define MAX_OPERATIONS 4

// int main() {
//     // 2. Constant Variable 
//     const float TAX_RATE = 0.08;

//     // 4. Variable Declarations [cite: 354]
//     float num1, num2;     // [cite: 355, 356]
//     int choice;           // [cite: 358]
//     float result = 0.0;
    
//     // Flag to track if operation is valid (for error handling)
//     int valid_operation = 1; 

//     // 5. Menu Display [cite: 359]
//     printf("Calculator Menu:\n");        // [cite: 360]
//     printf("1. Addition\n");         // [cite: 361]
//     printf("2. Subtraction\n");      // [cite: 362]
//     printf("3. Multiplication\n");   // [cite: 363]
//     printf("4. Division\n");         // [cite: 364]

//     // 6. Choice Input [cite: 365]
//     printf("Choose an operation (1-%d): ", MAX_OPERATIONS);
//     scanf("%d", &choice);

//     // 7. Number Input [cite: 367]
//     printf("Enter first number: ");
//     scanf("%f", &num1);
//     printf("Enter second number: ");
//     scanf("%f", &num2);

//     // 8. Operation Execution & 9. Error Handling [cite: 368, 369]
//     // We use short-circuiting of logical AND (&&) to execute 
//     // the assignment only if the condition (choice == X) is true.

//     (choice == 1) && (result = num1 + num2);
//     (choice == 2) && (result = num1 - num2);
//     (choice == 3) && (result = num1 * num2);

//     // Handle division and check for divide-by-zero [cite: 369]
//     (choice == 4) && (num2 != 0) && (result = num1 / num2);
//     (choice == 4) && (num2 == 0) && (printf("Error: Division by zero is not allowed.\n"), valid_operation = 0);

//     // 6. Validate choice range [cite: 366]
//     (choice < 1 || choice > MAX_OPERATIONS) && (printf("Error: Invalid choice.\n"), valid_operation = 0);

//     // 10. Tax Calculation & 11. Result Display [cite: 370, 371]
//     // This block only executes if valid_operation is still 1 (true)
//     (valid_operation) && (
//         result = result * (1 + TAX_RATE),  // Apply tax [cite: 370]
//         printf("The final result (with tax) is: %.2f\n", result) // Display with 2 decimal places [cite: 371]
//     );

//     // 12. Program Exit [cite: 372]
//     return 0; 
// }



//lecture 6
// variable , const, define var (defference)
int main(void){
    float n1, n2, result;
    char operation, temp;
    printf("enter numbers and operation ");
    scanf("%f%c%c%f", &n1,&temp, &operation, &n2);
    if (operation == '+')
    {
        result = n1 + n2;
        printf("%f\n",result);
    }
    else if (operation == '-')
    {
        result = n1 - n2;
        printf("%f\n",result);
    }
    else if (operation == '%')
    {
        result = fmod(n1,n2);
        printf("%f\n",result);
    }
    else if (operation == '*')
    {
        result = n1 * n2;
        printf("%f\n",result);
    }
    else if (operation == '/')
    {
        result = n1 / n2;
        printf("%f\n",result);
    }
    else
    {
        printf("invalid input");
    }

}