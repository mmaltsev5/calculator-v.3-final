import time
print('Добро пожаловать в Калькулятор')
while True:
    x = int(input('Введите первое число>> '))
    znak = input('Действие(+  -  /  *  %)>> ')
    y = int(input('Введите второе число>>  '))
    if znak == "+":
        result = x + y
        print(f'Результат: {result}')
        time.sleep(2)
        p = input('Вы хотите продолжить работу с калькулятором?(1 если Да, 2 если Нет)>> ')
        if p == '2':
            print('Спасибо за работу!')
            time.sleep(1)
            break
    elif znak == "-":
        result = x - y
        print(f'Результат: {result}')
        time.sleep(2)
        p = input('Вы хотите продолжить работу с калькулятором?(1 если Да, 2 если Нет)>> ')
        if p == '2':
            print('Спасибо за работу!')
            time.sleep(1)
            break
    elif znak == '/':
        result = x / y
        print(f'Результат: {result}')
        time.sleep(2)
        p = input('Вы хотите продолжить работу с калькулятором?(1 если Да, 2 если Нет)>> ')
        if p == '2':
            print('Спасибо за работу!')
            time.sleep(1)
            break
    elif znak == '*':
        result = x * y
        print(f'Результат: {result}')
        time.sleep(2)
        p = input('Вы хотите продолжить работу с калькулятором?(1 если Да, 2 если Нет)>> ')
        if p == '2':
            print('Спасибо за работу!')
            time.sleep(1)
            break
    elif znak == '%':
        result = x % y
        print(f'Результат: {result}')
        time.sleep(2)
        p = input('Вы хотите продолжить работу с калькулятором?(1 если Да, 2 если Нет)>> ')
        if p == '2':
            print('Спасибо за работу!')
            time.sleep(1)
            break
    else:
        print('Неверное значение. Повторите попытку.')
        print()
