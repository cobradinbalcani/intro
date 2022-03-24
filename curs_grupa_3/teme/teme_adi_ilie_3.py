# 1 Declara o lista note_muzicale in care sa pui do re mi etc pana la do

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']

print(note_muzicale, type(note_muzicale))  # a) afisez lista si tipul variabilei

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do'][::-1]  # b)	Inversez ordinea folosind slicing si suprascriu aceasta lista
print(note_muzicale)  # c)	Printeaza varianta actuala (inversata)

note_muzicale.reverse()  # d)  aplic metoda de inversare a listei
print(note_muzicale)  # e)	Printeaza varianta initiala

# 2 De cate ori apare ‘do’?

print(note_muzicale.count('do'))  # printez de cate ori apare 'do'

# 3 Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
# Gasiti 2 variante sa le uniti intr-o singura lista.

lista_1 = [3, 1, 0, 2]
lista_2 = [6, 5, 4]
lista_unita = lista_2 + lista_1  # varianta 1 unire a doua liste
print(lista_2.__add__(lista_1))  # varianta 2 unire a doua liste
lista_unita.sort()  # sortez lista
print(lista_unita)  # print lista sortata
# lista_1.append(lista_2)                 # varianta 3 unire a doua liste
# lista_1.sort()                          # de ce da eroare sortare de lista dupa ce am facut append ??
print(lista_1)  # printez verificare daca sunt unite lista 1 cu lista 2

# 4 Sortati si afisati lista generata la ex anterior
# Stergeti numarul 0 folosind o functie
# Afisati iar lista

print(set(sorted(lista_unita)))  # sortez si afisez lista, transformand in SET
(lista_unita.remove(0))  # sterg nr zero cu ajutorul functiei remove
print(lista_unita)  # afisez lista actualizata

# 5 Folosind un if verificati lista generata la ex3 si afisati:
# -	Lista este goala
# -	Lista nu este goala

if lista_unita:  # conditie daca lista contine elemente: TRUE
    print('Lista nu e goala.')
else:
    print('Lista e goala.')

# 6 Folositi o functie care sa stearga lista de la ex3

lista_unita.clear()  # sterg lista cu CLEAR

# 7 Copy paste la ex 5. Verificati inca o data.
# Acum ar trebui sa se afiseze ca lista e goala

if lista_unita:  # conditie daca lista contine elemente: FALSE, pentru ca a fost stearsa
    print('Lista nu e goala.')
else:
    print('Lista e goala.')

# 8 Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folositi o functie ca sa afisati Elevii (cheile)

dict1 = {'Ana': 8,
         'Gigel': 10,
         'Dorel': 5
}
print(dict1.keys())  # afisez cheile
print(type(dict1), dict1.values())  # afisez valorile si tipul variabilei

# 9 Printati cei 3 elevi si notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o veti lua folosindu-va de cheie

# print(sorted(dict1))         # sortare in dictionar DICT
# print(f'Ana a luat nota .')
print(f'Ana a luat nota {dict1["Ana"]}.')  # afisez nota Anei
print(f'Gigel a luat nota {dict1["Gigel"]}.')  # afisez nota lui Gigel
print(f'Dorel a luat nota {dict1["Dorel"]}.')  # afisez nota lui Dorel

# 10 Dorel a facut contestatie si a primit 6
# Modificati nota lui Dorel in 6
# Printati nota dupa modificare

dict1["Dorel"] = '6'  # suprascriere valoare
print(dict1["Dorel"])  # printare noua valoare

# print(set(dict1))       # transformat in set
# print(*set(dict1))         # afisat doar cheile fara paranteze si virgule

# 11 Gigel se transfera din clasa
# Cautati o functie care sa il stearga
# Vine un coleg nou. Adaugati Ionica, cu nota 9
# Printati dictionarul schimbat

dict1.pop('Gigel')  # scoatem elevul Gigel
dict1.update({'Ionica': 9})  # adaugam elevul Ionica cu nota 9 iar apoi printam noile valori
print(dict1)

# 12 Set
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# Adaugati in zilele_sapt ‘luni’
# Afisati zile_sapt

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
# print(sorted(list(zile_sapt)))      # sortare alfabetica de lista
# print(zile_sapt.union(weekend))     # unire a 2 SET - functia union()
zile_sapt.add('luni')                # adaugam ziua dar fiind set nu ia incosiderare o valaore identica
print(zile_sapt)
zile_sapt = list(zile_sapt)  # setul devine lista
zile_sapt.append('luni')  # adaugam o valoare care deja exista in lista
print(zile_sapt)  # printam lista actualizata
zile_sapt = set(zile_sapt)  # transformare lista in set din nou pentru a face operatii intre 2 seturi

# 13 Folositi un if si verificati daca
# -	Weekend este un subset al zilelor din sapt
# -	Weekend nu este un subset al zilelor din sapt

if weekend.issubset(zile_sapt):  # folosesc metoda issubset() VARIANTA 1
    print('Weekend este un subset al zilelor saptamanii.')  # daca toate elementele se gasesc in celalalt set, atunci este TRUE
else:
    print('Weekend nu este un subset al zilelor din sapt.')  # daca nu sunt toate, este FALSE

if zile_sapt <= weekend:  # VARIANTA 2 folosesc operator de comparare   (<= cand un set este propriul subset)
    print('Weekend este un subset al zilelor saptamanii.')  # daca toate elementele se gasesc in celalalt set, atunci este TRUE
else:
    print('Weekend nu este un subset al zilelor din sapt.')  # daca nu sunt toate, este FALSE

# saptamana = weekend <= zile_sapt         # declar variabila saptamana
# print(saptamana)                         # la printare, rezultatul va fi TRUE

# 14 Afisati diferentele dintre aceste 2 seturi (exercitiu 12)

print(zile_sapt)  # printez SET
print(zile_sapt - weekend)  # printez elementele prezente in set1 dar nu si in set2
print(weekend - zile_sapt)  # printez elementele prezente in set2 dar nu si in set1  (rezultat set nul)

print(zile_sapt.difference(weekend))  # VARIANTA 2 pentru a vedea diferente intre SETuri: set1 si set2
print(weekend.difference(zile_sapt))  # si invers set2 si set1

# 15 Afisati intersectia elementelor din aceste 2 seturi (exercitiu 12)

print(zile_sapt.intersection(weekend))  # printez intersectia prin metoda intersection()
print(zile_sapt.isdisjoint(weekend))  # isdisjoint() metoda se vezi daca 2 set contin elemente distincte
# raspuns FALSE, pentru ca exista elemente comune


# print(zile_sapt.issuperset(weekend))      # issuperset() este inversul lui issubset()

'''16 Ne imaginam o echipa de fotbal pt teren sintetic.
3 Schimbari maxime admise

Declara o Lista cu 5 jucatori
Schimbari_efectuate = va jucati voi cu valori diferite
Schimbari_max = 3

Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
-	Efectuam schimbarea 
-	Stergem jucatorul scos din lista
-	Adaugam jucatorul intrat
-	Afisam a intra x, a iesit y, mai aveti z schimbari
Daca jucatorul nu e in teren:
-	Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
-	Afisati ‘mai aveti z schimbari’

Testati codul cu diferite valori

Google search hint
“how to check if item is in list python” '''

echipa = ['gigi', 'didi', 'lolo', 'lili', 'fifi']
schimbari_efectuate = 0
schimbari_max = 3
first_in = 'gogu'
if 'mimi' in echipa:
    if schimbari_max > 0 and schimbari_max < 4 and schimbari_efectuate > -1 and schimbari_efectuate < 4 and schimbari_max + schimbari_efectuate == 3:
        schimbari_max -= 1
        first_sub = echipa.pop()
        echipa.append(first_in)
        schimbari_efectuate += 1
        print(F'Intra in teren jucatorul {echipa[-1]} si iese din teren {first_sub}, schimbari ramase = {schimbari_max} iar schimbari efectuate = {schimbari_efectuate}.')
    else:
        print('Ai voie ori zero ori una ori doua sau trei schimbari per meci.')
else:
    print('Nu se poate efectua schimbarea deoarece jucatorul "mimi" nu este in teren.')
    print(F'Au mai ramas {schimbari_max} schimbari.')

