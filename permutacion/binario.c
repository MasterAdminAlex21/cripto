#include<stdio.h>
#define CHAR_BITS 8

void 
print_binint(int num)
{
    int sup = CHAR_BITS*sizeof(int);
    while(sup >= 0)
    {
        if(num & (((long int)1) << sup))
            printf("1");
        else
            printf("0");
        sup--;
    }
    printf("\n");
}


int main()
{
    int num;
    printf("introduzca un numero entero:");
    scanf("%d", &num);
    printf("Número binario\n");
    print_binint(num);
    return 0;
}