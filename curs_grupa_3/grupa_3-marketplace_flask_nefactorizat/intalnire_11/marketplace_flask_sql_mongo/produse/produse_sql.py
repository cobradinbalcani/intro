from datetime import datetime
from pytz import country_timezones, timezone
from baza_de_date.sql import SQLiteDatabaseConnection
from common.utils import genereaza_id
from baza_de_date.sql_models.products_sql_db_model import ProductsSQLDBModel


def listeaza_produs_flask_sql(id_produs):
    db = SQLiteDatabaseConnection()
    with db:
        product = db.get_product_by_id(id_produs)
        if not product:
            return 404, f"Produs-ul {id_produs} nu se afla in baza de date"
        product = product.serialize()
    return 200, product


def adauga_un_produs_flask_sql(request_body):
    db = SQLiteDatabaseConnection()
    with db:
        if db.get_product_by_name(request_body["product_name"]):
            return 400, f"Produs-ul cu numele {request_body['product_name']} deja exista in baza de date"
    id_produs = genereaza_id({request_body["product_name"]: request_body["product_price"]})
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    request_body["id_produs"] = id_produs
    request_body["data_inregistrare"] = data_inregistrare
    produs_model = ProductsSQLDBModel(**request_body)
    with db:
        id_produs = db.create_product(produs_model)
    return 201, f"Product: {id_produs} has been successfully added"


def listeaza_toate_produsele_flask_sql():
    db = SQLiteDatabaseConnection()
    with db:
        product_list = ProductsSQLDBModel.serialize_list(db.list_all_products())
        if not product_list:
            return 404, "Nu exista produse"
    return 200, product_list


def sterge_un_produs_flask_sql(id_produs):
    db = SQLiteDatabaseConnection()
    with db:
        rows = db.delete_product_by_id(id_produs)
    if rows == 0:
        return 404, f"Produs-ul {id_produs} nu se afla in baza de date"
    return 200, f"Successfully deleted the product {id_produs}"
