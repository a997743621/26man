def aaa():
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
    return x/y