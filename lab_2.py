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


def f3():
    for x in range(45000000, 50000001):
        p = x
        while p % 2 == 0:
            p = p//2
        if (p ** 0.25) == int(p ** 0.25):
            z = 0
            for i in range(2, int(p ** 0.5)):
                if p % i == 0:
                    if i % 2 == 1:
                        z += 1
            if z == 1:
                print(x)


f1()
f2()
f3()
