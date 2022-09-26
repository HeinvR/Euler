from sympy import *

primenumbers = []
i = 1

while len(primenumbers) < 10001:
    if isprime(i):
       primenumbers.append(i)
       print("added " + str(i))
    i += 1

print(str(primenumbers[10000]))