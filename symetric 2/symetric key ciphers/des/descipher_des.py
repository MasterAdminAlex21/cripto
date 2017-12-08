from Crypto.Cipher import DES
from Crypto.Util import Counter
import os
import time

ruta=raw_input("Enter the image or path of the image to decrypt: ")
try:
 archivo=open(ruta,"r");
except IOError:
 ruta=raw_input("ERROR: the file doesn\'t exist\nEnter the image or path of the image to encrypt: ")
#empieza el descifrado

exe="./separa "+ruta
os.system(exe)
#time.sleep(10)
cifrado=open("imgn.txt","r")
clave=raw_input("Enter the key: ")
while len(clave)<8:
 clave=raw_input("ERROR: length smaller than the required\nEnter the key: ")

cifra=open("ciph.txt","w")
cad=""
opcion=int(input("Select operation mode: \n1.ECB\n2.CFB\n3.CBC\n4.OFB\n5.CTR\n"))
#condiciionales para modos de operacion

while(opcion<1 or opcion>5):
 opcion=int(input("Invaid Option\nSelect operation mode: \n1.ECB\n2.CFB\n3.CBC\n4.OFB\n5.CTR\n"))

if(opcion==1):#ECB modo
 imgn=cifrado.readline(1)
 ciph=DES.new(clave[:8],DES.MODE_ECB)
 cad=cad+imgn
 while imgn!='':
  imgn=cifrado.readline(1)
  cad=cad+imgn
  if(len(cad)==8):
   img_ciph=ciph.decrypt(cad)
   cad=""
   cifra.write(img_ciph)
 cifra.close()
 cifrado.close()
 union="./unir ciph.txt ECB_decrypt.bmp"
 os.system(union)

elif(opcion==2):#modo CFB
 vi=raw_input("Enter the initialization vector: ")
 while len(vi)<8:
  vi=raw_input("ERROR: smaller lenght than the required\nEnter the initialization vector: ")
 imgn=cifrado.readline(1)
 ciph=DES.new(clave[:8],DES.MODE_CFB,vi[:8])#ingresar el vector de inicializacion
 cad=cad+imgn
 while imgn!='':
  imgn=cifrado.readline(1)
  cad=cad+imgn
  if(len(cad)==8):
   img_ciph=ciph.decrypt(cad)
   cad=""
   cifra.write(img_ciph)
 cifra.close()
 cifrado.close()
 union="./unir ciph.txt CFB_decrypt.bmp"
 os.system(union)

elif(opcion==3):#modo CBC
 vi=raw_input("Enter the initialization vector: ")
 while len(vi)<8:
  vi=raw_input("ERROR: smaller lenght than the required\nEnter the initialization vector: ")
 imgn=cifrado.readline(1)
 ciph=DES.new(clave[:8],DES.MODE_CBC,vi[:8])#ingresar el vector de inicializacion
 cad=cad+imgn
 while imgn!='':
  imgn=cifrado.readline(1)
  cad=cad+imgn
  if(len(cad)==8):
   img_ciph=ciph.decrypt(cad)
   cad=""
   cifra.write(img_ciph)
 cifra.close()
 cifrado.close()
 union="./unir ciph.txt CBC_decrypt.bmp"
 os.system(union)

elif(opcion==4):#modo OFB
 vi=raw_input("Enter the initialization vector: ")
 while len(vi)<8:
  vi=raw_input("ERROR: smaller lenght than the required\nEnter the initialization vector: ")
 imgn=cifrado.readline(1)
 ciph=DES.new(clave[:8],DES.MODE_OFB,vi[:8])
 cad=cad+imgn
 while imgn!='':
  imgn=cifrado.readline(1)
  cad=cad+imgn
  if(len(cad)==8):
   img_ciph=ciph.decrypt(cad)
   cad=""
   cifra.write(img_ciph)
 cifra.close()
 cifrado.close()
 union="./unir ciph.txt OFB_decrypt.bmp"
 os.system(union)

elif(opcion==5):#modo CTR
 imgn=cifrado.readline(1)
 ciph=DES.new(clave[:8],DES.MODE_CTR,counter=Counter.new(64))#arreglar el contador de sta wea
 cad=cad+imgn
 while imgn!='':
  imgn=cifrado.readline(1)
  cad=cad+imgn
  if(len(cad)==8):
   img_ciph=ciph.decrypt(cad)
   cad=""
   cifra.write(img_ciph)
 cifra.close()
 cifrado.close()
 union="./unir ciph.txt CTR_decrypt.bmp"
 os.system(union)


os.system("rm imgn.txt ciph.txt cab.txt")