import sympy
primenumbers = []

for i in range(0,2000001):
    if sympy.isprime(i):
        primenumbers.append(i)
        
print(sum(primenumbers))