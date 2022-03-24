# comentariu one line cu diez in fata
'''
varianta 2: comentariu pe mai multe linii
'''

# ctrl+D = copiaza linia direct sub unde ai pus cursorul mouse

# print('Hello World')
# print('Hello IT-Factory')
# # print('Hello World')
# print('Hello IT-Factory')
# marca_masina = 'Audi'
# print(marca_masina)
# marca_masina = 'BMW'   #suprascriere
# print(marca_masina)

# integer
# marca_masina = 3
# marca_masina = 3.14
# print(marca_masina)

x, y, z, t = 'mere', 'pere', 'portocale', 'alune'
# print(x)
# print(y)
# print(z)
# print(x,y,z, z, y)
#
# my_var = 'mere 21 dec'
# print(my_var)
# my_var_2 = 'mc\'donalds' #sau
# my_var_2 = "mc'donalds"
# print(my_var_2)
#
# my_var_3 = True
# print(my_var_3)
#
# my_var_4 = my_var
# print(my_var_4)
# print(my_var)

# ctrl + alt + L ajuta la formatarea paginii in python

# print(x, type(x))  # citeste din interior catre exterior
# variabila = (variabila)# dublu click daca uiti sa pui paranteze si pui doar prima si se pune in automat

# cifra = 15.8234
# cifra = int(cifra)
# cifra = str(cifra)
# print(cifra, type(cifra))
# print(str(cifra))

# cifra_2 = 3.14160000
# print(cifra_2-1)
#
var_1 = 'ana'
var_2 = ' are '  # merge si cu spatiu direct de aici
var_3 = 'mere'
print(f'{var_1} {var_2} {var_3}')
print(var_1 + ' ' + var_2 + ' ' + var_3)

variabila_formatata = f'NUmele meu este {var_1} si am {var_3}'
#variabila_formatata_arhaic = f'NUmele meu este {0} si am {1}'.format('ana', 'mere')
print(variabila_formatata)
# print()
#print(variabila_formatata_arhaic)
#
# print(input('Va rog introd varsta: ')) #merge din int parantezei si apoi afara
# print('hellloooo')
# nume = input("numele_meu")
# print(int(input(nume)))

'''
slice = '' # exemplu gresit, mai bine scrii exact numele ca mai jos
index_example = 'aNAmaria are mere'
print(index_example[0:3]) #apelez n-ul
print(index_example[-1]) #apelez e-ul de la final
print(index_example[-4:]) # apelez mere

print(index_example[4:]) # nu printeaza primele
print(index_example[3:6]) #printez mar din anamaria
print(index_example[(2 + 3)]) #aduna si da caracterul 6 pt ca index este de la zero

print(len(index_example))

lup = 'Lupul'
print(lup.upper())
print(lup.lower())
print(index_example.replace('mere', 'pere'))
print(index_example.capitalize())
print(index_example.title())
'''
x = str(input('String de la tastatura: '))  # citesc string de la tastatura
first = (x[:1])  # salvez primul caracter in variabila
last = (x[-1:]) # salvez ultimul caracter in variabila
x_troncat = x[1:-1]
x_final = (x_troncat.replace(first, first.upper()))  # acest caracter se capitalizeaza peste tot
print(first + x_final + last)
