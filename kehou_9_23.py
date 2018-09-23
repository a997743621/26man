def TTT(T):
    print("")
    print("")
    print("")
    print("T",T,end="\t")
    print("T",T,end="\t")
    print("T",T,)
###T1###
TTT(1)
import random
def aaa(is_number,is_letter,is_symbol):
    mima=''
    a=0
    b=0
    c=0
    if is_number:a=int(input("number has "))
    if is_letter:b=int(input("letter has "))
    if is_symbol:c=int(input("symbol has "))
    if a>0:
        for i in range(a):
            l=random.randint(0,9)
            mima+=str(l)
    if b>0:
        for i in range(b):
            big_or_small=2
            big_or_small=random.randint(0,1)
            if big_or_small==0:
                l=random.randint(65,90)
            if big_or_small==1:
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

    password=list(mima)
    random.shuffle(password)
    password=''.join(password)

    print("It is your password!")
    print(password)
def hahaha():
    a=input("Do you need number?yes or no\n")
    b=input("Do you need letter?yes or no\n")
    c=input("Do you need symbol?yes or no\n")
    aa=0;bb=0;cc=0
    if a=='yes':
        aa=1
    if b=='yes':
        bb=1
    if c=='yes':
        cc=1
    if aa==0:
        if bb==0:
            if cc==0:
                print("You are naughty!!!")
                return 0;
    aaa(aa,bb,cc)
hahaha()



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



###T4###
TTT(4)
import T4_9_23
T4_9_23.aaa()



###T5###
TTT(5)
def aaa(lst):
    con=0
    for i in lst:
        con+=1
        if con==1:
            a=i
        if a>i:
            a=i
    return a
print(aaa([5,9,3,0,15,42,58,96,58,74,12,2,36,58,74,92,54,11,22,44,75,96,-9,-52]))