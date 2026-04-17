#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string.h>


int main(void){
int arr[10] = {};
int size = sizeof(arr) / sizeof(arr[0]);
int evenCount = 0;
int oddCount = 0;
int *ptr = arr;
for (int i = 0; i < size; i++) {
    printf("enter number %d: ", i + 1);
    scanf("%d", *(ptr + i));
}
for (int i = 0; i < size; i++) {
        if (*(ptr + i) % 2 ==0) {
            evenCount++;
        } else {
            oddCount++;
        }
    }

printf("even numbers: %d\n", evenCount);
printf("odd numbers: %d\n", oddCount);
return 0;
}