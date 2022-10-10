n = 100
product = 100
sum = 0

# get result of 100!
while n > 1:
    product *= (n - 1)
    n -= 1

# add sum of digets
for char in str(product):
    sum += int(char)

print(sum)
