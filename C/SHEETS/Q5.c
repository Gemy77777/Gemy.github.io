#include <stdio.h>

int mystery(int a, int b){
    if (b == 1)
        return a;
    else
        return a + mystery(a, b - 1);
}
int main(void){
return 0;
}