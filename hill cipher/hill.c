#include <stdio.h>
#include <stdlib.h>
#include "pixel.h"
#define z 256

unsigned int key[3][3]={{1,2,3},{4,5,6},{11,9,8}};
unsigned int invkey[3][3]={{138,111,55},{250,27,14},{41,201,249}};//add the inverted matrix

pixel ehill(pixel);
void encrypt(char *);
void decrypt(char *);
pixel dhill(pixel);
void data();


pixel ehill(pixel img){
	pixel ciph=(pixel)malloc(sizeof(pix));
	for(int i=0;i<4;i++)
	ciph->rgb[i]=0;
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			ciph->rgb[i]+=(img->rgb[j]*(key[j][i]));
		}
	}
	for(int i=0;i<3;i++)
		ciph->rgb[i]=ciph->rgb[i]%z;
	ciph->rgb[3]=img->rgb[3];
	return ciph;
}

void encrypt(char *dir){
 FILE *img;
 if((img=fopen(dir,"r"))!=NULL){
 	FILE *enc;
 	enc=fopen("encrypting.bmp","w");
 	pixel encr=(pixel)malloc(sizeof(pix));
 	int cont=0;
 	unsigned int c;
 	unsigned char aux;
 	for(int k=0;k<54;k++){
 		fscanf(img,"%c",&aux);
 		fprintf(enc, "%c",aux );
 	}

 	while(!feof(img)){
 		if(cont<4){
 			fscanf(img,"%c",&aux);
  			//printf("%d  %2x  %2x //",cont,aux,c);
  			/*if((int)aux==-1){
  				encr->rgb[cont]=255;
  			}else*/
   		encr->rgb[cont]=(int) aux;
   		cont+=1;
   	}
 	  	if(cont==4){
 	  		//printf("%d %d %d ->",encr->rgb[0],encr->rgb[1],encr->rgb[2]);
 		  	encr=ehill(encr);
 		  	//printf("%d %d %d \n",encr->rgb[0],encr->rgb[1],encr->rgb[2]);
 		  	for(int i=0;i<4;i++)
 			  fprintf(enc, "%c", (char)encr->rgb[i] );
 			  for(int i=0;i<4;i++)
 			  	 encr->rgb[i]=0;
 			  cont=0;
 		  }
 		  //printf("%x %x %x ->",encr->rgb[0],encr->rgb[1],encr->rgb[2]);

 		 }
 	}
 }


 void decrypt(char *dir){
 	FILE *imge;
 	if((imge=fopen(dir,"r"))!=NULL){
 		FILE *decr;
 		decr=fopen("decrypted.bmp","w");
 		pixel dec=(pixel)malloc(sizeof(pix));
 		char c;
 		int cont=0;
 		for(int k=0;k<54;k++){
 			fscanf(imge,"%c",&c);
 			fprintf(decr, "%c",c );
 		}

 		while(!feof(imge)){
 			if(cont<4){
 				if(cont<4)
 				fscanf(imge,"%c",&c);
 				dec->rgb[cont]=(int)c;
 				cont+=1;
 			}
 			if(cont==4){
 				dec=dhill(dec);
 				for(int i=0;i<4;i++)
 					fprintf(decr,"%c",(char)dec->rgb[i]);
 				for(int i=0;i<3;i++)
 					dec->rgb[i]=0;
 				cont=0;
 			}
 			}
 		}
 	}
 

pixel dhill(pixel imgd){
	pixel unciph=(pixel)malloc(sizeof(pix));
	for(int i=0;i<4;i++)
	unciph->rgb[i]=0;
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			unciph->rgb[i]+=(imgd->rgb[j]*(invkey[j][i]));
		}
	}
	for(int i=0;i<3;i++)
		unciph->rgb[i]=unciph->rgb[i]%z;
	unciph->rgb[3]=imgd->rgb[3];
	return unciph;
}

void data(){
	char dir[200],ans;
	printf("write the image route: ");
	scanf("%[^\n]",dir);
	printf("what would you wish to do? (e=encript/d=decript) ");
 getchar();
	scanf("%c",&ans);
	if(ans=='e'){
		//encrypt
		encrypt(dir);
	}else if(ans=='d'){
		//decrypt
		decrypt(dir);
	}else{
		printf("value error... try again\n");
	}
}