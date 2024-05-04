from collections import Counter
print(dict(Counter('dupa')))
#string = input("Podaj napis: ")

# print(f'Wystapienia litery "a": {string.lower().count("a")}')
# print(f'Wystapienia litery "a": {Counter(string.lower())["a"]}')


def policzenie_literek(string):
    literki = {}
    for ch in string:
        if ch in literki.keys():
            literki[ch] += 1
        else:
            literki[ch] = 1
    print(literki)


#policzenie_literek('dupaaaaaaa')