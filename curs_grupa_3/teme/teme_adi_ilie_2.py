'''
B # 1 "if else" functioneaza ca un conditional in mod secvential:
in cazul in care una din variantele propuse este True, aceasta se va printa
dar daca toate sunt False, atunci se printeaza "else", sau nimic daca else nu exista

pe scurt:
'''

# 2 Verifica si afiseaza daca x este numar pozitiv sau nu
x = int(input('Introdu nr:'))  # asociez x cu cifra intreaga pt a fi citita de la tastatura
if x > 0:  # incep conditia ca x mai mare ca zero
    print('Ai ales un nr pozitiv.')  # printez conditia
else:  # conditie in caz ca x nu e mai mare ca zero
    print('Nu ai ales un nr pozitiv.')  # printez conditia

# 3 Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

x = int(input('Introdu nr:'))  # asociez x cu cifra intreaga pt a fi citita de la tastatura
if x > 0:  # incep conditia ca x mai mare ca zero
    print('Ai ales un nr pozitiv.')  # printez conditia
elif x == 0:  # conditie in caz ca x egal cu zero
    print('Ai ales un nr neutru.')
else:  # conditie in caz ca x e mai mic ca zero
    print('Ai ales un nr negativ de data asta.')  # printez conditia

# 4 Verifica si afiseaza daca x este intre -2 si 13

x = 13
if x >= -2 and x <= 13: # pun 2 conditii: x mai mare sau egal decat -2 si in acelasi timp x tre sa fie mai mic sau egal ca 13
    print('Nr ales este intre 13 si -2.')
else:
    print('Ai ales un nr inafara secventei dorite.')

# 5 Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5

x = 7
y = 2

if not (x - y) < 5:  # conditie ca scadearea dintre x si y sa fie mai mic ca 5, apoi inversez cu NOT
    print(f'Diferenta dintre {x} si {y} e mai mare sau egala cu 5')
else:
    print(f'Diferenta dintre {x} si {y} e mai mica de 5')

# 6 Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)

x = 5
if not (x >= 5 and x <= 27):  # pun 2 conditii: x mai mare sau egal decat 5 si in acelasi timp x tre sa fie mai mic sau egal ca 27
    # iar la final inversez conditionalul cu ajutorul lui NOT
    print('Ai ales un nr inafara secventei 5 si 27.')
else:
    print('Nr ales este intre 5 si 27.')

# 7 x si y (int)
# Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare

x = int(input('Introdu nr:'))
y = int(input('Introdu celalalt nr:'))

if x == y:                                       # conditie x egal cu y
    print(f'Intotdeauna {x} e egal cu {y}.')
elif x > y:                                      # conditie x mai mare ca y
    print(f'{x} e mai mare ca {y}')
else:                                            # conditie x mai mic ca y
    print(f'{y} e mai mic ca {x}')

# 8 X, y, z - laturile unui triunghi
# Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.

X = 7
y = 9
z = 8

'''Le triunghi tadaaam: # desenez triunghi
    /\
 X /  \Y
  /____\
     Z
'''
if X == y == z:                                           # conditie 3 laturi egale
    print('Avem un triunghi echilateral.')
elif X != y != z:                                         # # conditie 3 laturi diferite
    print('Avem un triunghi oarecare')
else:                                                     # conditie ramasa, doar 2 laturi egale si 1 diferita
    print('Avem un triunghi isoscel')

# 9 Citeste o litera de la tastatura
# Verifica si afiseaza daca este vocala sau nu

x = str(input('Alege o litera: '))               # citesc litera de la tastatura
if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U':
    print('Ai ales o vocala.')                   # conditie 1: x sa fie oricare vocala, litera mica/mare
else:
    print('Nu ai ales o vocala.')                # conditie 2: x nu este vocala

'''
# 10 Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza:
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''
# x = int(input('Alege nota: '))
x = 4

if x > 9 and x < 11:
    print(f'Nota {x} reprezinta A in sistem american.')  # x mai mare ca 9, dar nici sa depaseasca 10
elif x > 10:
    print(f'Nota {x} nu exista in sistem.')  # x mai mare ca 10, input invalid
elif x > 8:
    print(f'Nota {x} reprezinta B in sistem american.')  # x mai mare ca 8
elif x > 7:
    print(f'Nota {x} reprezinta C in sistem american.')  # x mai mare ca 7
elif x > 6:
    print(f'Nota {x} reprezinta D in sistem american.')  # x mai mare ca 6
elif x > 4:
    print(f'Nota {x} reprezinta E in sistem american.')  # x mai mare ca 4
elif x <= 4 and x > 0:
    print(f'Nota {x} reprezinta F in sistem american')  # x mai mic sau egal cu 4
else:
    print(f'Nota {x} nu exista in sistem.')  # x mai mic ca 0, input invalid

# 11 Verifica daca x are minim 4 cifre
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

x = -1111

if len(str(abs(x))) >= 4:  # conditie ca dimensiunea lui x (de string) sa fie mai mare sau egala ca 4
    print(x, 'are 4 cifre.')
else:  # conditie ca dimensiunea lui x sa fie mai mica decat 4
    print(x, 'nu are minim 4 cifre.')

# 12 Verifica daca x are exact 6 cifre


x = -111222

if len(str(abs(x))) == 6:
    print(x, 'are exact 6 cifre.')  # conditie ca dimensiunea lui x (de string) sa fie egala cu 6
else:  # conditie ca dimensiunea lui x sa fie diferit de 6
    print(x, 'are mai mult sau mai putin de 6 cifre.')

# 13 Verifica daca x este numar par sau impar

x = int(input('Alege numarul: '))

if x % 2:                          # folosesc modulus ca sa obtin impartirea cu rest
    print(f'{x} este nr impar.')   # cand ramane rest 1 o sa fie impar
else:
    print(f'{x} este nr par.')     # fara rest, nr este par


# 14 x, y, z (int)
# Afiseaza care este cel mai mare dintre ele?

x = 7
y = 7
z = 7

if (x > y and x > z) and (x != y and x != z):  # conditie ca x sa fie mai mare sau diferit fata de y si z
    print(x, 'e cel mai mare')
elif (y > x and y > z) and (y != z and y != x):  # conditie ca y sa fie mai mare sau diferit fata de x si z
    print(y, 'e cel mai mare')
elif (z > x and z > y) and (z != x and z != y):  # conditie ca z sa fie mai mare sau diferit fata de x si y
    print(z, 'e cel mai mare')
else:
    print('numerele sunt egale')  # conditie ramasa: cand toate sunt egale

# 15 X, y, z - reprezinta unghiurile unui triunghi
# Verifica si afiseaza daca triunghiul este valid sau nu

X = 45
y = 44
z = 91

if X + y + z == 180:                 # conditie ca cele 3 laturi sa adune fix 180 de grade
    print('Triunghiul este valid.')
else:                                # conditie ca cele 3 laturi sa fie diferite valoare de 180 de grade
    print('Triunghiul nu este valid.')


''' 16
Pentru exercitiile cu biletele de avion incercati sa aplicati tehnicile de equivalence partitioning si boundary value analysis astfel incat sa eficientizati testarea.

Sa tineti cont de urmatoarea chestie: tehnicile de testare vor fi aplicate nu pe faptul ca o persoana are pasaport sau nu, ci pe varsta persoanei'''

# pasaport = input('Are pasaportul valid : DA/NU ')
# ambii_parinti = input('Are ambii parinti? DA/NU ')
# permisiune = input('Are permisiune? DA/NU/NA ')
# Age = int(input('Introdu varsta persoana: '))             # citesc varsta de la tastatura ca nr intreg
#
# if pasaport == 'DA' and (Age >= 18 or ambii_parinti == 'DA' or permisiune == 'DA'): # adaug conditie ca persoana sa aiba 18 ani sau mai mult
#     print('Permite calatoria')                                                      # in asa fel incat e de ajuns sa aiba pasaport + minim 18 ani
# else:
#     print('Nu permite calatoria')


# Codul de mai sus a fost actualizat mai jos astfel incat sa țină cont și de varsta
# tot in codul de sus am adaugat conditia sa tina cont si de varsta (vezi linia cu if) # varianta 2

Age = int(input('introduceti varsta: '))
pasaport = input('Are pasaportul valid : DA/NU ')
ambii_parinti = input('Are ambii parinti? DA/NU ')
permisiune = input('Are permisiune? DA/NU/NA ')

# varianta 1

if Age >= 18 and pasaport == 'DA':
    print('permite calatoria')
elif pasaport == 'DA' and (ambii_parinti == 'DA' or permisiune == 'DA') :
    print('Permite calatoria')
else :
    print('Nu permite calatoria')

''' 
Tehnicile de testare discutate vor fi aplicate pe condiția age>=18 
și vor consta în crearea unor clase de echivalență 
din care vom alege cate o singura valoare 
și respectiv valorile de graniță pentru a le folosi în testare
'''