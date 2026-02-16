#include <stdio.h>
int main(void){
char i = 'A';
char j = 'a';
printf("The uppercase letters are: \n");
for (; i <= 'Z'; i++){
    printf("%c ", i);
}
printf("\n");
printf("The lowercase letters are: \n");
for (; j <= 'z'; j++){
    printf("%c ", j);
}
return 0;
}
