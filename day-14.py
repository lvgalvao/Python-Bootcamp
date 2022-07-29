#create a compare list

from artday14 import logo, vs
from datagameday14 import data

print(logo)
print(vs)
print(data[1].items())

for e in data:
    for k,v in e.items():
        print(f'{k} e {v}')

    
