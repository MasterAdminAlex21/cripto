#include<stdio.h>
#include<stdlib.h>

int main(int argc,char *argv[]){
//	printf("%s\n",argv[1]);
	FILE *arc;
	if((arc=fopen(argv[1],"r"))!=0){
	 FILE *data,*cabecera;
	 data=fopen(argv[2],"w");
	 cabecera=fopen("cab.txt","r");
	 unsigned char car;
	 for(int i=0;i<54;i++){
	 	fscanf(cabecera,"%c",&car);
	 	fprintf(data,"%c",car);
	 }//fin lectura de cabecera
	 fclose(cabecera);
	 while(!feof(arc)){
	 	fscanf(arc,"%c",&car);
	 	 fprintf(data,"%c", car);
	 }
	 fclose(arc);
	 fclose(data);
	}
	return 0;
}