# Liste

# fructe = ['mere', 'pere', 'cirese', []]
# # #exemplu_lista = fructe
# exemplu_lista = ['Andrei', False, fructe, -1]
# # alte_fructe = []       # lista goala
# # lista_goala = list()   # lista goala
# # # print(fructe)
# # # print(lista_goala)
# # # print(alte_fructe)
# print(exemplu_lista)
# print(exemplu_lista[2])
# # # # print(exemplu_lista[2][0])
# print(exemplu_lista[2][0][-2])
# #
# # print(len(fructe))
#
# if 'mere' and [] in fructe:
#     print('avem mere si lista goala')
#
# # if alte_fructe:              # verificam daca lista contine elemente
# #     print(fructe)           # avem True
# # else:                      # avem False
# #     print("nu avem lista")
# #
# # print(len(alte_fructe))
# # if len(alte_fructe):
# #     print('daca avem ceva')
# # else:
# #     print('true')
#
# if fructe in exemplu_lista:
#     print('avem fructe')
# #
# exemplu_lista.insert(0, True)
# print(exemplu_lista)
# print(type(exemplu_lista))
# # dictionare   (cheile sunt unice, valori pot exista duplicate)
#
# cumparaturi = {'mancare':['sunca','oua'],
#                'lactate':'lapte',
#                'apa': 'dorna',
#                'detergent': False}
# # user_name = input('User: ')
# # password = input('Password: ')
# # nume = input('Nume: ')
# # prenume = input('Preume: ')
# # varsta = int(input('varsta: '))
#
# cont_olx =  {'user_name': 'user_name',
#              'password': 'password',
#              'nume': 'nume',
#              'prenume': 'prenume',
#              'varsta': 'varsta',
#              'email': 'mail@email.ro'}
# print(cont_olx)
# print(cont_olx['varsta'])
# print(cont_olx.get('varsta'))
# print(cont_olx['varsta'])
# print(cont_olx.get('email', 'contact_support@olx.ro'))
# if cont_olx.get('email') is not None:
#     print(cont_olx['email'])
#
# cont_emag = {'user_name1': 'user',
#              'password2': 'pass',
#              'nume3': 'gog',
#              'prenume4': 'mog',
#              'varsta5': 'multi',
#              'email6': 'mail@email.ro'}
#
# #print({cont_olx} + {cont_emag})  # nu se pot aduna dicturile
#
# cont_emag.update({'cheie': 'valoare'})   # echivalent append pt liste
# print(cont_emag)                       # cu update putem adauga alt element
#
# cont_emag.update(cont_olx)   # asa putem lipi 2 dicturi
# print(cont_emag)
# print(cont_emag.keys())
# print(type(cont_emag.values()))
# print(type(list(cont_emag.values())))
#
# print(cont_olx.items())
# cont_olx['adresa'] = 'via roma'
# print(cont_olx)
# cont_olx.pop('user_name')
# print(cont_olx)
# del cont_olx['password']
# print(cont_olx)
# cont_olx['nume'] = 'adrianos'  # suprascriem valoare
# cont_olx['nume'] = 123         # adaugam alta valoare ca int
# print(cont_olx)


# SET

#ex_set = dict()    # dict
#ex_set = {}        # dict
#ex_set = set()      # set si dict au aceleasi acolade

# ex_set = {1,3,4,4,3,6,8,0}    # ordonate in cod binar
# print(ex_set)
#
# ex = {'a', 'c', 'b'} # nu face ordine alfabetica
# print(ex)
# print(len(ex))
# print(set('112233'))
# print(sorted(set(ex)))

# TUPLE

tupla = ('exemplu', 'list','tupla')

print(list(tupla))
print(tupla[0])
print(len(tupla))


# recapitulare

ex_lista = ['mere', 'pere', 'prune']

ex_lista[0] = 'cirese'
print(ex_lista)
tupla_des_intalnita = (ex_lista)    # in interiorul tuplei se pot adauga dicturi
# ex_dict = {}
# ex_set = {}
# ex_tupla = ()



from collections import deque

stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack:')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
# print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty

# Initializing a queue
queue = []

# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

# Uncommenting print(queue.pop(0))
# will raise and IndexError
# as the queue is now empty
