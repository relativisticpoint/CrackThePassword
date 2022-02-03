
from threading import Thread
import numpy
import string
from itertools import product
from time import time
from numpy import loadtxt
from multiprocessing import Process
import multiprocessing as mp
import threading
import sys

def product_loop(password, generator):
    for p in generator:
        if ''.join(p) == password:
            print('\nPassword:', ''.join(p))
            return ''.join(p)
    return False

def cherche(password,q):
    print("comparaison avec les mdp les plus communs")
    common_pass = loadtxt('probable-v2-top12000.txt', dtype=str)
    common_names = loadtxt('middle-names.txt', dtype=str)
    cp = [c for c in common_pass if c == password]
    cn = [c for c in common_names if c == password]
    cnl = [c.lower() for c in common_names if c.lower() == password]

    if len(cp) == 1:
        print('\nPassword:', cp)
        q.put(cp)
    if len(cn) == 1:
        print('\nPassword:', cn)
        q.put(cn)
    if len(cnl) == 1:
        print('\nPassword:', cnl)
        q.put(cnl)
    else:
        q_check.put('fail1')

def cherche2(password,q,max_char):
    print("recherche aleatoire")
    generator = product(string.ascii_lowercase,repeat=int(max_char))
    p = product_loop(password,generator)
    print(p)
    if p is not False:
        print('\nPassword:', p)
        q.put(p)

if __name__ == '__main__':

    q_check = mp.Queue()
    q = mp.Queue()
    password = sys.argv[1]
    p=threading.Thread(target=cherche,args=(password,q,))
    p1=threading.Thread(target=cherche2,args=(password,q,len(password),))
    start = time()
    p.start()
    p1.start()
    p.join()
    end1 = time()
    p1.join()
    end = time()
    if q.get() != None:
        print("I found your password in {} seconds".format(end1-start))
    else:
        print("we couldn't find the password, maybe it s too long...")




    
    
