# Пользователь вводит 3 числа, сказать сколько из них
# положительных  и сколько отрицательных

first_num = float(input("Please enter the first number: "))
second_num = float(input("Please enter the second number "))
third_num = float(input("Please enter the third number "))
# Эта часть предназначена для нахождения нуля и подсчета десятичных чисел как -0,2.
zero_num = (first_num == 0) + (second_num == 0) + (third_num == 0)
neg_num = (first_num < 0) + (second_num < 0) + (third_num < 0)
pos_num = 3 - zero_num - neg_num
print("Number of negative numbers is: ", neg_num)
print("Number of positive numbers is: ", pos_num)
print("Zero Number have: ", int(zero_num))
