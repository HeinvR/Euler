coll = []

# read lines from textfile and add them to collection
with open("project euler thread 18.txt", encoding='utf-8') as f:
    for line in f:
        coll.append(line.split(" "))

# strip newlines and convert to int
for line in coll:
    line[-1] = line[-1].strip()
    for element in range(0, len(line)):
        line[element] = int(line[element])


def getmaximumtotal(dictionary):
    # reverse dictionary
    rvdict = dictionary[::-1]
    # iterate to rvdict

    for l in range(1, len(rvdict)):
        if len(rvdict[l]) > 1:
            for n in range(0, len(rvdict[l])):
                templist = rvdict[l-1][n:n+2]
                rvdict[l][n] += max(templist)
        else:
            templist = rvdict[l-1][0:2]
            rvdict[l][0] += max(templist)
            return rvdict[l][0]


print(getmaximumtotal(coll))


