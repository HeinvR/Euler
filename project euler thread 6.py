sumofsquares = 0
sum = sum([*range(0,101)])
squareofsum = sum * sum

for int in range(1,101):
    intsquare = int * int
    sumofsquares += intsquare

result = squareofsum - sumofsquares
print(result)