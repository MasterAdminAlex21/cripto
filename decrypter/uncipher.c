#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define mod 26

int inverterAditive(int);
int inverterMultiplier(int);
int charclear(int,int,char);
void decrypt(char *,int,int);
int gcd(int);
void bruteforce(char *);
int bf(char,int,int);

void data(){
  char arch[200],res;
  int alfa,beta,exis=0;
  while(exis==0){
    printf("archive's name to decrypt:  ");
    scanf("%[^\n]",arch);
    //existence validation
    FILE *ex;
    if((ex=fopen(arch,"r"))==NULL){
      printf("ERROR: don't exist any archive\n");
      getchar();
      strcpy(arch,"");
    }else{
      fclose(ex);
      exis=1;
    }
  }
  getchar();
  printf("do you known the cipher's formula? (y/n) ");
  scanf("%c",&res);
  getchar();
  if(res=='y'){
    printf("alpha value: ");
    scanf("%d",&alfa);
    printf("beta value: ");
    scanf("%d",&beta);
    //decrypt function
    decrypt(arch,alfa,beta);
  }else if(res=='n'){
    printf("Se probara por fuerza bruta (no a lo bruto :v)\n");
    //brute force function
    bruteforce(arch);
  }else{
    printf("ERROR: invalid option");
  }
}

int inverterAditive(int beta){
  int i;
  for(i=1;i<mod;i++){
    if((beta+i)%mod ==0)
    return i;
  }

  //if(i>beta) return 0;
}

int inverterMultiplier(int alpha){
  for(int i=1;i<mod;i++){
    if((alpha*i)%mod == 1)
    return i;
  }
}

int charclear(int alpha, int beta,char c){
  int car,invad,invmul;
  car=(int)c-65;
  invad=inverterAditive(beta);
  invmul=inverterMultiplier(alpha);
  car=(invmul*car)+(invmul*invad);
  car=car%mod;
  car=car+97;
  if(car<0) return 0;
  return car;
}

void decrypt(char *name,int alpha, int beta){
  FILE *arc,*textclear;
  if((arc=fopen(name,"r"))!=NULL){
    textclear=fopen("decrypted.txt","w");
    char car,dec;
    unsigned int decr;
    while(!feof(arc)){
      fscanf(arc,"%c",&car);
      decr=charclear(alpha,beta,car);
      if(decr>0) fprintf(textclear,"%c",decr);
    }
    fclose(textclear);
    fclose(arc);
  }
  printf("decrypted message :D\n");

}

int gcd(int alpha){
  //here starts the greatest common divisor's algorithm
  int a1,b1,r,q1;
  if(alpha>mod){
    a1=alpha;
    b1=mod;
    r=a1%b1;
    while(r>0){
      a1=b1;
      b1=r;
      r=a1%b1;
    }
  }
   else if(mod>alpha){
    a1=mod;
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

void bruteforce(char *name){
  FILE *arc,*dec;
  int cop,decr;
  char c;
  if((arc=fopen(name,"r"))!=NULL){
    dec=fopen("bruteforce.txt","w");
    for(int i=1;i<mod;i++){
      cop=gcd(i);
      if(cop==1){
        fprintf(dec,"invalfa=%d\n",i);
        for(int j=0;j<mod;j++){
          fprintf(dec,"invbeta=%d: ",j);
          while(!feof(arc)){
            fscanf(arc,"%c",&c);
            decr=bf(c,i,j);
            if(decr>0) fprintf(dec,"%c",decr);
          }//end while
          rewind(arc);
          fprintf(dec,"\n\n");
        }//end for j
      }//end if
    }//end for i
  }//end if file
}

int bf(char c,int alpha,int beta){
  int res=(int)c-65;
  res=alpha*res;
  res=res+(alpha*beta);
  res=res%mod;
  res=res+97;
  if(res<0) return 0;
  return res;
}
