from Crypto.Hash import SHA
import os

ruta=raw_input("ingrese archivo o ruta de archivo: ")
try:
	archivo=open(ruta,"r")
except IOError:
	ruta=raw_input("Error: archivo inexistente\ningrese archivo o ruta de archivo: ")

arc=open(ruta,"r")
msg=arc.readlines()
hash1=SHA.new()
mens=str(msg)
hash1.update(mens)
#hashex=hash1.hexdigest
exe="./union "+ruta+" "+hash1.hexdigest()
os.system(exe)

