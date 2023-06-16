import utils
import arguments
from Crypto.Random import get_random_bytes

class Put:
    def __init__(self):
        # citamo podatke iz binarne datoteke
        self.iv, self.salt, self.tag, self.ciphertext = utils.readFromBin()
        # generiramo kljuc
        self.key = utils.generateKey(self.salt)
        

    def decrypt(self):
        # dekriptiramo podatke
        self.plaintext = utils.decryptData(self.key, self.tag, self.iv, self.ciphertext)        
        # pretvaramo plaintext u dictionary
        self.password_dict = utils.stringToDict(self.plaintext)

    # nakon uredivanje plaintext-a, kriptiramo ponovno podatke
    def encrypt(self):
        self.plaintext = utils.dictToString(self.password_dict).encode()
        self.iv = get_random_bytes(16)
        self.salt = get_random_bytes(16)
        self.key = utils.generateKey(self.salt)
        self.ciphertext, self.tag = utils.encryptCypherText(self.key, self.iv, self.plaintext)
    
    def writeToBin(self):
        utils.writeToBin(self.iv, self.salt, self.tag, self.ciphertext)
        self.success()

    def success(self):
        print(f"Stored password for {arguments.args.arg2}.")


        
