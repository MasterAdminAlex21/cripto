from Crypto.PublicKey import RSA
from Crypto import Random

#llaves de alice
rand=Random.new().read
keyA=RSA.generate(1024,rand)
print keyA.can_encrypt()
print keyA.can_sign()
alice=open("../alice/privAlice.txt","w")
alice.write(keyA.exportKey('PEM'))
alice.close()
alice=open("../bob/pubAlice.txt","w")
alice2=open("../nidia/pubAlice.txt","w")
keyA=keyA.publickey()
alice.write(keyA.exportKey('PEM'))
alice2.write(keyA.exportKey('PEM'))
alice.close()
alice2.close()

#llaves de bob
rand=Random.new().read
keyB=RSA.generate(1024,rand)
print keyB.can_encrypt()
print keyB.can_sign()
bob=open("privBob.txt","w")
bob.write(keyB.exportKey())
bob.close()
bob=open("../alice/pubBob.txt","w")
bob2=open("../nidia/pubBob.txt","w")
keyB=keyB.publickey()
bob.write(keyB.exportKey())
bob2.write(keyB.exportKey())
bob.close()
bob2.close()

#llaves de nidia
rand=Random.new().read
keyN=RSA.generate(1024,rand)
print keyN.can_encrypt()
print keyN.can_sign()
nidia=open("privNidia.txt","w")
nidia.write(keyN.exportKey())
nidia.close()
nidia=open("../alice/pubNidia.txt","w")
nidia2=open("../bob/pubNidia.txt","w")
keyN=keyN.publickey()
nidia.write(keyN.exportKey())
nidia2.write(keyN.exportKey())
nidia.close()
nidia2.close()
