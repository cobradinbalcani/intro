import hashlib
import json
from marketplace_v2.marketplace_2.baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date
from pprint import pprint


def genereaza_id(detalii_comanda):
    hash_object = hashlib.md5(bytes(json.dumps(detalii_comanda), encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

def sterge(identificator_de_sters, key):
    datele = citeste_datele_din_baza_de_date()
    datele[key].pop(identificator_de_sters)
    scrie_datele_in_baza_de_date(datele)

def listeaza(key):
    """
    Functia trebuie sa afiseze toate comenzile prezente in baza de date.
    Afisarea ar trebui sa contina toate informatiile comenzilor
    """

    datele = citeste_datele_din_baza_de_date()
    listare = datele[key]
    if listare:
        pprint(listare)
    else:
        print(f"Nu exista {key}")