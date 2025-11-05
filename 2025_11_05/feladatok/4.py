'''

4. Feladat
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja,
és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó! 
'''
'''
words = []

def shortest(word1, word2, word3):
    length1 = len(word1)
    words.append(word1)
    length2 = len(word2)
    words.append(word2)
    words.append(word3)
    length3 = len(word3)

    if length1 < length2 and length1 < length3:
        print(f'{length1} karakter hosszú {word1}')
    
    elif length2 < length1 and length2 < length3:
        print(f'{length2} karakter hosszú {word2}')

    elif length3 < length1 and length3 < length2:
        print(f'{length3} karakter hosszú {word3}')

useri1 = input('Give me a word!\n')
useri2 = input('Give me another word!\n')
useri3 = input('Give me another word!\n')

shortest(useri1, useri2, useri3)
'''

szavak = []

szo1 = input('Adj meg egy szót! \n')
szo2 = input('Adj meg egy szót! \n')
szo3 = input('Adj meg egy szót! \n')

szavak.append(szo1)
szavak.append(szo2)
szavak.append(szo3)

def legrovidebb_szo_kereso(str_listaja):
    legrovidebb = len(str_listaja[0])
    legrovidebb_szo = str_listaja[0]
    for szo in str_listaja:
        if len(szo) < legrovidebb:
            legrovidebb = len(szo)
            legrovidebb_szo = szo
    print(f'a legrövidebb szó: {legrovidebb_szo}. Karakterszama: {(legrovidebb)}')

legrovidebb_szo_kereso(szavak)