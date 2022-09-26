from num2words import num2words

result = 0
for num in range(1, 1001):
    result += len(''.join(''.join(num2words(num).split(' ')).split('-')))

print(result)
