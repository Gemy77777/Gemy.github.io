
#include <stdio.h>
// int main(void) {
//     int numbers[10];
//     int max, min;
//     float sum = 0, average;
//     for (int i = 0; i < 10; i++) {
//         printf("Enter number %d: ", i + 1);
//         scanf("%d", &numbers[i]);
//         sum += numbers[i];
//         if (i == 0) {
//             max = numbers[i];
//             min = numbers[i];
//         }
//         else {
//             if (numbers[i] > max) {
//                 max = numbers[i];
//             }
//             if (numbers[i] < min) {
//                 min = numbers[i];
//             }
//         }
//     }
//     average = sum / 10;
//     printf("\n============= Results =============\n");
//     printf("Numbers entered: ");
//     for (int i = 0; i < 10; i++) {
//         printf("%d ", numbers[i]);
//     }
//     printf("\n\n");
//     printf("Maximum number: %d\n", max);
//     printf("Minimum number: %d\n", min);
//     printf("Sum of numbers: %.0f\n", sum);
//     printf("Average number: %.2f\n", average);
//     return 0;
// }

//=====================================================

// #include <stdio.h>
// #include <stdbool.h>
// int main(void) {
//     int numbers[10];
//     int trend[9]; // Stores the relationship between consecutive numbers
//     printf("=== Array Pattern Analyzer ===\n\n");
//     for (int i = 0; i < 10; i++) {
//         printf("Enter number %d: ", i + 1);
//         scanf("%d", &numbers[i]);
//     }
//     printf("\nYou entered: ");
//     for (int i = 0; i < 10; i++) {
//         printf("%d ", numbers[i]);
//     }
//     printf("\n\n");
//     for (int i = 0; i < 9; i++) {
//         if (numbers[i] < numbers[i + 1]) {
//             trend[i] = 1;  // Increasing
//         }
//         else if (numbers[i] > numbers[i + 1]) {
//             trend[i] = -1; // Decreasing
//         }
//         else {
//             trend[i] = 0;  // Equal
//         }
//     }
//     int increasingCount = 0, decreasingCount = 0, equalCount = 0;
//     for (int i = 0; i < 9; i++) {
//         if (trend[i] == 1) increasingCount++;
//         else if (trend[i] == -1) decreasingCount++;
//         else equalCount++;
//     }
//     if (increasingCount == 9) {
//         printf("RESULT: The numbers in the array are increasing.\n");
//     }
//     else if (decreasingCount == 9) {
//         printf("RESULT: The numbers in the array are decreasing.\n");
//     }
//     else if (equalCount == 9) {
//         printf("RESULT: The numbers in the array are not changing.\n");
//     }
//     else {
//         int changePoint = -1;
//         for (int i = 0; i < 8; i++) {
//             if (trend[i] == 1 && trend[i + 1] == -1) {
//                 changePoint = i + 1;
//                 break;
//             }
//         }
//         if (changePoint != -1) {
//             bool validPattern = true;
//             for (int i = 0; i < changePoint; i++) {
//                 if (trend[i] == -1) {
//                     validPattern = false;
//                     break;
//                 }
//             }
//             if (validPattern) {
//                 for (int i = changePoint; i < 9; i++) {
//                     if (trend[i] == 1) {
//                         validPattern = false;
//                         break;
//                     }
//                 }
//             }
            
//             if (validPattern) {
//                 printf("RESULT: The numbers in the array are increasing and then decreasing.\n");
//                 printf("        (Peak at index %d with value %d)\n", changePoint + 1, numbers[changePoint]);
//             }
//             else {
//                 printf("RESULT: The numbers in the array have no specific pattern.\n");
//             }
//         }
//         else {
//             printf("RESULT: The numbers in the array have no specific pattern.\n");
//         }
//     }
//     return 0;
// }


int main (void){

int arr [3][4];

for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 4; j++) {
        printf("Enter value for arr[%d][%d]: ", i, j);
        scanf("%d", &arr[i][j]);
    }
}
scanf_s("%d", &arr[0][0]);
return 0;
}