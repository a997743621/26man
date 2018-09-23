def TTT(T):
    print("")
    print("")
    print("")
    print("T",T,end="\t")
    print("T",T,end="\t")
    print("T",T,)
###T1###
TTT(1)
def aaa():
    a=input("name:")
    b=int(input("age:"))
    if b>=100:
        c=b-100
        print("You are good!\n",end="When ")
        print(c,end=" year ago, you are 100!")
    elif b<100:
        c=100-b
        print(a,end=" in ")
        print(c,end=" will 100 year")
aaa()



###T2###
TTT(2)
def aaa():
    b=int(input("int:"))
    if b%2==0:
        print("It is %2==0")
    elif b%2==1:
        print("It is %2==1")
aaa()



###T3###
TTT(3)
lst=[0,False,'0',8,0.0,[]]
def aaa(n):
    return n==False
a=list(filter(aaa,lst))
print(a,"\nit is first.")

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
    print("]\nit is second.")
aaa(lst)

def aaa(lst):
    lt=[i==False for i in lst]
    print(lt,"\nit is third.")
aaa(lst)



###T4###
TTT(4)
lst=list(range(1,11))
def aaa(lst):
    lt=[i*i for i in lst]
    return lt
lt=aaa(lst)
print(lst,"\n",lt,"\nit is first")

def aaa(lst):
    lt=list(map(lambda x:x*x,lst))
    return lt
lt=aaa(lst)
print(lst,"\n",lt,"\nit is second")



###T5###
TTT(5)
from functools import reduce
lst=range(1,101)
def aaa(lst):
    return reduce(lambda x,y:x+y,lst)
a=aaa(lst)
print(a)



###T6###
TTT(6)
lst=range(1,11)
def aaa(lst):
    lt=[i*i*i for i in lst]
    return lt
lt=aaa(lst)
print(list(lst),"\n",lt)



###T7###
TTT(7)
lst1=list(range(1,11))
lst2=list(range(5,15))
def aaa(lst1,lst2):
    lst3=set(lst1)&set(lst2)
    return list(lst3)
lst3=aaa(lst1,lst2)
print(lst1,"\n",lst2,"\n",lst3)



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
