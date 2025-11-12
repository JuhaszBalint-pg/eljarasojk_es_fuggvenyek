'''
3.1 Feladat
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt,
amely a paraméterként átvett listában megvizsgálja,
hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza!
A program tartalmazza a függvény hívását is!
'''

szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def harommal_oszthatok(listám):
    oszthatok = 0
    for i in listám:
        if i % 3 == 0:
            oszthatok += 1
    
    print(oszthatok)

harommal_oszthatok(szamok)