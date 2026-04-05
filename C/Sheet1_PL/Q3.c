#include <stdio.h>

int numbers[10];

int Max(){
    int max = numbers[0];
    for(int i = 1; i < 10; i++){
        if(numbers[i] > max){
            max = numbers[i];
        }
    }
    return max;
}
int Min(){
    int min = numbers[0];
    for(int i = 1; i < 10; i++){
        if(numbers[i] < min){
            min = numbers[i];
        }
    }
    return min;
}
int Differancee (){
    int maxnum = Max();
    int minnum = Min();
    return maxnum - minnum;
}

int main(void){
for(int i = 0; i < 10; i++){
    printf("Enter number %d: ", i + 1);
    scanf("%d", &numbers[i]);
}
printf("The maximum number is %d\n", Max());
printf("The minimum number is %d\n", Min());
printf("The difference is %d\n", Differancee());
return 0;
}
