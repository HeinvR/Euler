higheststeps = 1


def getsteps(num):
    steps = [num]

    def calculatesteps(number):
        if number != 1:
            if number % 2 == 0:
                number = int(number / 2)
                steps.append(number)
                calculatesteps(number)
            else:
                number = number * 3 + 1
                steps.append(number)
                calculatesteps(number)
        return steps
    return len(calculatesteps(num))


for n in range(1, 1000001):
    steps = getsteps(n)
    if steps >= higheststeps:
        higheststeps = steps
        print("Higher steps found!", n, "has", steps, "steps")
