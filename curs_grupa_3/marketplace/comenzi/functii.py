"""
Comenzile ar trebui sa aiba structura:
("id_comanda": {
    "id_comanda": "Idcomanda" - string,
    "detalii_comanda":
        [{"IdProdus": CantitateProdus}]
        - lista de dictionare de forma IdProdus (string): CantitateProdus (numar intreg),
    "data_inregistrare": "DataInregistrare" - string,
})

"""
import hashlib
import json

from datetime import datetime
from pprint import pprint

from pytz import country_timezones, timezone

from marketplace.baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date


def genereaza_id_comanda(detalii_comanda):
    hash_object = hashlib.md5(bytes(json.dumps(detalii_comanda), encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def adauga_o_comanda():
    """
    Introdu de la tastatura cu textul: "Introduceti produsele din comanda. Pentru a termina, introduceti 'stop':\n"
    Ca prim input dam Produsul, apoi Cantitatea
    Generam ID-ul unic comenzii
    Generam data inregistrarii
    Citim din baza de date
    Generam structura dictionarului
    Scriem in baza de date
    """

    actiune = None
    while actiune != 'stop':
        id_produs = input('Introduceti produsele din comanda: \n')
        cantitate_produs = abs(int(input('Introduceti cantitatea produsului din comanda: \n')))
        actiune = input('Daca ai terminat introdu textul:"stop" in schimb pentru a continua, apasa tasta "enter". \n')
        detalii_comanda = [{id_produs: cantitate_produs}]
        id_cmd = genereaza_id_comanda(detalii_comanda)

        data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
        datele_noastre = citeste_datele_din_baza_de_date()
        datele_noastre["comenzi"][id_cmd] = {
            "id_comanda": id_cmd,
            "detalii_comanda": detalii_comanda,
            "data_inregistrare": data_inregistrare.isoformat() # sau str(data_inregistrare)
        }
        scrie_datele_in_baza_de_date(datele_noastre)


def modifica_comanda():
    """
    Introduceti de la tastatura textul: "Introduceți identificatorul comenzii care se modifica: "
    Creeam o logica care sa primeasca ca input de la tastatura 4 variante de actiune:
        "Alegeti actiunea ('a' - adaugare produs; 'm ' - modificare cantitate; 's'-sterge produs, 'e'-exit \n")
        Creeam logica pentru cele 4 variante
        Ca input trebuie sa dam produsul si cantitatea pentru 'a' si 'm', pentru 's' dam identificatorul
        Din nou, Citim, Actionam, Scriem
    """


    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    datele_noastre = citeste_datele_din_baza_de_date()
    identificatorul = input('Introduceți identificatorul comenzii care se modifica: \n')
    if identificatorul in datele_noastre['comenzi']:
        print('Alegeti actiunea ("a" - adaugare produs; "m" - modificare cantitate; "a" -sterge produs, "e" -exit \n')
        id_produs = ''


        actiune = ''
        while actiune != 'e':
            actiune = input('\n')
            if actiune == 'e':
                pass
            elif actiune == 'a':

                while len(id_produs) < 1 or len(id_produs) > 50:
                    id_produs = input('Introduceti numele produsului de adaugat: \n')
                    if len(id_produs) < 1 or len(id_produs) > 50:
                        print('Nume invalid, trebuie sa aiba intre 1 si 50 de caractere')
                cantitate_produs = abs(int(input('Introduceti cantitatea produsului din comanda: \n')))
                detalii_comanda = [{id_produs: cantitate_produs}]
                datele_noastre['comenzi'][identificatorul] = {
                "id_comanda": identificatorul,
                "detalii_comanda": detalii_comanda,
                "data_inregistrare": data_inregistrare.isoformat() # sau str(data_inregistrare)
                 }
                print("Alegeti actiunea ('a' - adaugare produs; 'm ' - modificare cantitate; 's'-sterge produs, 'e'-exit \n")
            elif actiune == "m":
                while len(id_produs) < 1 or len(id_produs) > 50:
                    id_produs = input('Introduceti numele produsului de adaugat: \n')
                    if len(id_produs) < 1 or len(id_produs) > 50:
                        print('Invalid, trebuie sa fie intre 1 si 50 caractere.')
                cantitate_produs = abs(int(input('Introduceti cantitatea produsului din comanda: \n')))
                detalii_comanda = [{id_produs: cantitate_produs}]
                datele_noastre["comenzi"][identificatorul] = {
                "id_comanda": identificatorul,
                "detalii_comanda": detalii_comanda,
                "data_inregistrare": data_inregistrare.isoformat() # sau str(data_inregistrare)
                }
                print("Alegeti actiunea ('a' - adaugare produs; 'm ' - modificare cantitate; 's'-sterge produs, 'e'-exit \n")
            elif actiune == 's':
                datele_noastre['comenzi'].pop(identificatorul)
                print('Alegeti actiunea ("a" - adaugare produs; "m" - modificare cantitate; "s" -sterge produs, "e" -exit \n')
            else:
                actiune = input('\n')
    else:
        print('Identificator gresit')


    scrie_datele_in_baza_de_date(datele_noastre)


def listeaza_toate_comenzile():
    """
    Functia trebuie sa afiseze toate comenzile prezente in baza de date.
    Afisarea ar trebui sa contina toate informatiile comenzilor
    """
    datele_noastre = citeste_datele_din_baza_de_date()
    comenzi = datele_noastre['comenzi']
    if comenzi:
        pprint(comenzi)
    else:
        print('Nu exista comenzi!')


def sterge_o_comanda():
    """
    Introdu de la tastatura cu textul  "Introduceți identificatorul comenzii de sters: "
    Cititi, stergeti, Scrieti

    """

    cmd_de_sters = input('Introduceti id pt sters: \n')
    datele_noastre = citeste_datele_din_baza_de_date()
    datele_noastre['comenzi'].pop(cmd_de_sters)
    scrie_datele_in_baza_de_date(datele_noastre)
