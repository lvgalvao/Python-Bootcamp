import re
with open('tabacaria.txt') as f:
    text = f.read()


print(text)
# print(re.findall(r'.olha', text))

print(type(re.findall(r'[O|o]lha', text)))