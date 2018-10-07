import os
os.system('cls')
def TTT(T):
    print("------------------\tT",T,"\t------------------",sep='')


###T1###
TTT(1)
class Animal():
    name='animal'
    def call():
        pass
class Dog(Animal):
    name='dog'
    def call(self):
        print("My name is "+self.name+" miaomiaomiao")
class Cat(Animal):
    name='cat'
    def call(self):
        print("My name is "+self.name+" wangwangwang")
dog=Dog()
dog.call()
cat=Cat()
cat.call()
TTT(1)


###T2###
TTT(2)
def aaa(a):
    aa=(1 if(a<=2) else (aaa(a-1)+aaa(a-2)))
    return aa
a=int(input())
for i in range(1,10000):
    if aaa(i)<a:
        print(aaa(i))
    else:
        break
'''
for i in range(1,int(input())+1):
    print(aaa(i))
'''
TTT(2)


###T3###
TTT(3)
print([i for i in range(1,int(input())+1) if i%2==1])
TTT(3)


###T4###
TTT(4)
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def aaa():
    x=int(input())
    y=int(input())
    z=input()
    try:
        if z=="+":
            return add(x,y)
        elif z=="-":
            return sub(x,y)
        elif z=="*":
            return mul(x,y)
        elif z=="/":
            return div(x,y)
        else:
            print("You are naughty!!!")
    except:
        print("Except!!!")
        return
print(aaa())
TTT(4)


###T5###
TTT(5)
#sys.path.append can add path
#a.__file__ is a.path

import this
import sys
sys.path.append(this.__file__)
with open(this.__file__,"r") as q:
    with open("th_is.py",mode='w+') as d:
        for qq in q.readlines():
            d.write(qq)
            #one is ok write
TTT(5)










input("cls:")
os.system('cls')

###T6###
TTT(6)
str1="""def TTT(T):
    print("T",T,end="\t")
    print("T",T,end="\t")
    print("T",T,)
import os
###T1###
TTT(1)
import random
def aaa():
    mima=''
    a=0
    b=0
    c=0
    d=0
    a=int(input("number has "))
    b=int(input("big letter has "))
    d=int(input("small letter has "))
    c=int(input("symbol has "))
    if a>0:
        for i in range(a):
            l=random.randint(0,9)
            mima+=str(l)
    if b>0:
        for i in range(b):
            l=random.randint(65,90)
            mima+=chr(l)
    if d>0:
        for i in range(d):
            l=random.randint(97,122)
            mima+=chr(l)
    if c>0:
        for i in range(c):
            big_or_small=4
            big_or_small=random.randint(0,3)
            if big_or_small==0:
                l=random.randint(32,47)
            if big_or_small==1:
                l=random.randint(58,64)
            if big_or_small==2:
                l=random.randint(91,96)
            if big_or_small==3:
                l=random.randint(123,126)
            mima+=chr(l)
    if mima=="":
        print("On No!")
        return 0

    password=list(mima)
    random.shuffle(password)
    password=''.join(password)

    print("It is your password!")
    print(password)
aaa()
TTT(1)


###T2###
TTT(2)
def aaa(l,lst):
    con=0
    for i in lst:
        con+=1
        if i==l:
            print(l," in ",lst)
            changdu=len(lst)
            a=con/changdu
            if a<=0.5:
                print("left")
            elif a>0.5:
                print("right")
            break
    else:
        print(lst," is not ",l)
l=[5,8,6,9,3,2,555,4,7,8,25,98,20,1]
aaa(1,l)
aaa(7,l)
aaa(555,l)
aaa(4,l)
aaa(102020,l)
TTT(2)


###T3###
TTT(3)
def aaa():
    lst=[]
    for i in range(2,101):
        for l in range(2,i):
            if(i%l==0):
                break
        else:
            lst.append(i)
    return lst
b=aaa()
print(b)
TTT(3)


###T4###
TTT(4)
a1='''def aaa():
    x=int(input("number:"))
    y=int(input("number:"))
    z=input("symbol:")
    if z=="+":
        add(x,y)
    elif z=="-":
        sub(x,y)
    elif z=="*":
        mul(x,y)
    elif z=="/":
        div(x,y)
    else:
        print("You are naughty!!!")
def add(x,y):
    print(x+y)
    return x+y
def sub(x,y):
    print(x-y)
    return x-y
def mul(x,y):
    print(x*y)
    return x*y
def div(x,y):
    if y==0:
        print("NO!")
        return 0
    else:
        print(x/y)
    return x/y'''
with open("T4_9_23.py",'w+') as f:
    f.write(a1)
import T4_9_23
T4_9_23.aaa()
TTT(4)



###T5###
TTT(5)
def aaa(lst):
    a=lst[0]
    for i in lst:
        if a>i:
            a=i
    return a
print(aaa([5,9,3,0,15,42,58,96,58,74,12,2,36,58,74,92,54,11,22,44,75,96,-9,-52]))
TTT(5)
######

input("cls:")
os.system('cls')
####ketang

###T1###
TTT(1)
def aaa():
    a=input("name:")
    b=int(input("age:"))
    if b>=100:
        c=b-100
        print('You are good! ',end='When ')
        print(c,end=" year ago, you are 100!")
    elif b<100:
        c=100-b
        print(a,end=" in ")
        print(c,end=" will 100 year")
aaa()
TTT(1)


###T2###
TTT(2)
def aaa():
    b=int(input("int:"))
    print("It %2==0") if b%2==0 else print("It %2==1")
aaa()
TTT(2)


###T3###
TTT(3)
lst=[0,False,'0',8,0.0,[]]
def aaa(n):
    return n==False
a=list(filter(aaa,lst))
print(a)
print("it is first.")

def aaa(lst):
    con=1
    for i in lst:
        if i== False:
            if con==1:
                print("[",end="")
            if con!=1:
                print(", ",end="")
            print(i,end="")
            con+=1
    print("]")
    print("it is second.")
aaa(lst)

def aaa(lst):
    lt=[i==False for i in lst]
    print(lt)
    print("it is third.")
aaa(lst)
TTT(3)


###T4###
TTT(4)
lst=list(range(1,11))
def aaa(lst):
    lt=[i**2 for i in lst]
    return lt
lt=aaa(lst)
print(lst)
print(lt)
print("it is first")

def aaa(lst):
    lt=list(map(lambda x:x**2,lst))
    return lt
lt=aaa(lst)
print(lst)
print(lt)
print("it is second")
TTT(4)


###T5###
TTT(5)
from functools import reduce
lst=range(1,101)
def aaa(lst):
    return reduce(lambda x,y:x+y,lst)
a=aaa(lst)
print(a)
TTT(5)


###T6###
TTT(6)
lst=range(1,11)
def aaa(lst):
    lt=[i**3 for i in lst]
    return lt
lt=aaa(lst)
print(list(lst))
print(lt)
TTT(6)


###T7###
TTT(7)
lst1=list(range(1,11))
lst2=list(range(5,15))
def aaa(lst1,lst2):
    lst3=set(lst1)&set(lst2)
    return list(lst3)
lst3=aaa(lst1,lst2)
print(lst1)
print(lst2)
print(lst3)
TTT(7)


###T8###
TTT(8)
def aaa(q,w,e):
    max=0
    if q>=w:
        max=q
    if w>q:
        max=w
    if e>max:
        max=e
    return max
biggest=aaa(1,2,3)
print(biggest)

def aaa(q,w,e):
    return max(q,w,e)
biggest=aaa(8,2,3)
print(biggest)
TTT(8)
"""
with open("the_3_week.py",'w+') as f:
    f.write(str1)
import the_3_week


input("cls:")
os.system('cls')

str1="""def TTT(T):
    print("------------------\tT",T,"\t------------------",sep='')
import os
TTT(1)
print('hello,world'.replace('l','*'))
TTT(1)

TTT(2)
print (('Good'.lower()+'!')*3)
print ((('Good'.replace('G','g')).replace('d','d!'))*3)
TTT(2)

TTT(3)
print('FhlqoWe92Qbvc'.swapcase())
TTT(3)

TTT(4)
a='Fh1qoWe92Qbvc'
b=''
for c in a:
    if c.isdigit():
        b+=c

print(b)
TTT(4)

TTT(5)
print(sorted([2,0,3,6,9]))
TTT(5)

TTT(6)
l=[2,3,1,2,4,3]
print(list(set(l)))
TTT(6)

TTT(7)
l='aasdebbcaa'
a={}
for i in set(l):
    a[i]=l.count(i)
print(a)
TTT(7)

TTT(8)
def number():

    str_num=input("input:")
    count1=0
    count2=0
    count3=0
    count4=0
    for i in str_num:
        if i.isdigit():
            count1+= 1
        elif i.isalpha():
            count2+=1

        elif i.isspace():
            count3 += 1
        else:

            count4+=1

    print("the num is ",count1)
    print("the zimu is ",count2)

    print("the kongge is ",count3)

    print("the qita is ",count4)

number()
TTT(8)

TTT(9)
def number():

    a=input("input:")
    print(''.join([i for i in a if not a.isspace()]))
number()
TTT(9)

TTT(10)
import random
i = 1
a = random.randint(0,100)
b = int(input('input:'))
while a != b:
    if a > b:
        print('so small')
        b = int(input('input:'))
    else:
        print('so big')
        b = int(input('input:'))
    i+=1
else:
    print(i,b)
TTT(10)
input("cls:")
os.system('cls')
TTT(1)
def abc():
    for i in range(1,10):
        for l in range(1,10):
            if l<=i:
                print(l,'*',i,'=',i*l,end="\t",sep='')
                #if(print(l,'*',i,'=',i*l,end=''))==1 * 1 = 1
                #so you can add sep=''
        print('')
abc()
TTT(1)

TTT(2)
def abc():
    for i in range(0,100):
        print(i,end='')
        if i%3==0 and i%5!=0:
            print("Fizz")
        elif i%3!=0 and i%5==0:
            print("Buzz")
        elif i%3==0 and i%5==0:
            print("FizzBuzz")
        else:
            print("")
abc()
TTT(2)

TTT(3)
def aaa():
    nterms=int(input("input:"))
    n1=0
    n2=1
    nth=n1+n2
    if nterms<=0:
        print("Place scanf >0")
    elif nterms==1:
        print(n1)
    else:
        print(n1,end=",")
        print(n2,end=",")
        while nth<nterms:
            print(nth,end=",")
            n1=n2
            n2=nth
            nth=n1+n2
        print('')
aaa()
TTT(3)
"""
with open("the_2_week.py",'w+') as f:
    f.write(str1)
import the_2_week