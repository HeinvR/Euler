numbers = [*range(1,21,1)]
i = 1

while i < 1000000000:
    result = all(i % number == 0 for number in numbers)
    if result:
        print(str(i) + " is deelbaar door 1 t/m 20")
    i += 1