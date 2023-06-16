from Crypto.Random import get_random_bytes
import hashlib
import re


def check_password(password: str, repeat_password: str) -> bool:
    """Check if password and repeat password match

    Args:
        password (str): password
        repeat_password (str): repeat password

    Returns:
        bool: True if passwords match, False otherwise
    """
    if password != repeat_password:
        return False

    return True


def strong_password_check(password: str) -> object:
    """Check if password is strong enough

    Args:
        password (str): password

    Returns:
        object: regex object
    """
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    # check if password passes regex
    x = re.search(regex, password)
    return x

def check_if_user_exists(username: str) -> bool:
    """Check if user exists

    Args:
        username (str): username

    Returns:
        bool: True if user exists, False otherwise
    """
    try:
        for line in open('users.txt', 'r'):
            if line.startswith(username):
                return True
        return False
    except FileNotFoundError:
        return False


def generate_salt() -> bytes:
    """Generate salt

    Returns:
        bytes: salt
    """
    salt = get_random_bytes(32)
    return salt


def generate_hash(password: str, salt: bytes) -> bytes:
    """Generate hash

    Args:
        password (str): password
        salt (bytes): salt

    Returns:
        bytes: hash
    """
    iterations = 1000000

    hash_ = hashlib.pbkdf2_hmac('sha256', password=password.encode(),
                                salt=salt, iterations=iterations, dklen=32)

    return hash_


def write_lines_back(lines: str, output: str):
    """Pisanje linija natrag u datoteku

    Args:
        lines (str): lines
        output (str): output

    Returns:
        None
    """
    with open('users.txt', 'w') as f:
        for line in lines:
            if not line.startswith(output.split(',')[0]):
                f.write(line)
            else:
                f.write(output)


def get_flag_salt_hash(username: str) -> tuple:
    """Dohvacanje zastavice, soli i hasha iz datoteke

    Args:
        username (str): username

    Returns:
        tuple: flag, salt and hash
    """
    for line in open('users.txt', 'r'):
        if line.startswith(username):
            line = line.strip()
            username, flag, salt, hash_ = line.split(',')

    return flag, salt, hash_


def verify_password_match(password: str, salt: bytes, hash_: str) -> bool:
    """Provjera da li se lozinka podudara s hashom


    Args:
        password (str): password
        salt (bytes): salt
        hash_ (str): hash

    Returns:    
        bool: True if password matches the hash, False otherwise
    """

    hash_verify = generate_hash(password, salt)
    if hash_verify.hex() == hash_:
        return True
    else:
        return False


def get_all_lines():
    """Dohvacanje svih linija iz datoteke

    Returns:
        list: lines
    """
    with open('users.txt', 'r') as f:
        return f.readlines()


def change_flag(lines: list, username: str) -> str:
    """Mijenja zastavicu na 1

    Args:
        lines (list): lines
        username (str): username

    Returns:
        str: output
    """
    for line in lines:
        if line.startswith(username):
            line = line.strip()
            username, flag, salt, key = line.split(',')
            output = f'{username},1,{salt},{key}\n'
    return output
