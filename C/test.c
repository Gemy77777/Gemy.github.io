#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
int main(){
FILE *p;
char ch;
char Filename[100];
printf("Enter the name of the file to read: ");
gets(Filename);
p = fopen(Filename, "r");
if (p == NULL) {
    printf("Error opening file.\n");
    return 1;
}
while (1){
ch = fgetc(p);
if (ch == EOF){
    break;
}
printf("%c", ch);
}
fclose(p);
return 0;
}
