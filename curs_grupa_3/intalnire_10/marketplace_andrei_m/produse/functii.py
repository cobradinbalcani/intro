"""

Produsele ar trebui sa aiba structura:
("id_produs": {
    "nume_produs": "NumeleProdusului" - string,
    "pret": "Pret" - intreg/float,
    "data_inregistrare": "DataInregistrare" - string,
})

"""
from datetime import datetime

from pytz import country_timezones, timezone

from intalnire_10.marketplace_andrei_m.baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date
from intalnire_10.marketplace_andrei_m.common.utils import genereaza_id, sterge


def adauga_un_produs():
    nume_produs = ""
    pret = ""
    while len(nume_produs) < 1 or len(nume_produs) > 50:
        nume_produs = input('\nIntroduceti numele produsului de adaugat: ')
        if len(nume_produs) < 1 or len(nume_produs) > 50:
            print("Nume Invalid - Lungimea numelui trebuie sa fie intre 1 si 50 de caractere")
    while len(pret) < 1:
        pret = input('\nIntroduceti pretului produsului de adaugat: ')
    id_produs = genereaza_id([nume_produs, pret])
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    datele = citeste_datele_din_baza_de_date()
    datele["produse"][id_produs] = {
        'nume_produs': nume_produs,
        'pret': pret,
        'data_inregistrare': data_inregistrare.isoformat()
    }

    scrie_datele_in_baza_de_date(datele)


def adauga_un_produs_flask(product_name, price_tag):
    while len(product_name) < 1 or len(product_name) > 50:
        product_name = input('\nIntroduceti numele produsului de adaugat: ')
        if len(product_name) < 1 or len(product_name) > 50:
            print("Nume Invalid - Lungimea numelui trebuie sa fie intre 1 si 50 de caractere")
    while len(price_tag) < 1:
        price_tag = input('\nIntroduceti pretului produsului de adaugat: ')
    id_produs = genereaza_id({product_name: price_tag})
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    datele = citeste_datele_din_baza_de_date()
    datele["produse"][id_produs] = {
        "product_name": product_name,
        "pret": price_tag,
        "data_inregistrare": data_inregistrare.isoformat()
    }
    scrie_datele_in_baza_de_date(datele)
    return id_produs


def listeaza_toate_produsele():
    """
    Functia trebuie sa afiseze toate produsele prezente in baza de date.
    Afisarea ar trebui sa contina toate informatiile produselor
    """
    baza_de_date = citeste_datele_din_baza_de_date()
    chei_unice_produse = baza_de_date["produse"]

    print("{}\t{}\t{}".format("Produs", "Pret", "Data inregistrare"))
    print("{}\t{}\t{}".format("Produs", "Pret", "Data inregistrare"))
    for i in chei_unice_produse:
        temp = list(baza_de_date["produse"][i].values())
        print("{}\t{}\t\t{}".format(temp[0], temp[1], temp[2]))


def listeaza_toate_produsele_flask():
    """
    Functia trebuie sa afiseze toate produsele prezente in baza de date.
    Afisarea ar trebui sa contina toate informatiile produselor
    :return:
    """
    baza_de_date = citeste_datele_din_baza_de_date()
    chei_unice_produse = baza_de_date["produse"]

    print("{}\t{}\t{}".format("Produs", "Pret", "Data inregistrare"))
    print("{}\t{}\t{}".format("Produs", "Pret", "Data inregistrare"))
    for i in chei_unice_produse:
        temp = list(baza_de_date["produse"][i].values())
        return "{}\t{}\t\t{}".format(temp[0], temp[1], temp[2])


def sterge_produs():
    sterge(input("\nNume produs: "), "produse")


def sterge_un_produs_flask(product_id):
    return sterge(product_id, "produse")
