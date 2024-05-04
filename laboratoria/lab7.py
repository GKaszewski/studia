l = [1,2.25,3.14,3.75,4, {'hej': 'a'}]
print('for')
for element in l:
    print(element) 

print('while')

i = 0
while i < len(l):
    print(l[i])
    i += 1

print('fddf')
for i,e in enumerate(l):
    print(f'i: {i}, e: {e}')