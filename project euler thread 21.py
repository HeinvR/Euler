#collect amibles
amiclepairs = []

#function to get sum of divisors
def sum_of_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return(sum(divisors))

# loop to find amicles, add them to collection
for i in range(1, 10001):
    sumof = sum_of_divisors(i)
    amicle = sum_of_divisors(sumof)
    
    if i == amicle:
        if sumof != amicle:
            print(i, sumof, amicle)
            amiclepairs.append(i)
            amiclepairs.append(sumof)

#print result divide by two to remove doubles
print(sum(amiclepairs) / 2)