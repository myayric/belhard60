# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами
#
name = input("Please enter your name: ")
age = input("Please enter your age: ")
city = input("Please enter your city: ")

# The first method
print(f"1-- Dear friend {name} you have {age} years old, so welcome to the city of {city}.")

# The second method
print("2-- Dear friend %s you have %s years old, so welcome to the city of %s." % (name, age, city))

# The third method
total = '3-- Dear friend ' + name + 'you have ' + age + ' years old, so welcome to the city of ' + city + '.'
print(total)

# The fourth method
print("4-- Dear friend %(name)s you have %(age)s years old, so welcome to the city of %(city)s."
      "" % {"name": name, "age": age, "city": city})
