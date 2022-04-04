"""

Produsele ar trebui sa aiba structura:
("id_produs": {
    "nume_produs": "NumeleProdusului" - string,
    "pret": "Pret" - intreg/float,
    "data_inregistrare": "DataInregistrare" - string,
})

"""
import hashlib

from datetime import datetime
from pprint import pprint

from pytz import country_timezones, timezone

from marketplace.baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date


def genereaza_id_produs(nume_produs, pret):
    hash_object = hashlib.md5(bytes(nume_produs + str(pret), encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def adauga_un_produs():
    '''
    Introdu de la tastatura cu textul 'Introduceti numele produsului de adaugat: '
        Daca limitele lungimii numelui unui produs e intre 1 si 50 caractere
        Daca nu se incadreaza printati 'Nume Invalid - Lungimea numelui trebuie sa fie intre 1 si 50 de caractere'
    Introdu de la tastatura cu textul 'Introduceti pretului produsului de adaugat: '
    Generam ID-ul unic produsului
    Generam data inregistrarii
    Citim din baza de date
    Generam structura dictionarului
    Scriem in baza de date
    '''

    nume_produs = ''
    pret = 4

    while len(nume_produs) < 1 or len(nume_produs) > 50:
        nume_produs = input('Introduceti numele produsului de adaugat: \n')
        if len(nume_produs) < 1 or len(nume_produs) > 50:
            print('Invalid, trebuie sa fie intre 1 si 50 caractere.')

    if pret:
        pret = abs(float(input('Introduceti pretul produsului de adaugat: \n')))

    id_produs = genereaza_id_produs(nume_produs, pret)
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    datele_noastre = citeste_datele_din_baza_de_date()
    datele_noastre["produse"][id_produs] = {
        "nume": nume_produs,
        "pret": pret,
        "data_inregistrare": data_inregistrare.isoformat()   # sau str(data_inregistrare)
    }
    scrie_datele_in_baza_de_date(datele_noastre)


def listeaza_toate_produsele():
    """
    Functia trebuie sa afiseze toate produsele prezente in baza de date.
    Afisarea ar trebui sa contina toate informatiile produselor
    """
    datele_noastre = citeste_datele_din_baza_de_date()
    produse = datele_noastre['produse']
    if produse:
        pprint(produse)
    else:
        print('Nu exista produse!')


def sterge_produs():
    produs_de_sters = input('Introduceti id pt sters: \n')
    datele_noastre = citeste_datele_din_baza_de_date()
    datele_noastre['produse'].pop(produs_de_sters)
    scrie_datele_in_baza_de_date(datele_noastre)