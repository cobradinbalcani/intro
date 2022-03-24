# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import calendar                                   # import de calendar care juta pt zile, luni , ani, data


def printSpatiu():
    print('------------------------------')


#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# string = cuvinte
# boolean = adevarat sau fals
# int = 'cifre'
# float = 'cifra cu zecimale'

# 4 tipuri de variabile in python
# exercitiu cu if
# prajitura_buna = True
#
# print('Mergem la cofetarie')
# if prajitura_buna == False:
#     print('as dori o portie')
#     print('as mai dori inca o portie')
# print('ne indreptam spre casa')

# if else
# daca este nr impar printam corect
# daca este nr par, printam incorect
# nr = 8
# if (nr/2) - 1 == 0:
#     print('corect')
# elif (nr/2) < 0:
#     print('alege o valoare pozitiva')
# else:
#     print('incorect')

# cum scriem in consola

# ora = int(input('Introdu ora'))
# print(ora == 17)
# in cazul in care introducem valoarea '17' atunci raspunsul va fi True

# ex cu if elif else
# dorim sa vedem daca este deschis magazinul in intervalul 9 - 17

# ora = int(input('Introdu ora'))
# if ora < 0:
#     print('alege o valoare intre 0 si 24')
# elif ora < 9:
#     print('prea de dimi')
# elif ora <= 11:
#     print('deschis')
# elif ora <= 17:
#     print('deschis')
# elif ora <= 24:
#     print('inchis')
# else:
#     print('alege o valoare intre 0 si 24')

# benzina_ramasa = 2
# while benzina_ramasa > 0:
#     print('go go!')
# #     benzina_ramasa = benzina_ramasa - 1
# #     if benzina_ramasa == 1:
# #         print('attention!')
# #     print('Stop')
#
# legume = ['varza', 'cartof', 'morcov', '1', 'a', '&', 'True']
#
# print(legume)
# print(legume[4])
# print(len(legume))
# last = legume.pop()
# print(last)
# print('lista:', legume)
#
# legume.append('ceapa')
# print(legume)
#
# last = legume.pop()
# print(last)
# print('lista e:', legume)
#
# legume[3] = 'varza'
# print(legume)
# print(len(legume))
# #
#
# legume_iuti = ['ardei', 'praz']
# legume.extend(legume_iuti)
# print(legume)
# print(legume[3])
# print(legume[1])
# print(legume.count('varza'))


'''
lucram cu while
'''

# apa = 7
#
# # while apa > 0:
# #     print('bem sa ne hidratam')
# #     apa = apa - 1
# #     if apa <= 2:
# #         print('atentie!!!')
# # print('s-a terminat apa!')
#
# #exercitiu for, numaram cifrele dintr-un range si apoi din 2 in 2
# #primele 2 cifre din paranteza -> range-ul; ultima cifra -> passing;
# #in print punem mereu f, atunci cand introducem o valoare de mai sus;
#
# for i in range(1,10,2):
#     print(f'urmatorul este: {i}')
#
# #parcurgere lista cu for prin intermediul indexului
#
# numere = [2,6,8,16,32]
#
# for i in range(0, len(numere)):
#     print(f'indexul ales este:{i} => corespunde pentru {numere[i]}')
#
# #for each - parcurgere lista dar fara index, doar elementul; apoi realizam algoritm (adunam elementele)
# #pentru algoritm adaugam s=0 apoi ca la linia 135 si print la 136
# s=0
# for numar in numere:
#     print(f'numarul curent este {numar}')
#     s = s + numar
# print(f'Suma este {s}')

# listele au dimensiune dinamica si pot fi formate din elemente de tipuri diferite

# masini = ['audi', 'opel', 'vw', 3, True, 'audi',3]
#
# #afisam o lista
# print(masini)
#
# #accesam un element in functie de index
# print(masini[3])
# #
# # #adaugam un nou element
# # masini.append(False)
# # print(masini)
# #
# # #suprascriem un element
# # masini[0]= 'vw'
# # #afisam lista
# # print(masini)
# #
# # #aflam dimensiunea listei
# print(len(masini))
# #
# #scoatem si ne returneaza ultimul element
# last = masini.pop()
# print('ultimul elem', last)
# print('lista este urmatoarea',masini)
# print(len(masini))
# #
# #functia sorted faca oare sortare in ordine alfabetica ??
# team = ['inter','barca','psg']
# print(sorted(team))
# print(len(team))
# print(sorted(team))
# #
# # de cate ori apare un element
# print(masini.count('vw'))
#
#
# #extindem lista
# masini_ro = ['aro', 'dacia']
# masini.extend(masini_ro)
# print(masini)
#
# #printare de 2 liste
# print(masini + team)                     # adunare de liste, la fel ca linia 185
# print(masini, team)
# print(len(masini + team))
# print(masini.__add__(team))
# # #
# avioane = ['f19', 'f18']
#
# print(masini.__add__(avioane))
# print(sorted(avioane))
# # #
# #functia sorted - te ajuta sa aranjezi elementele din lista -> in ordine alfabetica
# #neaparat tre sa fie lista alcatuita din cuvinte string
# alfabet = ['a','c','e','d','b']
# print(sorted(alfabet))
# print(alfabet)
#
# #problema de cate ori apare 3 in [3,2,3,5,3,3]
#
# lista_numere = [3,2,3,5,3,3]
# print(lista_numere.count(3))
# print(len(lista_numere))
#
# s=10
# for numar in numere:
#     print(f'nr nostru este:{numar}')
# print(f'cat este rezultatul adunarii : {s} + {lista_numere.count(3)} = ?')
# #for merge si cu lista de cuvinta, nu doar cifre
# # litere = ['a','b','c']
# # for litera in litere:
#     print(f'{litera}')
#
# #declaram si initializam un dict
# lista_goala = []
# dict_gol = {}
#
# note_elevi = {'Gigi': 7, 'Ana': 8, "Mimi":9}
#
# # #adaugam elemente
# note_elevi ['Sebi'] = 10
#
# #printam dictul
# print(f'{note_elevi}')
# print(note_elevi)
# print(sorted(note_elevi))
# print(note_elevi['Gigi'])
# print(note_elevi.get('Gigi'))

#returneaza doar cheile
# print(note_elevi.keys())
#
#
# #atentie : FUNCTIA se pune in fatza; METODA e dupa numele listei/variabilei   ### de controlat info ###
#
# def printGreetings():
#     print('Buna ziua!!!')
#
# def printGreetingsbyName(nume, prenume):
#     print(f'Buna ziua {nume} {prenume}')
#
# def mediaNr(a, b, c):
#     return (a + b + c) / 3
#
# def piValue():
#     return 3.14
#
# #exercitiu
# #daca pers e majora = True, altfel este False
#
# def verificareMajor(varsta):
#     if varsta >= 18:
#         return True
#     else:
#         return False
#
#
# #zona de apelare (desktop)
# printGreetings()
# printGreetings()
# printGreetingsbyName('Adi', 'Adrian')
# #printGreetingsbyName('Ady','Adry' + 'Adriano')    #greseala pentru ca sunt 3 valori; iar in 2 def sunt daor
# printGreetingsbyName('adriano', 'Ady')
# print(mediaNr(4,6,7))
# print(piValue() + 3.14 + 4 + 4.1234)
# print(piValue())
# #print(len(piValue()))   #--- eroare --- length se poate face doar pt stringuri, pt float nu vrea
# print(verificareMajor(18))
# print(verificareMajor(17))
# print(verificareMajor(20.92))
#
# #se ia varsta userului                        #ex sa introd varsta in cifre, puterea luarii datelor de la tastatura
# age = int(input('introduceti varsta user'))
# if verificareMajor(age):                       #el verifica sa fie True acum
#     print('Cont creat, bine ai venit!')
# else:
#     print('Nu ai varsta minima necesara (18)!!')
#
#
#
#
# t = 'baba '
#
# print(t.rstrip())
# #print(t)
#
# m = 'baba '
#
# print(m.lstrip())

# print('----------tema 3------------ex-----------')
# lista_1=[3];lista_2=[6,5,4]
# lista_noua_metoda_1=lista_1+lista_2
# print(f"liste unite mod 1 {lista_noua_metoda_1}")
# lista_1.append(lista_2)
# print(f"liste unite mod 1 {lista_1}")
# a2='''4.
# Sortati si afisati lista generata la ex anterior
# Stergeti numarul 0 folosind o functie
# Afisati iar lista
# '''
# print(a2)
# lista_noua_metoda_1.sort()
# print(f"lista sortata {lista_noua_metoda_1}")
# print('----------tema 3------------ex-----------')

# pret_masini = {
#      'Dacia': 6800,
#      'Lastun': 500,
#      'Opel': 1100,
#      'Audi': 19000,
#      'BMW': 23000
#  }
# buget = 15000
# pret = list(pret_masini.values())
# i = 0
# for masinuta in pret_masini.keys():
#     if int(pret[i]) <= buget:
#         print(f"Pentru un buget de {buget} euro puteti alege masina {masinuta} care costa {pret[i]}")
#         i += 1



# ex sa gasesti care e cel mai mare nr din cele 3 alese
def nrTrei(x):
    return int(x)

print(nrTrei(max(-2, -1, -3)))

t = 3
pi = 3.14

c = (t*t) * pi

print(c)

x = 'baba'

print(x.upper())
print('--------------------------------')

for day in calendar.day_name:          # printez zilele saptamanii
    print(day)

printSpatiu()

for name in calendar.month_name:        # printez lunile anului
    print(name)

printSpatiu()

yy = 1974  # year
mm = 8    # month

# To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))

printSpatiu()

# import sexmachine.detector as gender
# import gender_guesser.detector as gender
# d = gender.Detector()
# print(d.get_gender("Bob"))

import os.path
import codecs


# def _most_popular_gender(self, name, counter):
#     """Finds the most popular gender for the given name counting by given counter"""
#     if name not in self.names:
#         return self.unknown_value


# print(_most_popular_gender())


def suma(a, b):
    return a+b

print(suma(2,3))


# trix = 4 / 0
# print(trix)


azi = 'buna dimineata!'
print(azi)