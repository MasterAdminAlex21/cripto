#include<stdio.h>
#include<stdlib.h>
#include<math.h>


int perm[4][8]={
{8,7,22,13,14,15,26,1},
{9,23,6,21,31,16,2,19},
{10,12,24,5,20,3,17,28},
{11,30,25,0,4,19,18,27}
};

int perm_1[4][8]={
{6,13,20,27,18,9,0,28},
{2,3,4,24,31,23,15,7},
{14,5,12,19,26,25,17,10},
{11,30,8,16,24,2,29,21}
};

void permu(unsigned char[]);
void desperm(unsigned char[]);	

void data(){
unsigned char pal[4];
	printf("ingrese palabra: ");
	scanf("%s",pal);
permu(pal);

}


void permu(unsigned char *s){
 printf("valor hex: %2x %2x %2x %2x \n",s[0],s[1],s[2],s[3]);
int pos;
unsigned char anding[8]={128,64,32,16,8,4,2,1};
unsigned char car[4]={0,0,0,0};
 for(int i=0;i<4;i++){//for fila
 	for(int j=0;j<8;j++){//for columna
 		pos=perm[i][j];
 		if((s[pos/8] & anding[pos%8])!=0){
 			car[i]+=pow(2,(7-j));
 		}
 	}
 }
 printf("permutacion(p):\n%c %c %c %c \nvalor hex: %2x %2x %2x %2x \n",car[0],car[1],car[2],car[3],car[0],car[1],car[2],car[3]);

 desperm(car);
}


void desperm(unsigned char s[]){
int pos;
unsigned char anding[8]={1,2,4,8,16,32,64,128};
unsigned char car[4]={0,0,0,0};

for(int i=0;i<4;i++){
	for(int j=0;j<8;j++){
		pos=perm_1[i][j];
		if((s[pos/8] & anding[pos%8])!=0){
			car[i]+=pow(2,(j));
		}
	}
}
printf("recomposicion(p^-1):\n%c %c %c %c\nvalor hex: %2x %2x %2x %2x\n", car[0],car[1],car[2],car[3],car[0],car[1],car[2],car[3]);

}