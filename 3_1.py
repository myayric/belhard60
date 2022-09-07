# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами


text = input("Type the text: ")
spl1 = text.split()
print("The first method is :", "_".join(spl1))
text2 = text.replace(" ", "_")
print("The second method is :", text2)
