# Пользователь вводит 3 числа, сказать сколько из них
# положительных  и сколько отрицательных

first_num = input("Please enter the first number: ")
second_num = input("Please enter the second number ")
third_num = input("Please enter the third number ")
zero_num = first_num.count('0') + second_num.count('0') + third_num.count('0')
neg_num = first_num.count('-') + second_num.count('-') + third_num.count('-')
pos_num = 3 - zero_num - neg_num
print("Number of negative numbers is: ", neg_num)
print("Number of positive numbers is: ", pos_num)
print("Zero Number have: ", zero_num)
