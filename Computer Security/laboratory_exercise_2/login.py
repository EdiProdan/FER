import getpass
from arguments_login import args
import utils

if __name__ == "__main__":

    password = getpass.getpass('Password: ')

    # provjera ako korisnik postoji
    if not utils.check_if_user_exists(args.username):
        print('Username or password incorrect.')
        exit()

    flag, salt, hash_ = utils.get_flag_salt_hash(args.username)
    flag = int(flag)

    if flag == 1:

        new_password = getpass.getpass('New password: ')
        repeat_new_password = getpass.getpass('Repeat new password: ')

        # provjera ako nova lozinka i ponovljena nova lozinka se poklapaju
        if not utils.check_password(new_password, repeat_new_password):
            print('Username or password incorrect.')
            exit()

        # provjera ako je nova lozinka dovoljno jaka
        strong_password_check = utils.strong_password_check(new_password)
        if not strong_password_check:
            print('Username or password incorrect.')
            exit()

        # provjera ako je stara lozinka tocno unesena
        if not utils.verify_password_match(password, bytes.fromhex(salt), hash_):
            print('Username or password incorrect.')
            exit()

        # provjera ako je nova lozinka razlicita od stare
        if utils.verify_password_match(new_password, bytes.fromhex(salt), hash_):
            print('Username or password incorrect.')
            exit()

        # unesi novu lozinku u bazu
        lines = utils.get_all_lines()
        salt = utils.generate_salt()
        hash_ = utils.generate_hash(new_password, salt)
        output = f'{args.username},0,{salt.hex()},{hash_.hex()}\n'
        utils.write_lines_back(lines, output)
        print('Login successful.')

    elif flag == 0:
        if utils.verify_password_match(password, bytes.fromhex(salt), hash_):
            wrong_password = False
            print('Login successful.')
        else:
            wrong_password = True
            print('Username or password incorrect.')

        while wrong_password:
            password = getpass.getpass('Password: ')
            if utils.verify_password_match(password, bytes.fromhex(salt), hash_):
                print('Login successful.')
                wrong_password = False
            else:
                print('Username or password incorrect.')
