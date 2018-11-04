from concurrent.futures import ThreadPoolExecutor,as_completed
from concurrent.futures import ProcessPoolExecutor
import time
import asyncio
def TTT(T):
    print("-"*8,"\tT",T,"\t","-"*8,sep='')
def my():
    lst=[]
    for i in range(26,36):
        lst.append(i)
    yield lst
def fib(n):
    if n<=2:
        return 1
    return fib(n-2)+fib(n-1)
if __name__=='__main__':
    TTT(1)
    sui=my().__next__()
    with ProcessPoolExecutor(max_workers=3) as executor:
        for num,result in zip(sui,executor.map(fib,sui)):
            print("fib(",num,")=",result,sep="")


    TTT(2)
    async def g1():
        for i in range(10):
            yield i
    async def g2():
        async for v in g1():
            print(v)
        return [v*2 async for v in g1()]
    loop=asyncio.get_event_loop()
    result=loop.run_until_complete(g2())
    print(f'Result is {result}')