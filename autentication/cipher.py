from Crypto.PublicKey import RSA
from Crypto.Hash import SHA

#se obtiene la llave publica de bob
bob=open("pubBob.txt","r")
pubKey=RSA.importKey(bob.read())
bob.close()
print pubKey

#llave privada de bob para una prueba de decifrado
#bob=open("privBob.txt","r")
#privKeyB=RSA.importKey(bob.read())
#bob.close()
#print privKeyB

#se obtiene la llave privada de alice
alice=open("privAlice.txt")
privKey=RSA.importKey(alice.read())
alice.close()
print privKey

#se abre el mensaje
msg=open("msg.txt","r")
mens=str(msg.readlines())
print mens

#se genera el digesto
hash1=SHA.new()
hash1.update(mens)
print hash1.hexdigest()

#se cifra con la llave privada de alice
firma=privKey.encrypt(hash1.hexdigest(),32)
print firma

#se crea el mensaje cifrado
cifra=open("cf.txt","w")
men_cif=pubKey.encrypt(mens,32)
print "mensaje cifrado"
print men_cif

#print privKeyB.decrypt(men_cif)

cifra.write(str(men_cif)+"\n----------------------------------------\nFirma Digital\n"+str(firma))


