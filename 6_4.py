# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка незаконно

spis = [1, 3, 'fish', None, "mori", 54, "my"]
spis = list(filter(lambda i: isinstance(i, str), spis))
print(spis)