palindromes = []

for a in range(100, 1000):
    for b in range(100, 1000):
        strab = a * b
        if str(strab) == str(strab)[::-1]:
            palindromes.append(strab)

print(max(palindromes))
