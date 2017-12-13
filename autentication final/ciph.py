from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5

#se obtiene la llave publica de bob
bob=open("pubBob.txt","r")
pubKey=RSA.importKey(bob.read())
bob.close()
#print pubKey

#se obtiene la llave privada de alice
alice=open("privAlice.txt")
privKey=RSA.importKey(alice.read())
alice.close()
#print privKey

#se abre el mensaje
msg=open("msg.txt","r")
mens=msg.read()
#print mens
msg.close()

#se genera el digesto
hash1=SHA.new(mens).hexdigest()
#print hash1

#se cifra con la llave privada de alice
#firma=privKey.encrypt(hash1,32)
#print "firma:\n"+str(firma)

#otra forma de firma
firma=privKey.sign(hash1,123)
#print firma

#se cifra el mensaje con la llave publica de bob
msg_ciph=pubKey.encrypt(mens,32)
#print "mensaje cifrado:\n"+str(msg_ciph)

#se guarda en el archivo
enc=open("cf.txt","w")
enc.write(str(msg_ciph)+"\n-------------------------------\n"+str(firma))
enc.close()
print "mensaje cifrado\n"