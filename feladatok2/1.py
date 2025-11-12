'''
1. Feladat
Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt,
ami a paraméterként átvett listaelemeket (egész számokat) összeadja és az összegükkel tér vissza!
A program tartalmazza a függvény hívását is!
'''

szamlista = [1, 6, 3, 5, 6, 2, 7]

def osszegzo (szamok):
    osszegek = 0
    for i in szamok:
        osszegek += i
    print(osszegek)

osszegzo(szamlista)
    