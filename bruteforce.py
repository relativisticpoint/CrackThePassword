"""
 @RaphaelVallat a tt fait moi j ai juste bidouille
"""
import numpy
import string
from itertools import product
from time import time
from numpy import loadtxt


def product_loop(password, generator):
    for p in generator:
        if ''.join(p) == password:
            print('\nPassword:', ''.join(p))
            return ''.join(p)
    return False


def bruteforce(password, max_nchar=8):
    """Password brute-force algorithm.

    Parameters
    ----------
    password : string
        To-be-found password.
    max_nchar : int
        Maximum number of characters of password.

    Return
    ------
    bruteforce_password : string
        Brute-forced password
    """
    print('1) Comparing with most common passwords / first names')
    common_pass = loadtxt('probable-v2-top12000.txt', dtype=str)
    common_names = loadtxt('middle-names.txt', dtype=str)
    cp = [c for c in common_pass if c == password]
    cn = [c for c in common_names if c == password]
    cnl = [c.lower() for c in common_names if c.lower() == password]

    if len(cp) == 1:
        print('\nPassword:', cp)
        return cp
    if len(cn) == 1:
        print('\nPassword:', cn)
        return cn
    if len(cnl) == 1:
        print('\nPassword:', cnl)
        return cnl
    """
    # this find the 
    print('2) Digits cartesian product')
    for l in range(1, 9):
        generator = product(string.digits, repeat=int(l))
        print("\t..%d digit" % l)
        p = product_loop(password, generator)
        if p is not False:
            return p
    """
    # i ll try to implement this method

    print('si on connait le nombre de char')
    generator = product(string.ascii_lowercase,repeat=int(max_nchar))
    p = product_loop(password,generator)
    if p is not False:
        return p

    print(' 2bis) ASCII lowercase')
    # relativisticpoint:the pb with this method is that it tries to find the pswd using all the 
    # combinations i think we could significantly reduce the time by precising 
    # the number of characters we re gonna use
    for l in range(1, max_nchar + 1):
        print("\t..%d char" % l)
        generator = product(string.ascii_lowercase,
                            repeat=int(l))
        p = product_loop(password, generator)
        if p is not False:
            return p
    

    print('3) Digits + ASCII lowercase')
    for l in range(1, max_nchar + 1):
        print("\t..%d char" % l)
        generator = product(string.digits + string.ascii_lowercase,
                            repeat=int(l))
        p = product_loop(password, generator)
        if p is not False:
            return p
    

    print('4) Digits + ASCII lower / upper + punctuation')
    # If it fails, we start brute-forcing the 'hard' way
    # Same as possible_char = string.printable[:-5]
    all_char = string.digits + string.ascii_letters + string.punctuation

    for l in range(1, max_nchar + 1):
        print("\t..%d char" % l)
        generator = product(all_char, repeat=int(l))
        p = product_loop(password, generator)
        if p is not False:
            return p


# EXAMPLE

# passw = str(input('type in the password you want to bruteforce : '))
start = time()
bruteforce('leopol',6) # changed the method now you have to specify the number of char that are contained in the passwrd pour aller plus vite
end = time()
print('Total time: %.2f seconds' % (end - start))