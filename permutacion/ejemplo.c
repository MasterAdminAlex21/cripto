#include<stdlib.h>
#include<stdio.h>

int main(){
	unsigned char a,b;
	a='j';
	b='a';
	unsigned char c=a+b;
	printf("%c -> %d\n%c -> %d\n%c -> %d\n",a,a,b,b,c,c);

	unsigned char x=2,y=8;
	unsigned char z=x & y;

	printf("%c -> %d\n",z,z);
}