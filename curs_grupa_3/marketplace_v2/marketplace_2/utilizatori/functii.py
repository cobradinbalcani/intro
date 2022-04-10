"""

Utilizatorii ar trebui sa aiba structura:
("id_utilizator": {
    "nume": "Numele" - string,
    "email": "EmailAddress" - string,
    "data_inregistrare": "DataInregistrare" - string,
})

"""

from datetime import datetime
from pprint import pprint

from pytz import country_timezones, timezone

from marketplace_v2.marketplace_2.baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date
from marketplace_v2.marketplace_2.common.utils import genereaza_id, sterge, listeaza




def adauga_un_utilizator():
    nume, email = "", ""
    while len(nume) < 1 or len(nume) > 50:
        nume = input("Introduceti numele utilizatorului:\n")
        if len(nume) < 1 or len(nume) > 50:
            print("Nume Invalid - Lungimea numelui trebuie sa fie intre 1 si 50 de caractere")
    while len(email) < 1:
        email = input("Introduceti emailul utilizatorului:\n")

    id_utilizator = genereaza_id({
        nume: email})
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    datele = citeste_datele_din_baza_de_date()
    datele["utilizatori"][id_utilizator] = {
        "nume": nume,
        "email": email,
        "data_inregistrare": data_inregistrare.isoformat()
    }
    scrie_datele_in_baza_de_date(datele)


def listeaza_toti_utilizatorii():
    """
    Functia trebuie sa afiseze toti utilizatorii prezenti in baza de date.
    Afisarea ar trebui sa contina toate informatiile utilizatorilor
    :return:
    """
    listeaza('utilizatori')


def sterge_un_utilizator():
    identificator_de_sters = input("Introduceti identificatorul utilizatorului de sters:\n")
    sterge(identificator_de_sters, 'utilizatori')
