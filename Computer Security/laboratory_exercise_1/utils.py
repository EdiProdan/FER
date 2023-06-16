import hashlib
from arguments import args
from Crypto.Cipher import AES


def generateKey(salt):
    password = args.arg1
    
    # broj iteracija za pbkdf2 kako bi se sprijecio brute force napad
    iterations = 1000000
    
    key = hashlib.pbkdf2_hmac('sha256',password=password.encode(), salt=salt, iterations=iterations, dklen=32)
    return key

def encryptCypherText(key, iv, plaintext):
    # stvaramo objekt AES-a
    cipher = AES.new(key, AES.MODE_GCM, nonce = iv)

    # enkriptiramo plaintext
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    # vracamo sifrirani plaintext i tag (potpis/MAC)
    return ciphertext, tag


def writeToBin(iv, salt,tag, ciphertext):
    concatenated_data = iv + salt + tag + ciphertext
    with open('encrypted_data.bin', 'wb') as f:
        try:
            f.write(concatenated_data) 
        except:
            print("Error writing to file.")
           

def readFromBin():
    with open('encrypted_data.bin', 'rb') as f:
        data = f.read()
        iv = data[:16]
        salt = data[16:32]
        tag = data[32:48]
        ciphertext = data[48:]

    return iv, salt, tag, ciphertext


def decryptData(key, tag, iv, ciphertext):
    # stvaramo objekt AES-a
    decipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    # dekriptiramo ciphertext
    decrypted_plaintext = decipher.decrypt_and_verify(ciphertext, tag)

    # vracamo dekriptirani plaintext kao string (dekodeiramo ga)
    return decrypted_plaintext.decode()



def stringToDict(plaintext):
    address_password_dict = {}
    if plaintext == "":
        return {}
    
    # dijelimo plaintext na linije
    plaintext_list = plaintext.split("Ž")
    # za svaku liniju dijelimo na adresu i lozinku
    for line in plaintext_list:
        address, password = line.split("ž")
        address_password_dict[address] = password

    return address_password_dict

def dictToString(address_password_dict):
    plaintext = ""
    # za svaki par u rjecniku, dodajemo ga u plaintext
    for count, pair in enumerate(address_password_dict.items()):
        key = pair[0]
        value = pair[1]
        plaintext += f"{key}ž{value}"
        # ako nije zadnji par, dodajemo znak za novi red
        if count < len(address_password_dict) - 1:
            plaintext += "Ž"

    return plaintext