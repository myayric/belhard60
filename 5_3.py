# Вывести четные числа от 2 до N по 5 в строку

num = int(input("Enter the number: "))
ent = 0
for i in range(2, num + 1):
    if not i % 2 and ent < 5:
        print(i, end=" ")
        ent += 1
    elif ent == 5:
        print()
        ent = 0
