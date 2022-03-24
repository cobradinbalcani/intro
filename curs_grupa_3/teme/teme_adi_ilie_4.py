# LOOP (for si while)

'''1.
Avand lista
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
a)	Folositi un for ca sa iterati prin toata lista si sa afisati
‘Masina mea preferata este x’
b)	Faceti acelasi lucru cu range-ul listei
c)	Faceti acelasi lucru cu un while
'''
# print('-----------------------------')
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    print(f'Masina mea preferata este {masina}')  # a) iterez prin toata lista cu for
print('-----------------------------')

for masina in range(len(masini)):
    print(f'Masina mea preferata este {masini[masina]}')  # b) iterez prin toata lista cu for si range-ul listei
print('-----------------------------')
masina = 0
while masina in range(len(masini)):
    print(f'Masina mea preferata este {masini[masina]}')   # c) iterez prin toata lista cu while (merge si cu for aici)
    masina += 1
print('-----------------------------')
# print(masini)
'''2.
Aceeasi lista
Folositi un for else
In for
   Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
In else 
   Printati lista
'''
#masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# prima = [masini[0]]
# ultima = [masini[-1]]
# x = [masina.upper() for masina in masini[1:-1]]   # list comprehension, declaram valorile cu majuscula, exceptand prima si ultima valoare
# print(prima + x + ultima)

masina = len(masini)-1
for index in range(len(masini)):
    if index == 0:
        continue
    if index == masina:
        continue
    masini[index] = masini[index].upper()
print(masini)



print('-----------------------------')
'''3. 
Aceeasi lista, 
Vine un cumparator care doreste sa cumpere un Mercedes
Iterati prin ea prin modalitatea aleasa de voi
Daca masina e mercedes 
   Printam ‘am gasit masina dorita de dvs’
   Iesim din ciclu folosind un cuvant cheie care face acest lucru
Altfel
   Printam Am gasit masina X. Mai cautam	
# '''

for masina in masini:                                        # iteram cu for
    if masina == 'MERCEDES':                                 # folosim conditie cu if, ca atunci cand gaseste marca dorita, sa printeze ca a fost gasita
        print('Am gasit masina dorita de dvs')
        break                                                # punem stop sa nu mearga mai departe iteratia
    else:
        print(f'Am gasit masina {masina}, mai cautam.')      # in caz ca nu intra in conditie if, printeaza else



print('-----------------------------')
'''4.
Aceasi lista
Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si 5.
Modernizati parcul de masini
Creati o lista goala, masini_vechi
Iterati prin masini
Cand gasiti Lastun sau Trabant:
-	Salvati aceste masini in masini_vechi
-	Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
Printati Modele vechi: x
Modele noi: x
'''
#masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []

for masina in masini:
    if masina == 'LASTUN' or masina == 'TRABANT':
        continue
    else:
        print(f'Avem masini performante ca: {masina}')


for masina in masini:
    if masina == 'LASTUN':
        masini_vechi.append('LASTUN')
    if masina == 'TRABANT':
        masini_vechi.append('TRABANT')
else:
    masini[masini.index('LASTUN')] = 'Tesla'
    masini[masini.index('TRABANT')] = 'Tesla'

print(masini_vechi)
print(masini)










print('-----------------------------')
# '''
# 6.
# Avand dict
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina xLastun
# Iterati prin lista
#
# Daca masina e Trabant sau Lastun
#    Folositi un cuvant cheie care sa dea skip la ce urmeaza
# (nu trebuie else)
# Printati S-ar putea sa va placa masina x
# '''
#
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

for item in pret_masini.items():
    if item[1] <= 15000:
        print(f'Pentru un buget de 15000 euro puteti alege masina {item[0]} la pretul de {item[1]} de euro.')

for item in pret_masini.items():
    if item[0] == 'Lastun' or item[0] == 'Trabant':
        print(f'S-ar putea sa va placa masina {item[0]}')
        break




print('-----------------------------')
# '''
# 7.
# Avand lista
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterati prin ea
# Afisati de cate ori apare 3
# (nu aveti voie sa folositi count)
# '''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for numar in numere:
    if numar == 3:
        print(f'Aici apare cifra magica:{numar}')      # varianta 1

from collections import Counter                       # varianta 2

x = Counter(numere)
items = x.items()

for i in items:
    print(x[3])
    break

x = 0                                                  # varianta 3

for i in numere:
    if i == 3:
        x += 1
print(x)





print('-----------------------------')
'''
8.
Aceeasi lista
Iterati prin ea
Calculati si afisati suma numerelor
(nu aveti voie sa folositi sum)
'''

suma = 0

for numar in numere:
    print(f'Urmatorul nr este prezent in lista: {numar}.')
    suma = suma + numar
print(f'Suma numerelor din lista este {suma}.')



print('-----------------------------')
'''
9.
Aceeasi lista
Iterati prin ea
Afisati cel mai mare numar
(nu aveti voie sa folositi max)
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# numere.sort()
# print(numere)

for numar in numere:
    print(f'numerele din lista sunt {numar}.')
    numere.sort()
print(f'cel mai mare nr din lista este {numere[-1]}.')
print(f'cel mai mic nr din lista este {numere[0]}.')



print('-----------------------------')
'''
10.
Aceeasi lista
Iterati prin ea
Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
Ex: daca e 3, sa devina -3
Afisati noua lista
'''
lista_n = []
for numar in numere:
    if numar > 0:
        numar = -numar                       # varianta 1
        #numar = numar * -1                   # varianta 2
        #numar = numar - numar - numar        # varianta 3
    lista_n.append(numar)
print(lista_n)







print('-----------------------------')
'''
c. Optionale (may need google)

11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Iterati prin lista alte_numere
Populati corect celelalte liste
Afisati cele 4 liste la final
'''

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3, 0]   # adaug ZERO ca sa vad in ce lista apare
numere_pare = []
numere_impare = []
numere_negative = []
numere_pozitive = []


for x in alte_numere:
    if x % 2:
        numere_impare.append(x)
    if not x % 2:
        numere_pare.append(x)
    if x > 0:
        numere_pozitive.append(x)
    if x < 0:
        numere_negative.append(x)


print(numere_impare, 'nr impare')
print(numere_pozitive, 'nr pozitive')
print(numere_negative, 'nr negative')
print(numere_pare, 'nr pare')
print('-----------------------------')
# '''
# 12.
# Aceeasi lista
# Ordonati crescator lista fara sa folositi sort
# Va puteti inspira vizual de aici
# https://www.youtube.com/watch?v=lyZQPjUT5B4
# '''

new = []
for i in range(len(alte_numere)):
    y = min(alte_numere)
    new.append(y)
    alte_numere.remove(y)
print(new)


#
# def bubbleSort(theSeq):                     # rezolvare de pe net cu DEF
#     n = len(theSeq)
#
#     for i in range(n - 1):
#         flag = 0
#
#         for j in range(n - 1):
#
#             if theSeq[j] > theSeq[j + 1]:
#                 tmp = theSeq[j]
#                 theSeq[j] = theSeq[j + 1]
#                 theSeq[j + 1] = tmp
#                 flag = 1
#
#         if flag == 0:
#             break
#
#     return theSeq
#
#
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
#
# result = bubbleSort(alte_numere)
#
# print(result)


print('-----------------------------')
# '''
# 13.
# Ghicitoare de numar
# numar_secret = Generati un numar random intre 1 si 30
# Numar_ghicit = None
# Folosind un while
#    User alege un numar
#    Programul ii spune:
# -	Nr secret e mai mare
# -	Nr secret e mai mic
# -	Felicitari! Ai ghicit!
# '''

import random

numar_secret = random.randint(1, 30)
nr_ghicit = None
nr_ghicit = int(nr_ghicit or -1)
# print(nr_ghicit)

while nr_ghicit != numar_secret:
    nr_ghicit = int(input('Alege un numar intre 1 si 30: '))
    if nr_ghicit == numar_secret:
        print('Felicitari! Ai ghicit')
    elif numar_secret > nr_ghicit:
        print('Nr secret e mai mare.')
    else:
        print('Nr secret e mai mic.')




print('-----------------------------')
'''14.
Alegeti un numar de la tastatura
Ex:7
Scrieti un program care sa genereze in consola urmatoarea piramida
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
'''

x = int(input('Introdu nr: '))                                   # varianta de pe net
# Outer loop will print number of rows
for i in range(x+1):
    # Inner loop will print the value of i after each iteration
    for nr in range(i):
        print(i, end=' ')  # print number
    # line after each row to display pattern correctly
    print()

print('-----------------------------')
'''15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterati prin lista 2d
Printati ‘Cifra curenta este x’
(hint: nested for - adica for in for)
'''

tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]

lista_2d = []
for z in tastatura_telefon:
    for item in z:
        lista_2d.append(item)
for i in lista_2d:
    print(f'Cifra curenta este {i}')


print('-----------------------------')

