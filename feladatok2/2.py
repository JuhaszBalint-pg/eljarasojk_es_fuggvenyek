'''
2. Feladat
Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza,
ha a paraméterként átvett listaelemek (egész számok) között van páros,
ellenkező esetben a visszatérési érték False! A program tartalmazza a függvény hívását is!
'''
szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
paratlanszamok = [1, 3, 5, 7, 9]

def paros_e(mylist):
    specelem = 0
    for i in mylist:
        if i % 2 == 0:
            specelem = True
        
    if specelem == True:
        print('Van legalább egy páros szám a listában!')
    else:
        print('Nincsen páros szám a listában')

paros_e(szamok)

paros_e(paratlanszamok)
     