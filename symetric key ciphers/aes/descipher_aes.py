from Crypto.Cipher import AES
from Crypto.Util import Counter
import os

ruta=raw_input("ingrese ruta de imagen a descifrar: ")
try:
 archivo=open(ruta,"r");
except IOError:
 ruta=raw_input("ERROR: archivo inexistente\nIngrese ruta de imagen a descifrar: ")
#empieza el descifrado

exe="./separa "+ruta
os.system(exe)

cifrado=open("imgn.txt","r")
clave=raw_input("Ingrese clave(16, 24 o 32 caracteres): ")
while len(clave)<16:
 clave=raw_input("ERROR: longitud menor a la requerida\nIngrese clave(16, 24 o 32 caracteres): ")

cifra=open("ciph.txt","w")
cad=""
opcion=int(input("Seleccione modo de operacion: \n1.ECB\n2.CFB\n3.CBC\n4.OFB\n5.CTR\n"))
#condiciionales para modos de operacion

while(opcion<1 or opcion>5):
 opcion=int(input("Opcion no valida\nSelecciione modo de operacion: \n1.ECB\n2.CFB\n3.CBC\n4.OFB\n5.CTR\n"))

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
   img_ciph=ciph.decrypt(cad)
   cad=""
   cifra.write(img_ciph)
 cifra.close()
 cifrado.close()
 union="./unir ciph.txt ECB_decrypt.bmp"
 os.system(union)

elif(opcion==2):#modo CFB
 vi=raw_input("ingrese vector de inicializacion: ")
 while len(vi)!=len(clave):
  vi=raw_input("ERROR: vector de longitud distinta a la clave ("+str(len(clave))+")\ningrese vector de inicializacion: ")
 imgn=cifrado.readline(1)
 if(len(clave)>=32):
  ciph=AES.new(clave[:32],AES.MODE_CFB,vi[:32])
 elif(len(clave)<32 and len(clave)>=24):
  ciph=AES.new(clave[:24],AES.MODE_CFB,vi[:24])
 elif(len(clave)<24 and len(clave)>=16):
  ciph=AES.new(clave[:16],AES.MODE_CFB,vi[:16])
 cad=cad+imgn
 while imgn!='':
  imgn=cifrado.readline(1)
  cad=cad+imgn
  if(len(cad)==16):
   img_ciph=ciph.decrypt(cad)
   cad=""
   cifra.write(img_ciph)
 cifra.close()
 cifrado.close()
 union="./unir ciph.txt CFB_decrypt.bmp"
 os.system(union)

elif(opcion==3):#modo CBC
 vi=raw_input("ingrese vector de inicializacion: ")
 while len(vi)!=len(clave):
  vi=raw_input("ERROR: vector de longitud distinta a la clave ("+str(len(clave))+")\ningrese vector de inicializacion: ")
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
   img_ciph=ciph.decrypt(cad)
   cad=""
   cifra.write(img_ciph)
 cifra.close()
 cifrado.close()
 union="./unir ciph.txt CBC_decrypt.bmp"
 os.system(union)

elif(opcion==4):#modo OFB
 vi=raw_input("ingrese vector de inicializacion: ")
 while len(vi)!=len(clave):
  vi=raw_input("ERROR: vector de longitud distinta a la clave ("+str(len(clave))+")\ningrese vector de inicializacion: ")
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
   img_ciph=ciph.decrypt(cad)
   cad=""
   cifra.write(img_ciph)
 cifra.close()
 cifrado.close()
 union="./unir ciph.txt OFB_decrypt.bmp"
 os.system(union)

elif(opcion==5):#modo CTR
 imgn=cifrado.readline(1)
 if(len(clave)>=32):
  ciph=AES.new(clave[:32],AES.MODE_CTR,counter=Counter.new(128))
 elif(len(clave)<32 and len(clave)>=24):
  ciph=AES.new(clave[:24],AES.MODE_CTR,counter=Counter.new(128))
 elif(len(clave)<24 and len(clave)>=16):
  ciph=AES.new(clave[:16],AES.MODE_CTR,counter=Counter.new(128))#arreglar el contador de sta wea
 cad=cad+imgn
 while imgn!='':
  imgn=cifrado.readline(1)
  cad=cad+imgn
  if(len(cad)==16):
   img_ciph=ciph.decrypt(cad)
   cad=""
   cifra.write(img_ciph)
 cifra.close()
 cifrado.close()
 union="./unir ciph.txt CTR_decrypt.bmp"
 os.system(union)


os.system("rm imgn.txt ciph.txt cab.txt")