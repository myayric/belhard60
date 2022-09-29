# # file = open('input.txt', 'r+', encoding='utf-8')
# # # lines = file.readlines()
# # # test = file.read()
# # file.write('\n privet ')
# # lines = [line.strip() for line in file]
# # print(lines)
# # file.close()
#------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------#
# import json
# with open('input.json','r', encoding='utf-8') as file:
#     data =json.load(file)
#     print(data)
# from pydantic import BaseModel, Field, EmailStr, validator
#
# class Data(BaseModel):
#
# class User(BaseModel):
#     name: str = Field(min_length=4, max_length=10, default='mrjhi')
#     age: int
#
#
# vasya = User(name="mori", age=38)
# print(vasya)
#-------------------------------------------------------------------------------------------------------------------#
#
# import pandas
# frame = pandas.DataFrame(
#     {"name": ['mori', 'moh'],
#      'age': [23,43],
#      'city': ['minsk', 'rus']
#      }
# )
#  print(frame)
#-----------------------------------
# import yaml
# from yaml.loader import SafeLoader
#
# data = {
#     'name': 'mori',
#     'email':'mofs@lskjf',
#     'age': 45,
#     'lang': ['ru', 'fa']
# }
#-----------------------------------------------------------------------

text ='''

мобильный телефон 3000

ru от 1 шт 18000

ru от 5 шт 17000
'''

countries = ['ru', 'en', 'fr']
from_price = ['от 1', 'от 5', 'от 20', 'от 50']

data = for i in text:
