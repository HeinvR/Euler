for a in range(1, 999):
    for b in range(1, 999):
        if a < b:
            ab = a ** 2 + b ** 2
            for c in range(1, 999):
                if c ** 2 == ab:
                    if a + b + c == 1000:
                        answer = a * b * c
                        print("het antwoord is " + str(answer))
