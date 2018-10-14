from functools import partial
import time
import datetime
import os
import re
def TTT(T):
    print("\n\n\n\n\n")
    input("cls:")
    os.system('cls')
    if T>=1 and T<=5:
        print('It is week5-in-class')
    else:
        print('It is week5-after-class')
        T=T-5
    print("------------------\tT",T,"\t------------------",sep='')

###TTT(1)###
TTT(1)
f=partial(lambda x,y:x*y,2)
print(f(int(input("Can you print a number:"))))
###TTT(1)###

###TTT(2)###
TTT(2)
t=partial(lambda x,y,z:x*y*z,1,2)
print(t(3))
###TTT(2)###

###TTT(3)###
TTT(3)
def whm(w):
    def whl(*hr,**yyl):
        a=time.time()
        print("Start")
        ll=w(*hr,**yyl)
        [i for i in range(1000001)]
        print(time.time()-a)
        return ll
    return whl
@whm
def wc(a,b,c):
    return a*b*c
print(wc(100,200,300))
###TTT(3)###

###TTT(4)###
TTT(4)
def whm(w):
    def whl(a,b):
        if b!=0:
            ll=w(a,b)
            return ll
        else:
            print("ZeroDivisionError!!!")
    return whl
@whm
def wc(a,b):
    return a/b
print(wc(100,0))
###TTT(4)###

###TTT(5)###
TTT(5)
def whm(w):
    def whl(*hr,**yyl):
        ll=w(*hr,**yyl)
        print(datetime.datetime.now())
        return ll
    return whl
@whm
def wc(a,b,c):
    return a*b*c
print(wc(100,200,300))
###TTT(5)###









###TTT(1)###
TTT(1+5)
def whm(w):
    def whl(a):
        if re.search('[a-z]',a):
            a=a.upper()
            ll=w(a)
            return ll
    return whl
@whm
def wc(a):
    return a
print(wc('.d2gv5n 52gn h5,525l5;2m02.0'))
###TTT(1)###

###TTT(2)###
TTT(2+5)
f=''
for i in range(10001):
    f+=str(i)
    f+="\n"
with open("aa2.txt",'w+') as ff:
    ff.write(f)
def aaa():
    with open("aa2.txt") as f:
        while 1:
            aa=f.readline()
            yield aa
a=aaa()
for i in range(int(input())):
    print(next(a))
###TTT(2)###

###TTT(3)###
TTT(3+5)
def aaa(id):
    while 1:
        yield id
        id=id+1
a=aaa(1)
for i in range(10):
    print(next(a))
a.close()
###TTT(3)###

###TTT(4)###
TTT(4+5)
def aaa(id):
    while 1:
        if (not id%2) and id<=50:
            yield id
        id=id+1
a=aaa(0)
for i in range(26):
    print(next(a))
a.close()
###TTT(4)###

###TTT(5)###
TTT(5)
print("!!!!!!!!!!!!!!!!")
print("bug!bug!bug!bug!")
print("if homework in (C: or D:)")
print("it is not print (C: or D:) file!")
print("bug!bug!bug!bug!")
print("!!!!!!!!!!!!!!!!")
def aaa():
    ph='C:'
    for dirpath,dirnames,filenames in os.walk(ph):
        yield dirpath,dirnames,filenames
a=aaa()
try:
    while 1:
        print(next(a))
except:
    a.close()
###TTT(5)###