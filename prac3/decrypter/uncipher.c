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
void euclidesExtendido(long,long,long*,long*,long*);

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
    long x,y,d;
    euclidesExtendido((long)mod,(long)alfa,&d,&x,&y);
    printf("Additive Inversor: %d\n",inverterAditive(beta));
    printf("Multiplier Inversor: %ld\n",/*inverterMultiplier(alfa)*/y);//the inverser


    //decrypt function
    decrypt(arch,alfa,beta);
  }else if(res=='n'){
    printf("it will be decrypted by using brute force\n");
    //brute force function
    bruteforce(arch);
  }else{
    printf("ERROR: invalid option");
  }
}

int inverterAditive(int beta){
  if(beta==0) return mod;
  int i;
  for(i=1;i<=mod;i++){
    if((beta+i)%mod ==0)
    return i;
  }

  //if(i>beta) return 0;
}

int inverterMultiplier(int alpha){
  for(int i=1;i<=mod;i++){
    if((alpha*i)%mod == 1)
    return i;
  }
}

int charclear(int alpha, int beta,char c){
  long car,invad,invmul;
  car=(int)c-65;
  //here is the E.E.A
  long d,x,y;
  euclidesExtendido((long)mod,(long)alpha,&d,&invad,&invmul);
 // printf("euclidesExtendido: %ld %ld %ld %ld \n",(long)mod,(long)alpha,invad,invmul);
  //if(invad<0) invad=(-1)*invad;
  if(invmul<0) invmul=inverterAditive((-1)*(int)invmul);

  //printf("invad: %d  invmul: %d \n",invad,invmul );

  //here end
  
  invad=inverterAditive(beta);
  /*invmul=inverterMultiplier(alpha);
  */
  //printf("inversor: %ld %ld\n",invad,invmul );
  car=(invmul*car)+(invmul*invad);
  car=car%mod;
  car=car+97;
  if(car<0) return 0;
  return (int)car;
}

void decrypt(char *name,int alpha, int beta){
  FILE *arc,*textclear;
  if((arc=fopen(name,"r"))!=NULL){
    textclear=fopen("decrypted.txt","w");
    char car,dec;
    unsigned int decr;
    long d,x,y;
  euclidesExtendido((long)mod,(long)alpha,&d,&x,&y);
   printf("%ld = %ld(%ld) + %ld(%ld) \n",d,(long)mod,x,(long)alpha,y);
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


//Euclides's extended Algorithm
void euclidesExtendido(long a, long b,long *d,long *x, long *y){
  long x1,y1;

  if(b==0){
    *d=a;
    *x=1;
    *y=0;
  }else{
    euclidesExtendido(b,a%b,d,x,y);
//    printf("%ld %ld %ld %ld %ld\n",a,b,*d,*x,*y );
    x1=*x;
    y1=*y;
    *x=y1;
    *y=x1- (a/b)*y1;
  }
  }