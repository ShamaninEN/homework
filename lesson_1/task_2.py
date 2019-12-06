value = int(input('введите количество секунд: '))
hours = value // 3600
minutes = (value % 3600) // 60
seconds = (value % 3600) % 60
print(f'Выводим в формате чч:мм:сс, {hours}:{minutes}:{seconds}')
