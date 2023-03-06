fibnumbers = [0]

n = 1
answer = 0

# calculate fibnumbers
def fib(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]

# loop until 1000 digits
while len(str(fibnumbers[-1])) < 1000:
    fibnumbers.append(fib(n))
    n += 1

# print result, minus 1 because fibnumbers is not empty at start time
print(len(fibnumbers)-1)