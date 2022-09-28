fibnumbers = [0]

n = 1
answer = 0


# calculate fibnumbers
def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    else:
        n = fib(n-1) + fib(n-2)
    return n


# populate fibnumbers collection
while fibnumbers[-1] < 4000000:
    fibnumbers.append(fib(n))
    n += 1

# calculate sum of even-valued fibnumbers
for i in range(0, len(fibnumbers)):
    if fibnumbers[i] % 2 == 0:
        answer += fibnumbers[i]

print(answer)
