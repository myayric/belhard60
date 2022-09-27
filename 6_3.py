# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]


my_list = [1, 2, 3, 4, 5, 6, 7]
n = int(input("Choose your number between 1 and 7\n >>> "))
print(my_list[len(my_list) - n:] + my_list[0:len(my_list) - n])
