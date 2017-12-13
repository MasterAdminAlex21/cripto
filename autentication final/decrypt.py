from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
import ast
from Crypto.Signature import PKCS1_v1_5

#se obtienen la llave publica de alice
alice=open("pubAlice.txt","r")
pubKey=RSA.importKey(alice.read())
alice.close()
#print pubKey

#se obtiene la llave privada de bob
bob=open("privBob.txt")
privKey=RSA.importKey(bob.read())
bob.close()
#print privKey

#se lee el mensaje
msg=open("cf.txt","r")
msg_ciph=msg.readline()
#print msg_ciph

#se obtiene la firma
msg.readline()
firma=msg.readline()
#print firma
msg.close()

#se decifra el mensaje
mens=privKey.decrypt(ast.literal_eval(msg_ciph))
print mens


#se verifica la firma
hash1=SHA.new(mens).hexdigest()
#print hash1

if(pubKey.verify(hash1,ast.literal_eval(firma))):
	print "verificado: msg de alice"
else:
	print "invalido, mensaje modificado"