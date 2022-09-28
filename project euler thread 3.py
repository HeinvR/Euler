import math
import sympy

primes = []
number = int(math.sqrt(600851475143))

for i in range(0, number):
    if sympy.isprime(i):
        if 600851475143 % i == int(0):
            primes.append(i)

print("Highest prime factor of 600851475143 is:", primes[-1])