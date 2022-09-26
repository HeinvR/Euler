import math

currenttriangle = 1
highestfractures = 0


def getnexttrianglenumber(number):
    return number * (number + 1) // 2


def getnumberofdivisors(number):
    counter = 0
    i = 1
    while i <= math.sqrt(number):
        if number % i == 0:
            if number / i == i:
                counter += 1
            else:
                counter += 2
        i += 1
    return counter


while True:
    num = getnexttrianglenumber(currenttriangle)
    fractures = getnumberofdivisors(num)
    if fractures >= highestfractures:
        highestfractures = fractures
        print("New highest number of fractures found! Triangle number", num, "has", fractures, "fractures")
    currenttriangle += 1
    if fractures > 500:
        print("Result found! First triangle number with more dan 500 fractures is:", num, "with", fractures, "fractures")
        break
