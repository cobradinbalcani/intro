# LOOP - while, while else, for, for each
# control iteratii cu BREAK si CONTINUE

# WHILE = periculos

# ploua = True
# i = 0
# while ploua:
#     print('go')
#     i += 1
#     if i == 3:
#         ploua = False
#         print('nu mai ploua')
#
# print('-------------------------------')
#
# numar = 0
# while numar in range(0, 7):
#     print(numar)
#     numar += 1
#
# print('-----------------------')
#
# i = 0
# while i <= 3:
#     print(i)
#     i += 1
#
# print('------------------------------')
#
#
# i = 0
# while i <= 9:
#     print('deasupra if ului', i)
#     if i == 5:
#         break
#     print('dupa if', i)
#     i += 1
# else:
#     i = 0
#     print('i-ul in else', 0)
#
# print('------------------------------')
#
# # FOR / FOR ELSE - folosim des in viata de zi cu zi
#
# for i in range(4):
#     print(i)
#
# print('------------------------------')
#
# for numar in range(0, 10):
#     print(numar)
#
# print('------------------------------')
#
# for numar in range(-5, 3):
#     print(numar)
#
#
# print('------------------------------')

# lista_1 = [1, 2 ,3 ,4]
# lista_2 = [3 ,4, 5, 6]
#
# for nr_lista_1 in lista_1:
#     print()
#     for nr_lista_2 in lista_2:
#         if nr_lista_1 == nr_lista_2:
#             print(nr_lista_1)
#
# print('------------------------------')
# lista_culori = []
# culori = ['rosu', 'albastru', 'verde', 'violet', 'galben', 'orange']
#
# for culoare in culori:
#     if culoare == 'rosu':
#         lista_culori.append(culoare)
#     if culoare == 'verde':
#         lista_culori.append(culoare)
#     if culoare == 'galben':
#         lista_culori.append(culoare)
#     print(lista_culori)
#
# print('------------------------------')
#
# lista_culori = []
# culori = ['rosu', 'albastru', 'verde', 'violet' ,'galben', 'orange']
# #
# #
# for culoare in culori:
#     for c in ['rosu', 'galben', 'verde']:
#         if culoare in ['rosu', 'galben', 'verde']:
#             if culoare == c:
#                 lista_culori.append(c)
# print(lista_culori)
#
#
# # LIST COMPREHENSION
#
#
# # l_numere = [num for num in range(0, 10) if num <= 5]
# #
# # print(l_numere)
#
# culori = ['rosu', 'albastru', 'verde', 'violet', 'galben', 'orange']
# culori_noi = [c for c in culori if c in ['rosu', 'galben', 'verde']]
# print(culori_noi)

print('---------------------------------')

cont_emag = {'user_name1': 'user',
             'password2': 'pass',
             'nume3': 'gog',
             'prenume4': 'mog',
             'varsta5': 'multi',
             'email6': 'mail@email.ro'}

for item in cont_emag.items():               # printeaza tot timpul cheile din dict, daca nu e alta conditie
    print(item)


for item in cont_emag.items():               # printeaza tot timpul cheile din dict, daca nu e alta conditie
    print(item[1]), item[0]






print('---------------------------------')