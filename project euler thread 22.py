total_Score = 0

# get sorted names list from txt file
with open("project euler thread 22.txt") as f:
    names = f.read().replace('"', "").split(",")
names.sort()

for name in names:
    number_in_list = names.index(name) + 1
    name_value = 0
    for char in name:
        name_value += (ord(char) - 64)
    total_Score += number_in_list * name_value

print(total_Score)