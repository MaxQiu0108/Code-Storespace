import hashlib
import random
import time
asdf = open('token.txt', 'a', encoding = 'utf-8')
b = str(random.randint(1,10000))
a = input("type password to get secret")
if hashlib.sha512(a.encode('utf-8')).hexdigest() =='91c00c70d86f4a00b2306bca94e3bd8881a22001f100169224d37a1372a0d12c1d0a1dffee007ef2dd6b070484bffda8646c6936b9def8d10e4b3fa4b31fac5e':
    token = hashlib.sha512((a + b).encode('utf-8')).hexdigest()
    print('this is ur token:',token)
    print("this is ur identification key",b)
    asdf.write('token: ' )
    asdf.write(token)
    asdf.write('\n')
    asdf.write('id_key is: ')
    asdf.write(b)
    asdf.close()
    print("you can find it in token.txt")
    print('do not lose or change em, send it to max to find out if it is correct')
    time.sleep(5)
else:
    print('nope')
    time.sleep(1)
