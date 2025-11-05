'''
3. Feladat
Írj eljárást, amely paraméterül kapott 2 számot összehasonlít, és a képernyőre kiírja, melyik a nagyobb szám! Kezeld azt az esetet is, ha a két szám egyenlő! 
'''

def comparison(num1, num2):
    if num1 > num2:
        print ('The first given number is greater')
    
    elif num1 < num2:
        print ('The second given number is greater')

    else:
        print('The two given number are even')

useri1 = input('give me a number ')
useri2 = input('give me another number ')

comparison(useri1, useri2)