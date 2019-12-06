value = input('введите целое положительное число: ')
big_value = 0
i = 0
while i < len(value):
    if big_value < int(value[i]):
        big_value = int(value[i])
    i = i + 1
print(big_value)