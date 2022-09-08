# Пользователь вводит 3 числа, сказать сколько из них
# положительных  и сколько отрицательных

first_num = input("Please enter the first number: ")
second_num = input("Please enter the second number ")
third_num = input("Please enter the third number ")

zero_num = float(first_num) == 0 + float(second_num == 0) + float(third_num) == 0
neg_num = first_num.count('-') + second_num.count('-') + third_num.count('-')
pos_num = 3 - zero_num - neg_num
print("Number of negative numbers is: ", neg_num)
print("Number of positive numbers is: ", pos_num)
print("Zero Number have: ", int(zero_num))
