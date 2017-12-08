from Crypto.PublicKey import RSA
from Crypto.Hash import SHA

#se lee el mensaje cifrado
mensaje=open("cf.txt","r")
msg=""
msg=mensaje.readline()
mensaje.readline()
print "mensaje"
print msg

#obtenemos la firma del archivo
mensaje.readline()
firma=mensaje.readline()
print "firma"
print firma

#se obtiene la llave privada de bob
bob=open("privBob.txt","r")
privKey=RSA.importKey(bob.read())
bob.close()
print privKey

#se decifra el mensaje
tp=privKey.decrypt(msg)
print "texto claro"
#print len(msg)
print tp

#se aplica sha al mensaje
sha=SHA.new()
sha.update(msg)

