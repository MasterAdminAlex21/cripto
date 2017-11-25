//programa que une el digesto y el mensaje
#include<stdio.h>
#include<stdlib.h>

int main(int argc,char *argv[]){

	FILE *msg;
	if((msg=fopen(argv[1],"r"))!=NULL){
		FILE *dig;
		dig=fopen("message.txt","w");
		char c;
		while(!feof(msg)){
			fscanf(msg,"%c",&c);
			fprintf(dig, "%c",c);
		}
		fprintf(dig, "-> ");
		fprintf(dig, "%s",argv[2] );
		fclose(dig);
		fclose(msg);
	}
	
}