abundant_numbers = []
abundant_sums = []
non_abundant_numbers = []

# function to check if number is abundant
def check_abundant(n):
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    if sum_of_divisors > n:
        return True

# Get abundant numers, put them in list
for i in range(1, 28124):
    if check_abundant(i):
        abundant_numbers.append(i)

# get abundant sums, put them im list
for a in abundant_numbers:
    for b in abundant_numbers:
        ab = a + b
        if ab > 28123:
            break
        else:
            abundant_sums.append(ab)

# get ints not in abundant sums list
for n in range(1, 28124):
    if n not in abundant_sums:
        non_abundant_numbers.append(n)

# print result
print(sum(non_abundant_numbers))



