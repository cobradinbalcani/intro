'''Pentru toate exercitiile
Apelati functia de cel putin 2 ori cu valori diferite pentru a testa
Daca functia are return, printati raspunsul'''

import math

from datetime import datetime

from datetime import date
import calendar
from calendar import monthrange


def print_spatiu():
    print('------------------------------')


# printSpatiu()

# b. Dificultate: usor spre mediu

# 1.Functie care sa calculeze si sa returneze suma a 2 numere

def calcul_Two(x, y):
    return f'Suma dintre cele doua nr este: {x + y}'


print(calcul_Two(4, 1))
print(calcul_Two(6, -2))

print_spatiu()


# 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

def Par_Impar(nr):
    if nr % 2 == 0:
        return True
    else:
        return False


print(Par_Impar(4))
print(Par_Impar(5))

print_spatiu()


# 3. Functie care returneaza numarul total de caractere din numele tau complet. (nume, prenume, nume_mijlociu)

def nr_Tot_Char(numele_meu):
    # return str(len(numele_meu))                    # varianta care ia in calcul spatiile
    return str(len(numele_meu.replace(' ', '')))  # varianta care nu ia in calcul spatiile


print(nr_Tot_Char('Ilie Adrian Marius'))
print(nr_Tot_Char('numele meu'))
print_spatiu()


# 4. Functie care returneaza aria dreptunghiului

def aria_D(a, b):
    return f'Aria dreptunghiului este: {a * b}'


a = abs(int(input('Introdu latimea: ')))
b = abs(int(input('Introdu Lungimea: ')))
print(aria_D(a, b))

print_spatiu()


# 5. Functie care returneaza aria cercului

def aria_C(r):
    return f'atunci Aria cercului este: {(r * r) * math.pi}'


r = abs(int(input('Daca valoarea razei este: ')))

print(aria_C(r))

print_spatiu()


# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu

def char_X(string):
    if '3' in string:
        return True
    else:
        return False


print(char_X('r3*'))
print(char_X('r4*'))

print_spatiu()


# 7. Functie fara return, primeste un string si printeaza pe ecran:
# -	Nr de caractere lower case este x
# -	Nr de caractere upper case exte y


def fara_Return(x):
    lower = 0
    upper = 0
    not_alpha = 0
    for y in x:
        if y.isupper():
            upper += 1

        elif y.islower():
            lower += 1
        else:
            not_alpha += 1

    print(
        f'Nr de caractere upper este: {upper}; nr de lower este: {lower}, iar nr de altfel de caractere este: {not_alpha}.')


fara_Return(' PIZZA-4-stagioni ')
print(fara_Return('McDonalds'))
print_spatiu()


# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive


def pozitive(nr):
    nr_pozitiv = []
    for i in nr:
        if i > 0:
            nr_pozitiv.append(i)
    return nr_pozitiv


print(pozitive([2, -2, 4, -6, 0, 93]))
print(pozitive([-1, 4, 44, -46, 10, 193]))

print_spatiu()
'''9. Functie care nu retunraza nimic. Primeste 2 numere si PRINTEAZA
-	Primul numar x este mai mare decat al doilea nr y
-	Al doilea nr y este mai mare decat primul nr x
-	Numerele sunt egale.'''


def doua_NR(x, y):
    if x > y:
        print(f'{x} este mai mare ca {y}')
    elif y > x:
        print(f'{y} este mai mare ca {x}')
    else:
        print(f'Cele 2 nr sunt egale.')


doua_NR(5, 4)
doua_NR(3, 6)
doua_NR(2, 2)
print_spatiu()
'''10. Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False'''


def cu_SET(a, b):
    if a not in b:
        b.add(a)
        print('Am adaugat nr nou in set.')
        print(b)
        return True
    else:
        print('nu am adaugat numarul in set. Acesta exista deja.')
        print(b)
        return False


print(cu_SET(0, {66, -2, 3, 4, 5}))
print(cu_SET(3, {66, -2, 3, 4, 5}))

print_spatiu()


# c. Optionale (may need google)

# 11. Functie care primeste o luna din an si returneaza cate zile are acea luna

def zile_Din_Luna(luna):
    if luna in range(1, 13):
        ziua = monthrange(2024, luna)[1]
        return ziua


print(zile_Din_Luna(2))
print(zile_Din_Luna(3))

print_spatiu()
# 12. Functie calculator care sa returneze 4 valori
# Suma, diferenta, inmultirea, impartirea a 2 numere

'''In final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)'''


def calculator(x, y):  # de verificat impartirea cu zero 0

    print(x * y, ', inmultire')
    print(x + y, ', adunare')
    print(x - y, ', scadere')
    try:  # bloc de cod pt verificare de eroare
        x / y  # aici punem codul 'periculos'
    except ZeroDivisionError as m:  # tratam exceptia ZeroDivisionError (putem inlocui cu "Exception" care inglobeaza toate erorile)
        print(m)
    else:  # daca nu avem eroare, nu intra except si ajunge in else ca sa folosim codul
        print(x / y, ', impartire verificata, pentru impartirea cu zero')
    finally:  # am pus finally, care se executa indiferent daca este eroare in try sau nu
        print('am pus finally, care se executa indiferent daca este eroare in try sau nu')


calculator(10, 2)
calculator(20, 5)
print_spatiu()
'''13. Functie care primeste o lista de cifre (adica doar 0-9)
Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returneaza un DICT care ne spune de cate ori apare fiecare cifra
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}'''


def lista_Cifre(x):
    dict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
    }
    for item in x:
        if item in dict:
            dict[item] += 1
    return dict


print(lista_Cifre([1, 3, 1, 5, 9, 7, 7, 5, 5]))

print_spatiu()


# 14. Functie care primeste 3 numere.  Returneaza valoarea maxima dintre ele

def nr_Trei(x, y, z):  # rezolvare varianta 1 fara IF
    x = int(x)
    y = int(y)
    z = int(z)
    return max(x, y, z)


print(nr_Trei(2, 0, -3))

# def trei_nr(x,y,z):                    # rezolvare varianta 2, cu ajutorul lui IF
#     if (x > y and x > z) and (x != y and x != z):  # conditie ca x sa fie mai mare sau diferit fata de y si z
#         print(x, 'e cel mai mare')
#     elif (y > x and y > z) and (y != z and y != x):  # conditie ca y sa fie mai mare sau diferit fata de x si z
#         print(y, 'e cel mai mare')
#     elif (z > x and z > y) and (z != x and z != y):  # conditie ca z sa fie mai mare sau diferit fata de x si y
#         print(z, 'e cel mai mare')
#     else:
#         print('Cele 3 numere sunt egale.')  # conditie ramasa: cand toate sunt egale
#     return max(x,y,z)
#
# trei_nr(-31,-2,-3)


print_spatiu()
'''15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
Ex: daca dam nr 3
Suma va fi 6 (0+1+2+3)'''


def suma_Tot_Nr(x):
    suma_nr = (abs(x) * (abs(x) + 1)) / 2
    return abs(suma_nr)


print(suma_Tot_Nr(3))
print(suma_Tot_Nr(-6))

print_spatiu()
# BONUS:

# 16. Functie in care sa dai un nume romanesc si sa iti printeze pe ecran
# ‘Numele este de baiat’ sau ‘Numele este de fata’


# from gender_guesser import data
# from gender_guesser import detector
# import gender_guesser.detector as gender
#
#
# def Romanesc(d):
#     d = gender.Detector()
#     print(d.get_gender('Iris'))
#
#
# Romanesc(' ')

print_spatiu()
'''17. Functie care primesete 2 liste de numere (numerele pot fi dublate)
Returnati numerele comune

Ex:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Raspuns: {2, 3}'''


def inter_Section(list1, list2):
    list1 = set(list1)
    list2 = set(list2)
    return list1.intersection(list2)


print(inter_Section([1, 1, 2, 3], [2, 2, 3, 4]))

print_spatiu()
'''
18. Functie care sa aplice o reducere de pret
Daca produsul costa 100 lei si aplicam reducere de 10%
Pretul va fi 90
Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida
'''


def reducere(pret, discount):
    if discount in range(0, 101):
        pret_redus = pret - (pret * discount / 100)
        return pret_redus
    else:
        print('Alege un discount pana la maxim 100%.')


print(reducere(100, 10))
print(reducere(100, 105))

print_spatiu()


# 19. Functie care sa afiseze data si ora curenta


def time():
    return datetime.now()


print(time())

print_spatiu()


# 20. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)

def eta(zi, luna, an):
    zi = int(zi)
    luna = int(luna)
    an = int(an)
    viitor = date(an, luna, zi)
    azi = date.today()
    diferenta = viitor - azi
    return f'Ziua cea mare apare in {diferenta.days} de zile.'


print(eta(4, 9, 2022))
print(eta(25, 12, 2023))

print_spatiu()

# if __name__ == '__main__':
#     print_spatiu()
