import utils
from Crypto.Random import get_random_bytes


class Init:
    def __init__(self):
        # generiranje nasumicnog salt-a
        self.salt = get_random_bytes(16)

        # generiranje nasumicnog iv-a
        self.iv = get_random_bytes(16)
    
        # generiranje kljuca
        self.key = utils.generateKey(self.salt)
    

    # funkcija za enkripciju, na pocetku je plaintext prazan string
    def encrypt(self):
        self.ciphertext, self.tag = utils.encryptCypherText(self.key ,self.iv, b'')

    # funkcija za upisivanje u binarnu datoteku
    def writeToBin(self):
        utils.writeToBin(self.iv, self.salt, self.tag, self.ciphertext)
        self.success()
        
    def success(self):
        print("Password manager initialized.")
    
     