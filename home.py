name = input("name: ")
name = name.title()
surename = (surename.title(input("surname: ")))
#surename = surename.title()
age = int(input("age: "))
if age >= 120:
    print(f'Mr {name} {surename}, you are joking.\nyou are dead)).')
elif age >= 80:
    print(f"hello {name} {surename} you are very old for this ")
elif age >= 18:
    print(f"hello {name} {surename}.\nwelocome.")
else:
    age2 = str(18 - age)
    print(f"hello {name} {surename}. you can come back after {age2} years.")
# fullname = 'mori, zangi,'
# print(fullname)
# fullname.split(", ")
# print(fullname)
# nofull = fullname.join("--")
# print(nofull)

# text = 'Love thy  neighbor'
# # # разделяем строку
# # print(text.split( ))
# # grocery = 'Milk, Chicken, Bread'
# # # разделяем запятой
# # print(grocery.split('. '))
# # # разделяем двоеточием
# # print(grocery.split(':'))
# # text2 = (text.join(''))
# # print(text2)
#
# print(text.find('t'))
# print(text.rfind("j"))
# print(text.index("t"))
# print(text.rindex("b"))
# text2 = text.split()
# text3 = text2
# print(text2)
# # text2.replace('love', 'notlove')
# print(text2)
# print(text.isdigit())
# print(text.isspace())
# print(text.isalpha())
# print(text.isalnum())
# print(text.isidentifier())
# print(text.isprintable())
# print(text.isascii())
# print(text.startswith('Love'))
# print(text.endswith('h'))
# print(text.islower())
# print(text.upper())
# print(text.lower())
# print(text.capitalize())
# j = text.title()
# print(j)
# print(text.title())