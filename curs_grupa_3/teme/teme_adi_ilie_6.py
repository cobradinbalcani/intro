# b. Obligatorii (mediu)

# Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei


import datetime
import datetime
import math
from datetime import date
import calendar


# from teme_adi_ilie_5 import print_spatiu
#
# print_spatiu()

def space():
    print('------------------------------')


'''1. 
Clasa Cerc

Atribute: raza, culoare

Constructor pt ambele atribute

Metode:
descrie_cerc() - va PRINTA culoarea si raza
aria() - va RETURNA aria 
diametru() 
circumferinta() '''


class Cerc:
    raza = None
    culoare = None

    def __init__(self, raza, culoare):
        self.culoare = culoare
        self.raza = raza

    def descrie_cerc(self):
        print(f' raza = {self.raza} cm, iar culoarea este: {self.culoare}')

    def aria(self):
        print(f'Aria cercului este: {(self.raza * self.raza) * math.pi} cm')

    def diametru(self):
        print(f'Diametrul cercului este: {self.raza * 2} cm')

    def circumferinta(self):
        print(f'Circumferinta cercului este: {(self.raza * 2 * math.pi)} cm')


cerc1 = Cerc(3, 'orange')
cerc2 = Cerc(4, 'gri')

# print(Cerc.raza, Cerc.culoare)  atunci cand atributele detin deja valori -> dai print asa atributelor
print(cerc1.culoare, cerc1.raza)

cerc1.descrie_cerc()
cerc1.aria()
cerc1.diametru()
cerc1.circumferinta()
cerc2.descrie_cerc()
cerc2.aria()
cerc2.diametru()
cerc2.circumferinta()

space()
'''2. 
Clasa Dreptunghi

Atribute: lungime, latime, culoare

Constructor pt toate atributele

Metode:
descrie() va PRINTA lungime, latime, culoare
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().
'''


class Dreptunghi:
    lungime = None
    latime = None
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'lungimea = {self.lungime}, latimea = {self.latime}, culoarea este: {self.culoare}')

    def aria(self):
        print(f'Aria dreptunghi = {self.lungime * self.latime} cm')

    def perimetru(self):
        print(f'Perimetrul dreptunghi = {2 * (self.lungime + self.latime)} cm')

    def schimba_culoarea(self, culoare_9):
        self.culoare = culoare_9


primul_d = Dreptunghi(5, 4, 'verde')
second_d = Dreptunghi(4, 3, 'mov')

print(primul_d.lungime, primul_d.latime, primul_d.culoare)
primul_d.descrie()  # la print apare culoarea initiala
primul_d.aria()
primul_d.perimetru()
primul_d.schimba_culoarea('blue')  # introduc noua culoare
primul_d.descrie()  # la print se vede noua culaore

second_d.descrie()  # la print apare culoarea initiala
second_d.aria()
second_d.perimetru()
second_d.schimba_culoarea('violet')  # introduc noua culoare
second_d.descrie()  # la print se vede noua culaore

space()

'''3.
Clasa Angajat

Atribute: nume, prenume, salariu

Constructor() pt toate atributele // constructor reprezinta __init__

Metode:
descrie() print nume, prenume, salariu
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent) 
'''


class Angajat:
    nume = None
    prenume = None
    salariu = None

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Salariul lui {self.nume} {self.prenume} este de {self.salariu} euro.')

    def nume_complet(self):
        print(f'Angajatul lunii martie este: {self.nume} {self.prenume}!')

    def salariu_lunar(self):
        print(f'Salariul pe luna decembrie este: {self.salariu} euro!')

    def salariu_anual(self):
        print(f'Salariul anual este: {self.salariu * 12} euro!')

    def marire_salariu(self, procent):
        self.salariu = ((self.salariu / 100) * procent) + self.salariu
        print(f'Salariu marit din ianuarie este de: {self.salariu} euro!')


angajat1 = Angajat('Ion', 'Popescu', 2000)
angajat2 = Angajat('Adi', 'Ionescu', 3000)
angajat1.descrie()
angajat1.nume_complet()
angajat1.salariu_lunar()
angajat1.salariu_anual()
angajat1.marire_salariu(25)
angajat1.salariu_anual()
angajat2.descrie()
angajat2.nume_complet()
angajat2.salariu_lunar()
angajat2.salariu_anual()
angajat2.marire_salariu(20)
angajat2.salariu_anual()

space()

'''4.
Clasa Factura

Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc

Constructor: toate atributele, fara serie

Metode:
schimba_cantitatea(cantitate)
schimba_pretul(pret)
schimba_nume_produs(nume)
genereaza_factura() - va printa tabelar daca reusiti

Factura seria x numar y
Data: generati automat data de azi
Produs | cantitate | pret bucata | Total “
Telefon |      7       |       700       | 49000     

Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/
'''


class Factura:
    seria = 'FRF'
    numar = None
    nume_produs = None
    cantitate = None
    pret_bucata = None

    def __init__(self, numar, nume_produs, cantitate, pret_bucata):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_bucata = pret_bucata

    def schimba_cantitate(self, cantitate_9):
        self.cantitate = cantitate_9

    def schimba_pretul(self, pret_nou):
        self.pret_bucata = pret_nou

    def schimba_nume_produs(self, nume_nou):
        self.nume_produs = nume_nou

    def genereaza_factura(self):
        print(f'Factura {self.seria} numar {self.numar}')
        print(f'Data: {date.today()}')
        print(' Produs | cantitate | pret bucata | Total')
        print(
            f'{self.nume_produs} |     {self.cantitate}     |     {self.pret_bucata}     | {self.cantitate * self.pret_bucata}')


factura1 = Factura(3, 'tv', 1, 500)
factura2 = Factura(4, 'laptop', 3, 600)
factura1.schimba_cantitate(2)
factura1.schimba_pretul(550)
factura1.schimba_nume_produs('telefon')
factura2.schimba_cantitate(1)
factura2.schimba_pretul(450)
factura2.schimba_nume_produs('consola')

print(factura1.nume_produs, factura1.pret_bucata, factura1.cantitate, factura1.numar, factura1.seria)
factura1.genereaza_factura()
factura2.genereaza_factura()

space()

'''5. 
Clasa Cont

Atribute: iban, titular_cont, sold

Constructor pentru toate

Metode:
afisare_sold() - Titularul x are in contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
'''


class Cont:
    iban = None
    titular_cont = None
    sold = None
    suma = None

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.')

    def debitare_cont(self, suma):
        self.suma = suma
        self.sold = self.sold + self.suma
        print(f'Ai alimentat cu succes contul cu {self.suma} lei.')

    def creditare_cont(self, suma):
        self.suma = suma
        if self.suma <= self.sold:
            self.sold = self.sold - self.suma
            print(f'Ai retras cu succes suma de {self.suma} iar in cont au mai ramas {self.sold} lei.')
        else:
            print('Fonduri insuficiente!')


cont1 = Cont('ING44', 'Adrian Ilie', 500)
cont2 = Cont('ING55', 'Marius Popa', 600)

cont1.afisare_sold()
cont1.debitare_cont(50)
cont1.afisare_sold()
cont1.creditare_cont(100)
cont1.afisare_sold()

cont2.afisare_sold()
cont2.debitare_cont(500)
cont2.afisare_sold()
cont2.creditare_cont(10000)
cont2.afisare_sold()

space()

'''6.
Clasa Masina

Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate masinile cand ies din fabrica sunt gri
Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
Culori disponibile = alegeti voi 5-7 culori
Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
Inmatriculata = False

Constructor: model, viteza_maxima

Metode:
descrie() (se vor printa toate atributele, inafara de culori_disponibile)
inmatriculare() - va schimba atributul inmatriculata in True
vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
franeaza() - masina se va opri si va avea viteza 0
'''


class Masina:
    marca = 'Volvo'
    model = None
    viteza_maxima = None
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = {'alb', 'negru', 'verde', 'mov', 'bleu', 'rosu'}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(
            f'Masina {self.marca} {self.model} are urm caracteristici: culoare = {self.culoare}, viteza actuala = {self.viteza_actuala} km/h, viteza maxima = {self.viteza_maxima} km/h, inmatriculata = {self.inmatriculata} !')

    def inmatriculare(self):
        if self.inmatriculata == False:
            self.inmatriculata = True
            print(self.inmatriculata)
        else:
            print('Masina deja inmatriculata!')

    def vopseste(self, culoare_9):
        if culoare_9 in self.culori_disponibile:
            self.culoare = culoare_9
            return self.culoare
        else:
            print('Culoarea nu este disponibila!')

    def accelereaza(self, viteza):
        self.viteza_actuala = viteza
        if viteza > 0 and viteza <= self.viteza_maxima:
            return f'accelerez pana la {viteza} km/h'
        elif self.viteza_actuala < 0:
            return 'eroare'
        elif viteza > self.viteza_maxima:
            return self.viteza_maxima
        else:
            return 'Masina ramane pe loc, mai baga combustibil!'

    def franeaza(self):
        self.viteza_actuala = 0
        print(f'Masina s-a oprit la viteza {self.viteza_actuala} km/h!')


masina1 = Masina('xc40', 200)
masina2 = Masina('s80', 300)
print(masina1.model, masina1.viteza_maxima, masina1.inmatriculata, masina1.culoare, masina2.model,
      masina2.viteza_maxima, masina2.inmatriculata)
Masina.descrie(masina1)
masina1.descrie()
masina1.inmatriculare()
masina1.vopseste('menta')
print(masina1.culoare)
print(masina1.accelereaza(0))
masina1.franeaza()

masina2.descrie()
masina2.inmatriculare()
masina2.vopseste('alb')
print(masina2.culoare)
print(masina2.accelereaza(10))
masina2.franeaza()

space()

'''7. Clasa TodoList
 
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor

Metode:
adauga_task(nume, descriere) - se va adauga in dict
finalizeaza_task(nume) - se va sterge din dict
afiseaza_todo_list() - doar cheile
afiseaza_detalii_suplimentare(nume_task) - in functie de numele taskului, printam detalii suplimentare daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
Daca acesta raspunde nu - la revedere
daca raspunde da - il cerem detalii task si salvam nume+detalii in dict
'''


class ToDoList:
    todo = {}

    def adauga_task(self, nume, descriere):
        self.nume = nume
        self.descriere = descriere
        self.todo = {nume: descriere}
        print(self.todo)

    def finalizeaza_task(self, nume):
        self.nume = nume
        self.todo.pop(nume)
        print(self.todo)

    def afiseaza_todo_list(self):
        print(list(self.todo.keys()))  # afiseaza cheile ca o lista, altfel ar scrie ca este dict cand dai run!

    def detalii(self, nume_task):
        if nume_task not in self.todo.keys():
            print(f'{nume_task} nu e in lista, doresti sa-l adaugi? spune da daca doresti: ')
            if input() == 'da':
                self.todo[nume_task] = input('Introdu detalii: ')
                print(self.todo)
            else:
                print('la revedere')
        else:
            print(f'{nume_task} se afla deja in lista!')


shop1 = ToDoList()
shop2 = ToDoList()
shop1.adauga_task('apa', 'dorna')  # printeaza dict cu apa: dorna
shop1.finalizeaza_task('apa')  # printeza dict gol pt ca am sters cheia
shop2.adauga_task('bere', 'stela')  # printeaza dict cu bere: stela
shop2.finalizeaza_task('bere')
shop1.adauga_task('suc', 'natural')  # printeaza dict cu suc: natural
shop2.adauga_task('fructe', 'mere')  # printeaza dict cu suc: natural

shop1.afiseaza_todo_list()
shop1.detalii('alune')
shop2.afiseaza_todo_list()
shop2.detalii('fructe')

space()

# if __name__ == '__main__':
#     print_spatiu()
