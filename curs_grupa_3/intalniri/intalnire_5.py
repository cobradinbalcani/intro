#FUNCTII

from datetime import datetime    # obligatoriu SUS se pun importurile
from intalnire_5_proba import time


lista_1 = [1, 2, 3, 4, 5]
lista_2 = [3, 2, 4, 4, 1]


def adunare_liste(x, y):
    rezultat = x + y
    return rezultat

# print(adunare(2, 3))
# print(adunare('2','3'))
# print(adunare(['a', 'b'], [2, 3]))

rezultat_adunare = adunare_liste(lista_1, lista_2)

print(rezultat_adunare)


def afiseaza_timpul_curent():
    timpul_curent = time()
    return timpul_curent


def time():
    return datetime.now()

rezultat_adunare = adunare_liste(lista_1, lista_2)
print(rezultat_adunare)
print(type(afiseaza_timpul_curent()))
print(afiseaza_timpul_curent())

lista_nr_pare = []
lista_nr = [1, 2, 3, 4, 55, 8, 9, 11, 23]

def numere_pare(numar):
    if numar % 2 == 0:
        lista_nr_pare.append(numar)


def function(lista):
    for numar in lista:
        numere_pare(numar)



rezultat = function(lista_nr)
print(rezultat)
print(lista_nr_pare)
