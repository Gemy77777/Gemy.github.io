#include <stdio.h>
int main(void){ 
int a,b,c,I=1, rows;
printf("Enter the number of rows\t");
scanf("%d",&rows);
for (a=1; a<=rows; a++){
    for (b = rows; b>=a; b--){
        printf(" ");
    }
    for (c=1; c<=I; c++){
        printf("*");
    }
    I+=2;
    printf("\n");
    
}
return 0;
}
