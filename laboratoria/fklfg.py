def policz_znaki(napis, znak):
    licznik = 0
    for ch in napis.lower():
        if ch == znak.lower():
            licznik += 1
    return licznik

print(policz_znaki('Ala ma kota', 'a'))
