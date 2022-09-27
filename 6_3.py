# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]


lst = []
num_el = int(input("Enter number of elements : "))
print('#type the numbers and press Enter#')
for i in range(0, num_el):
    ele = int(input())
    lst.append(ele)
print("Your list of numbers is \n>>>", lst)
while True:
    n = int(input(f"Choose your number between 1 to {num_el}\n>>> "))
    if n <= num_el:
        break
print(lst[len(lst) - n:] + lst[0:len(lst) - n])
