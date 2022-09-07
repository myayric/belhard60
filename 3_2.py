# Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3

fnum = float(input('First number is: '))
snum = float(input('Second number is: '))
tnum = float(input('Third number is: '))
result = (fnum + snum + tnum) / 3
print(round(result, 3))
