from itertools import product

def f1():
    counter = 0
    for i in product("ABCDXYZ", repeat=4):
        if(i[0] in "XYZ") and (i.count("X") + i.count("Y") + i.count("Z") == 1):
            counter+=1
    print(counter, "\n")

def f2():
    x = 9**8 + 3**5 - 9
    s = ''
    while x != 0: 
        s += str(x % 3)
        x //= 3
    s = s[::-1]
    print(s.count("2"), "\n")



def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:          
            return False
    return True

def f3():
    primes = set()
    for i in range(3, int(50000000**0.25) + 1):
        if prime(i):
            primes.add(i)
    for i in range(45000000, 50000001):
        p = i
        while p % 2 == 0:
            p //= 2
        if int(p**0.25) in primes and (int(p**0.25))**4 == p:
            print(i)

f1()
f2()
f3()