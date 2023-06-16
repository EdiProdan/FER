from arguments_usermgmt import args
import utils
import getpass

# Password1234!
if __name__ == '__main__':

    if args.command == 'add':

        password = getpass.getpass('Password: ')
        repeat_password = getpass.getpass('Repeat password: ')

        # provjera ako lozinka i ponovljena lozinka se poklapaju
        if not utils.check_password(password, repeat_password):
            print('User add failed. Password mismatch.')
            exit()

        # provjera ako je lozinka dovoljno jaka
        strong_password_check = utils.strong_password_check(password)
        if not strong_password_check:
            # print('Password is not strong enough.')
            print('User add failed. Password mismatch.')
            exit()
        
        # provjera ako korisnik vec postoji
        if utils.check_if_user_exists(args.username):
            # print("Korisnik vec postoji.")
            print('User add failed. Password mismatch.')
            exit()

        salt = utils.generate_salt()
        hash_ = utils.generate_hash(password, salt)

        output = f'{args.username},0,{salt.hex()},{hash_.hex()}'
        with open('users.txt', 'a+') as f:
            f.write(output + '\n')

        print(f'User {args.username} successfuly added.')

    elif args.command == 'passwd':

        password = getpass.getpass('Password: ')
        repeat_password = getpass.getpass('Repeat password: ')

        if not utils.check_password(password, repeat_password):
            print('Password change failed. Password mismatch.')
            exit()

        # check if password is strong enough
        strong_password_check = utils.strong_password_check(password)
        if not strong_password_check:
            # print('Password is not strong enough.')
            print('Password change failed. Password mismatch.')
            exit()

        if not utils.check_if_user_exists(args.username):
            # print("Korisnik ne postoji.")
            print('Password change failed. Password mismatch.')
            exit()

        _, compare_salt, compare_hash = utils.get_flag_salt_hash(
            args.username)

        if utils.verify_password_match(password, bytes.fromhex(compare_salt), compare_hash):
            # print('New password must be different from the old one.')
            print('Password change failed. Password mismatch.')
            exit()
        

        # get all lines from file
        lines = utils.get_all_lines()

        salt = utils.generate_salt()
        hash_ = utils.generate_hash(password, salt)
        output = f'{args.username},0,{salt.hex()},{hash_.hex()}\n'
        utils.write_lines_back(lines, output)

        print("Password change successful.")

    elif args.command == 'forcepass':
    
        if not utils.check_if_user_exists(args.username):
            # print('User not found.')
            print('Something went wrong.')
            exit()

        # get all lines from file
        lines = utils.get_all_lines()

        output = utils.change_flag(lines, args.username)

        utils.write_lines_back(lines, output)
        print("User will be requested to change password on next login.")

    elif args.command == 'del':
        lines = utils.get_all_lines()

        if not utils.check_if_user_exists(args.username):
            # print('User not found.')
            print('Something went wrong.')
            exit()

        with open('users.txt', 'w') as f:
            for line in lines:
                if not line.startswith(args.username):
                    f.write(line)

        print('User successfuly removed.')
