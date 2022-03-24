# B # 1 variabila reprezinta o zona ce memoreaza o valoare

# 2 declar si initializez variabile din tipurile:string, int, float, boolean.

leguma = 'cartof'
ziua = 1
pi = 3.14
azi_ninge = True

print(leguma)
print(ziua)
print(pi)
print(azi_ninge)

# 3 utilizez functia type pt a verifica tipul de date

print(leguma, type(leguma))
print(pi, type(pi))
print(ziua, type(ziua))
print(azi_ninge, type(azi_ninge))

# 4 rotunjesc float cu round() si suprascriu variabila + verificare

print(round(pi))
pi = round(pi)
print(pi, type(pi))

# 5 printez 4 prop fol cele 4 variabile

print(f'La pranz as manca si un {leguma} copt.')
print(f'Azi este ziua {ziua} a lunii februarie.')
print(f'Azi a nins ? Raspuns: {azi_ninge}.')
print(f'{pi} este cifra mea norocoasa.')

'''6 Citim numele si prenumele de la tastatura
apoi afisam cate caractere are numele intreg'''

nume = input('Numele meu este: ')
prenume = input('Prenumele meu este: ')
numele_complet = input(f'{nume} {prenume} are {len(nume + prenume)} caractere')

'''7 Citim lungimea si latimea de latastatura
apoi afisam care este aria dreptunghiului'''

Lungime = input('L este de ')
latime = input('l este de ')
aria_d = print(f'Aria dreptunghiului este {int(Lungime) * int(latime)}')

# 8 declaram string si un int x, apoi afisam stringul fara ultimele x caractere

enunt = 'Coral is either the stupidest animal or the smartest rock'
enunt_taiat = int(input('Voi alege cifra: '))
'''enunt_final = len(enunt) - enunt_taiat
print(enunt[:(enunt_final)])'''  # varianta 2
print(enunt[:(len(enunt) - enunt_taiat)])  # varianta 1

# 9 declaram un string nou care sa fie format din primele 5 caractere + ultimele 5

enunt_nou = print(enunt[:5] + enunt[-5:])

# 10 afisam de cate ori apare cuvantul 'the'

print(enunt.count('the '))

# 11 inlocuim the cu THE peste tot si apoi printam

print(enunt.replace('the', 'THE'))

# 12 salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock


# print(len(enunt)) # verificata dimensiunea
cuvantul_rock = enunt.index('rock')
# print(enunt.index('rock'))
print(cuvantul_rock)

# folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant

print(enunt[:(cuvantul_rock)])

# 13 declar o alta variabila de tip string in care adaug cele 4 variabile de la ex 2, folosind tehnica de formatare

variabila_formatata = f'Am cumparat {ziua * 1} {leguma.capitalize()} de {pi}kg, lucru mai rar dar este {azi_ninge}.'
print(variabila_formatata)

# putem avea expresii (operaţii aritmetice, apeluri de funcţii etc) direct în interiorul formatării. Ex:

# variabila_formatata = f'Am cumparat {ziua*1} {leguma.capitalize()} de {pi}kg, lucru mai rar dar este {azi_ninge}.'
# print(variabila_formatata)

# 14 afisare doar numere pare/impare din string

numerotare = '0123456789'

# print(list(enumerate(numerotare))) # enumereaza indexul fiecarei valori din string

print(numerotare[0:10:2])
print(numerotare[1::2])

# 15 declar laturile unui dreptunghi si iau datele de la tastatura, apoi printez aria dreptunghiului

Lungime = int(input())
latime = int(input())
print(Lungime * latime)

# 16 citesc de la tastatura un string de dimensiune impara
# afisez caracterul din mijloc

dim_impara = input('Introduceti cuvantul: ')
index = len(dim_impara)  # aflu lungimea
index = (index - 1) / 2  # aflu cifra caracterului pentru a fi printata cea din mijloc
print(dim_impara[int(index)])

# 17 citesc un string de la tastatura si salveaza fiecare cuvant intr-o variabila

a, b = input().split(' ', 1)
print(a)
print(b)
print('------------------------------------------------')
# 18 -- oare exista o metoda speciala ?

x = str(input('String de la tastatura: '))  # citesc string de la tastatura
first = x[:1]  # salvez primul caracter in variabila
last = x[-1:]  # salvez ultimul caracter in variabila
x_troncat = x[1:-1] # salvez stringul fara prima si ultima litera
x_final = (x_troncat.replace(first, first.upper()))  # acest caracter salvat se capitalizeaza peste tot
print(first + x_final + last)


# 19 citesc un user si apoi o parola de la tastatura

user = input('Introduceti userul: ')
parola = input('Introduceti parola: ')
parola_stelata = '*' * len(parola) # modific sa apara cu simbolul stea
# printez userul si parola, afisand dimensiunea parolei in mod dinamic, indiferent care este
print(f'Parola pentru userul {user} este {parola_stelata} si are {len(parola)} caractere.')
print('---------------------------------------------------------')
