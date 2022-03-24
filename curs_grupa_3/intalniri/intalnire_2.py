print('-------operatori atribuire------scurtaturi')
x = 5
# x = x + 3
print(x)

x += 3
print(x)

x //= 2  # neaparat pus al doilea slash, altfel printeaza float
print(x)

# operatori aritmetici
i = 6
j = 4
print(i + j)  # adunare
print(i - j)  # scadere
print(i * j)  # inultire
print(i / j)  # impartire float
print(i // j)  # impartire int
print(i % j)  # modulus
# import math

d = 6.89
e = 2
# print(math.floor(d)) # transforma semnul // in impartire exact
print(d // e)

# % = modulus # restul impartirii la 2
# se foloseste pentru sirul Fibonaci

print('----operatori de comparatie-----------------')

print(i == j)  # egal
print(i != j)  # diferit
print(i > j)  # mai mare
print(i < j)  # mai mic
print(i >= j)  # mai mare sau egal
print(i <= j)  # mai mic sau egal
print('---------------------------------------------')
print('A' == 'A')
print('a' > 'b')  # rezultatul arata care e mai mare in cod binar
print(False < True)  # probabil false = 0 si True = 1
print(False == 0)
# ascii standard american
print(1.1 > 1)

print('-----------operatori logici-------------')

k = 5
y = 10

print(k < 5 and k < y)  # e nevoie sa fie ambele True
# and nu are limita
print(k == 5)  # returneaza True
print(k == 5 and k <= 5)  # returneaza True
print(k != 5 and k <= 5)  # returneaza False
print(k == 5 or k < 5)  # returneaza True

print(not(k != 5)) # transforma True in False si invers
# not inverseaza boolean

print('-----flow control --------- if -------')

nota = 2
nota_x = (float(input()))
if nota > nota_x:
    print('ok')
print('lolol')

nota_de_trecere = 4.5
nota = float(input("alege nota"))
if nota > nota_de_trecere:
    print(f'ai luat nota {nota}')
    print(f'Felicitari')

# atunci cand nu trece de operator = nu printeaza nimic si nu da eroare

# if nota > nota_de_trecere:   # daca pui IF NOT este reversul
#     print(f'ai luat nota {nota}')
#     print(f'Felicitari')
# else:
#     print(f'nasoleanuuu ...{nota}')
#     print(f'nu mergi la mare')


if nota > nota_de_trecere:   # daca pui IF NOT este reversul
    print(f'ai luat nota {nota}')
    print(f'Felicitari')
elif nota == nota_de_trecere:
    print(f'ai luat nota {nota} ce noroc')
    print(f'Felicitari')
else:
    print(f'nasoleanuuu ...{nota}')
    print(f'nu mergi la mare')


