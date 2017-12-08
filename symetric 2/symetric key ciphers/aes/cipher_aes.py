from Crypto.Cipher import AES
from Crypto.Util import Counter
import os

ruta=raw_input("Enter the image or path of the image to encrypt: ")
try:
 archivo=open(ruta,"r");
except IOError:
 ruta=raw_input("ERROR: the file doesn\'t exist\nEnter the image or path of the image to encrypt: ")
#empieza el cifrado
exe="./separa "+ruta
os.system(exe)
cifrado=open("imgn.txt","r")
clave=raw_input("Enter the key(16, 24 or 32 chars): ")
while len(clave)<16:
 clave=raw_input("ERROR: length smaller than the required\nEnter the key(16, 24 or 32 chars): ")
 
cifra=open("ciph.txt","w")
cad=""
opcion=int(input("Select operation mode: \n1.ECB\n2.CFB\n3.CBC\n4.OFB\n5.CTR\n"))
#condiciionales para modos de operacion

while(opcion<1 or opcion>5):
 opcion=int(input("Invalid option\nSelect operation mode: \n1.ECB\n2.CFB\n3.CBC\n4.OFB\n5.CTR\n"))

if(opcion==1):#ECB modo
 imgn=cifrado.readline(1)
 if(len(clave)>=32):
  ciph=AES.new(clave[:32],AES.MODE_ECB)
 elif(len(clave)<32 and len(clave)>=24):
  ciph=AES.new(clave[:24],AES.MODE_ECB)
 elif(len(clave)<24 and len(clave)>=16):
  ciph=AES.new(clave[:16],AES.MODE_ECB)
 cad=cad+imgn
 while imgn!='':
  imgn=cifrado.readline(1)
  cad=cad+imgn
  if(len(cad)==16):
   img_ciph=ciph.encrypt(cad)
   cad=""
   cifra.write(img_ciph)
 cifra.close()
 cifrado.close()
 union="./unir ciph.txt ECB_ciph.bmp"
 os.system(union)

elif(opcion==2):#modo CFB
 vi=raw_input("Enter the initialization vector("+str(len(clave))+" chars): ")
 while len(vi)!=len(clave):
  vi=raw_input("ERROR: vector's length different than the key ("+str(len(clave))+")\nEnter the initialization vector("+str(len(clave))+" chars): ")
 imgn=cifrado.readline(1)
 if(len(clave)>=32):
  ciph=AES.new(clave[:32],AES.MODE_CFB,vi[:32])
 elif(len(clave)<32 and len(clave)>=24):
  ciph=AES.new(clave[:24],AES.MODE_CFB,vi[:24])
 elif(len(clave)<24 and len(clave)>=16):
  ciph=AES.new(clave[:16],AES.MODE_CFB,vi[:16])#ingresar el vector de inicializacion
 cad=cad+imgn
 while imgn!='':
  imgn=cifrado.readline(1)
  cad=cad+imgn
  if(len(cad)==16):
   img_ciph=ciph.encrypt(cad)
   #print img_ciph
   cad=""
   cifra.write(img_ciph)
 cifra.close()
 cifrado.close()
 union="./unir ciph.txt CFB_ciph.bmp"
 os.system(union)

elif(opcion==3):#modo CBC
 vi=raw_input("Enter the initialization vector("+str(len(clave))+" chars): ")
 while len(vi)!=len(clave):
  vi=raw_input("ERROR: vector's length different than the key ("+str(len(clave))+")\nEnter the initialization vector("+str(len(clave))+" chars): ")
 imgn=cifrado.readline(1)
 if(len(clave)>=32):
  ciph=AES.new(clave[:32],AES.MODE_CBC,vi[:32])
 elif(len(clave)<32 and len(clave)>=24):
  ciph=AES.new(clave[:24],AES.MODE_CBC,vi[:24])
 elif(len(clave)<24 and len(clave)>=16):
  ciph=AES.new(clave[:16],AES.MODE_CBC,vi[:16])#ingresar el vector de inicializacion
 cad=cad+imgn
 while imgn!='':
  imgn=cifrado.readline(1)
  cad=cad+imgn
  if(len(cad)==16):
   img_ciph=ciph.encrypt(cad)
   #print img_ciph
   cad=""
   cifra.write(img_ciph)
 cifra.close()
 cifrado.close()
 union="./unir ciph.txt CBC_ciph.bmp"
 os.system(union)

elif(opcion==4):#modo OFB
 vi=raw_input("Enter the initialization vector("+str(len(clave))+" chars): ")
 while len(vi)!=len(clave):
  vi=raw_input("ERROR: vector's length different than the key ("+str(len(clave))+")\nEnter the initialization vector("+str(len(clave))+" chars): ")
 imgn=cifrado.readline(1)
 if(len(clave)>=32):
  ciph=AES.new(clave[:32],AES.MODE_OFB,vi[:32])
 elif(len(clave)<32 and len(clave)>=24):
  ciph=AES.new(clave[:24],AES.MODE_OFB,vi[:24])
 elif(len(clave)<24 and len(clave)>=16):
  ciph=AES.new(clave[:16],AES.MODE_OFB,vi[:16])
 cad=cad+imgn
 while imgn!='':
  imgn=cifrado.readline(1)
  cad=cad+imgn
  if(len(cad)==16):
   img_ciph=ciph.encrypt(cad)
   #print img_ciph
   cad=""
   cifra.write(img_ciph)
 cifra.close()
 cifrado.close()
 union="./unir ciph.txt OFB_ciph.bmp"
 os.system(union)

elif(opcion==5):#modo CTR
 #clave=clave *2
 imgn=cifrado.readline(1)
 if(len(clave)>=32):
  ciph=AES.new(clave[:32],AES.MODE_CTR,counter=Counter.new(256))
 elif(len(clave)<32 and len(clave)>=24):
  ciph=AES.new(clave[:24],AES.MODE_CTR,counter=Counter.new(192))
 elif(len(clave)<24 and len(clave)>=16):
  ciph=AES.new(clave[:16],AES.MODE_CTR,counter=Counter.new(128))
 cad=cad+imgn
 while imgn!='':
  imgn=cifrado.readline(1)
  cad=cad+imgn
  if(len(cad)==16):
   img_ciph=ciph.encrypt(cad)
   cad=""
   cifra.write(img_ciph)
 cifra.close()
 cifrado.close()
 union="./unir ciph.txt CTR_ciph.bmp"
 os.system(union)


os.system("rm imgn.txt ciph.txt cab.txt")

