import utils

class Get:
    def __init__(self):
        self.iv, self.salt, self.tag, self.ciphertext = utils.readFromBin()
        self.key = utils.generateKey(self.salt)
    
    # dekriptiramo podatke
    def decrypt(self):
        self.plaintext = utils.decryptData(self.key, self.tag, self.iv, self.ciphertext)
        # pretvaramo plaintext u dictionary
        self.address_password_dict = utils.stringToDict(self.plaintext)
