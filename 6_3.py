# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]


lst = [1, 2, 3, 4, 5, 6, 7]
number = int(input("Ведите число: "))
print(lst[len(lst)-number:] + lst[0:len(lst)-number])