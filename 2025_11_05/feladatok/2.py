'''
2. Feladat
Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e! 
'''
fut = True


def neg_vagy_poz (szam):
    if szam > 0:
        print (f'a {szam} pozitív')
    else:
        print (f'a {szam} negaív')

useri = int(input('Adj meg egy számot! '))

neg_vagy_poz(useri)

