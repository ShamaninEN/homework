proceeds = int(input('введите выручку: '))
costs = int(input('введите расходы: '))
# workers = input('Численность предприятия: ')
if proceeds > costs:
    # print('у вас прибыль')
    profit = proceeds - costs
    print(f'Ваша рентабильность выручки: {profit/proceeds}')
    workers = int(input('Численность работников: '))
    print(f'Прибыль на одного сотрудника: {profit / workers}')
else:
    print('У вас убыток')

