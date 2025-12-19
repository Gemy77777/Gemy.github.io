#include <stdio.h>
#include <math.h>

int main(void){
    float n1, n2, result;
    char operation, hold;
    printf("enter numbers and operation \n");
    scanf("%f%c%c%f", &n1,&hold, &operation, &n2);
    if (operation == '+')
    {
        result = n1 + n2;
        printf("%.1f\n",result);
    }
    else if (operation == '-')
    {
        result = n1 - n2;
        printf("%.1f\n",result);
    }
    else if (operation == '%')
    {
        result = fmod(n1,n2);
        printf("%.1f\n",result);
    }
    else if (operation == '*')
    {
        result = n1 * n2;
        printf("%.1f\n",result);
    }
    else if (operation == '^')
    {
        result = pow(n1, n2);
        printf("%.1f\n",result);
    }
    else if (operation == '/')
    {
        result = n1 / n2;
        printf("%.1f\n",result);
    }
    else
    {
        printf("invalid input\n");
    }
    return 0;
}