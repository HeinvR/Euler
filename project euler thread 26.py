repeat_length = 0
answer = 2

def count_decimals(number):
    cycle_list = [10]
    while ((cycle_list[-1]) % number) * 10 not in cycle_list:
        cycle_list.append((cycle_list[-1] % number) * 10)

    return len(cycle_list)-cycle_list.index((cycle_list[-1] % number) * 10)

for i in range(2, 1001):
    if count_decimals(i) >= repeat_length:
        repeat_length = count_decimals(i)
        answer = i

print(answer)