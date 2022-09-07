# Пользователь вводит 3 числа, сказать сколько из них
# положительных  и сколько отрицательных

first_num = input("Please enter the first number: ")
second_num = input("Please enter the second number ")
third_num = input("Please enter the third number ")
neg_num = first_num.count('-') + second_num.count('-') + third_num.count('-')
pos_num = 3 - neg_num
print("Number of negative numbers is: ", neg_num)
print("Number of positive numbers is: ", pos_num)
