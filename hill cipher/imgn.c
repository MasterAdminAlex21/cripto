#include<stdio.h>
#include<stdlib.h>

int main(){
	char nom[100];
	printf("ingrese nombre bmp: ");
	scanf("%[^\n]",nom);
	FILE *f;
	if((f=fopen(nom,"r"))!=NULL){
		FILE *i;
		char c;
		int cont=0;
		i=fopen("imagen.txt","w");
		while(!feof(f)){
			fscanf(f,"%c",&c);
			fprintf(i,"%x ",c);

			//printf("%d ",cont);
			
		}
	}
}