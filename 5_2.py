# Сделать калькулятор:
# у пользователя спрашивается число, потом действие и второе число

num_1 = float(input('Введите первое число: '))
act = input("Какую операцию нужно произвести над числом?  выбрите между (+, -, /, *) :")

while act != '+' and act != '-' and act != '/' and act != '*':
    act = input("не правильное дествие:выбрите между (+, -, /, * ) :")
    print(bool(act))
else:
    num_2 = float(input('Введите второе число: '))

if act == '-':
    print(f'Ответ на вычитание двух чисел {num_1} и {num_2} = {num_1 - num_2}')
elif act == "+":
    print(f'Ответ на сложение двух чисел {num_1} и {num_2} = {num_1 + num_2}')
elif act == "/":
    print(f'Ответ на деление двух чисел {num_1} и {num_2} = {num_1 / num_2}')
elif act == "*":
    print(f'Ответ на умножение двух чисел {num_1} и {num_2} = {num_1 * num_2}')
