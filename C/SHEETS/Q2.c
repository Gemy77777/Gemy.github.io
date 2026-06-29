#include <stdio.h>

 float area(float base, float height){
     return 0.5 * base * height;
 } 
 int main(void){
 float base , height;
 printf("Enter the base of the triangle: ");
 scanf("%f", &base);
 printf("Enter the height of the triangle: ");
 scanf("%f", &height); 
 printf("The area of the triangle is: %.2f\n", area(base, height));
 return 0;
 }


 int findGreatest(int a, int b, int c) {
     if (a>b && a>c)
     {
        return a;
     }
     else if (b>a && b>c)
     {
         return b;
     }
     else
     {
         return c;
     }
    
 }
 int main() {
     int num1, num2, num3;
     printf("Enter three integer values: ");
     scanf("%d %d %d", &num1, &num2, &num3);
     int greatest = findGreatest(num1, num2, num3);
     printf("The greatest value is: %d\n", greatest);
     return 0;
 }



 char grade(float score){
     if (score >= 90.0)
     {
         return 'A';
     }
     else if (score >= 70.0)
     {
         return 'B';
     }
     else if (score >= 50.0)
     {
         return 'C';
     }
     else
     {
         return 'F';
     }
 }
 int main(){
 float s1,s2,s3, average;
 char result;
 printf("Enter the three scores: ");
 scanf("%f %f %f", &s1, &s2, &s3);
 average = (s1+s2+s3) / 3;
 result = grade(average);
 printf("your grade is: %c\n", result);
 return 0; 
 }


 int is_even(int n){
     if (n % 2 == 0)
     {
         return 1;
     }
     else
     {
         return 0;
     }
 }
 int main(){
     int num;
     printf("Enter a number: ");
     scanf("%d", &num);
     if (is_even(num))
     {
         printf("%d is even\n", num);
     }
     else
     {
         printf("%d is odd\n", num);
     }
     return 0;
 }



 void comparazon(int a, int b){
     if (a > b)
     {
         printf("%d is greater\n", a);
     }
     else if (a < b)
     {
         printf("%d is greater\n", b);
     }
     else
     {
         printf("%d and %d are equal\n", a, b);
     }

 }
 int main(){
     int num1, num2;
     printf("Enter two integer values: ");
     scanf("%d %d", &num1, &num2);
     comparazon(num1, num2);
     return 0;
 }



 void triangleType(int a, int b, int c) {
     if (a + b + c != 180) {
         printf("Result: Invalid triangle (sum = %d°, must be 180°)\n", a + b + c);
         return     0;
     }
     printf("Result: ");
     if (a == b && b == c) {
         printf("Equilateral Triangle (all angles equal)\n");
     }
     else if (a == b || b == c || a == c) {
         printf("Isosceles Triangle (two angles equal)\n");
     }
     else {
         printf("Acute Triangle (all angles different)\n");
     }
 }
 int main() {
     int a, b, c;
     printf("Triangle Type Checker\n");
     printf("=====================\n");
     printf("Enter three angles: ");
     scanf("%d %d %d", &a, &b, &c);
     triangleType(a, b, c);
     return 0;
 }



 int reverseTriangle(int rows){
     for (int i = rows; i >= 1; i--)
     {
         for (int j = 1; j <= i; j++)
         {
             printf("*");
         }
         printf("\n");
     }
 }
 int main(){
 int rows;
 printf("Enter the number of rows: ");
 scanf("%d", &rows);
 reverseTriangle(rows);
 return 0;
 }



 #include <stdio.h>
 void Diamond(int n) {
     int i, j;
     for (i = 1; i <= n; i += 2) {
         for (j = 1; j <= i; j++) {
             printf("*");
         }
         printf("\n");
     }
     for (i = n; i >= 1; i -= 2) {
         for (j = 1; j <= i; j++) {
             printf("*");
         }
         printf("\n");
     }
 }
 int main() {
     Diamond(9);
     return 0;
 }


 int sumOfDigits(int n) {
     int sum = 0;
     while (n > 0) {
         sum += n;
         n--;       
     }
     return sum;
 }
 int main() {
     int number;
     printf("Enter an integer: ");
     scanf("%d", &number);
     int result = sumOfDigits(number);
     printf("The sum of the digits is: %d\n", result);
     return 0;
 }



