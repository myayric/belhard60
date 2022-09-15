# #Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры


slov = input("Enter your sentence:  ")
slov2 = slov.replace(" ", "")
Result = [slov2.lower()[i] for i in range(0, len(slov2))]
num_slov = {Result[i]: Result.count((Result[i])) for i in range(0, len(slov2))}
print(num_slov)
