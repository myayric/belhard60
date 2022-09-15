# Заполнить список степенями числа 2 (от 2^1 до 2^n).
number = int(input("Enter the number: "))
num = [i * 2 for i in range(1, number + 1)]
print(num)
print("sum: ", sum(num))
