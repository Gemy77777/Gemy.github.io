#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void printArray(int *arr, int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}
void Bubblesort(int *arr, int n) {
    for (int i = 0; i < n; i++) {
    bool swapped = false;
    for (int j = 0; j < n-i-1; j++) {
        if (arr[j] > arr[j+1]) {
            int temp = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = temp;
            swapped = true;
        }
    }
    if (!swapped) {
        break;
    }
}
}
int main(){
int arr[] = {1,2,5,1};
int n = sizeof(arr) / sizeof(arr[0]);
printArray(arr, n);
Bubblesort(arr, n);
printArray(arr, n);
return 0;
}