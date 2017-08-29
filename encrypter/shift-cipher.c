#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define modulo 26
//encrypt method shift-cipher
//the prototypes

void data();
int gcd(int);
void cipher(int,int,char *);
int encryptchar(char,int,int);

void data(){
char arch[200];
int alfa,beta,accept=0,exist=0;
FILE *find;
while(exist==0){
printf("archive's name to encrypt: ");
scanf("%[^\n]",arch);
if((find=fopen(arch,"r"))==NULL){
  getchar();
  printf("ERROR: the file doesn't exist\n");
  strcpy(arch,"");
}else{
  fclose(find);
  //printf("%s\n",arch);
  exist=1;
}
}

//printf("%s\n",&arch);
//here starts to search the archive
while(accept!=1){
printf("set the alpha value: ");
scanf("%d",&alfa);
if(alfa>=modulo){
  alfa=alfa%modulo;
  printf("alpha value: %d\n",alfa);
}
printf("set the beta value: ");
scanf("%d",&beta);
if(beta>=modulo){
  beta=beta%modulo;
  printf("beta value: %d\n",beta);
}
accept=gcd(alfa);
if(accept!=1){
  printf("ERROR: alpha can't be that value\ntry again\n");
}
}
cipher(alfa,beta,arch);
//here calls the cipher function
printf("message encrypted :D\n");
}

int gcd(int alpha){
  //here starts the greatest common divisor's algorithm
  int a1,b1,r,q1;
  if(alpha>modulo){
    a1=alpha;
    b1=modulo;
    r=a1%b1;
    while(r>0){
      a1=b1;
      b1=r;
      r=a1%b1;
    }
  }
   else if(modulo>alpha){
    a1=modulo;
    b1=alpha;
    r=a1%b1;
    while(r>0){
      a1=b1;
      b1=r;
      r=a1%b1;
    }
  }
  return b1;
}

int encryptchar(char c,int alpha,int beta){
  int val=0,res=0;
  res=alpha*(((int)c)-97);
  if(res>=modulo){
    res=res%modulo;
  }
  res=res+beta;
  if(res>=modulo){
    res=res%modulo;
  }
  val=res+65;
  if(val<0) return 0;
  return val;
}

void cipher(int alpha, int beta, char *arc){
//here starts the encrypt function
FILE *archive,*cipher;
if((archive=fopen(arc,"r"))!=NULL){
  cipher=fopen("encrypted.txt","w");
  char car,enc;
  unsigned int encr;
  while(!feof(archive)){
    fscanf(archive,"%c",&car);
    encr=encryptchar(car,alpha,beta);
    if(encr>0){
      fprintf(cipher,"%c",encr);
    }
  }
  fclose(cipher);
  fclose(archive);
}else{
  printf("Archivo no encontrado o no existe\n");
}

}
