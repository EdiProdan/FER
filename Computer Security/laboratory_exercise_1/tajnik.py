from arguments import args
from Init import Init
from Put import Put
from Get import Get

if __name__ == '__main__':
    if args.command == 'init':
        init = Init()
        init.encrypt()
        init.writeToBin()


    elif args.command == 'put':
        put = Put()
        try:
            put.decrypt()
            put.password_dict[args.arg2] = args.arg3
            put.encrypt()
            put.writeToBin()
        except ValueError:
            print("Master password incorrect or integrity check failed.")
        

    elif args.command == 'get':
        get = Get()
        try:
            get.decrypt()
            if args.arg2 in get.address_password_dict:
                print(f"Password for {args.arg2} is: {get.address_password_dict[args.arg2]}.")
            else:
                print("Master password incorrect or integrity check failed.")
        except ValueError:
            print("Master password incorrect or integrity check failed.")
        
    else:
        print('Nepoznata naredba.')
