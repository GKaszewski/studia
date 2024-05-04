"""
for i in range(1,6):
    for j in range(1,6):
        print(f'{i}*{j} = {i*j}')
"""

# i = 1
# while i <= 5:
#     j = 1
#     while j <= 5:
#         print(f'{i}*{j} = {i*j}')
#         j+=1
#     i+=1

# i = 1
# j = 1
# while i <= 5:
#     j = 1
#     while j<=5:
#         wynik = i * j
#         print(str(i) + "*" + str(j) + "=" + str(wynik))
#         j += 1
#     i = i + 1


for i in range(6):
    for j in range(6):
        print(str(i) + "*" + str(j) + "=" + str(i*j))
