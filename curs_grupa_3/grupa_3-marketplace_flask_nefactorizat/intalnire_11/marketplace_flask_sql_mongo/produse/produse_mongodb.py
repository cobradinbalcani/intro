from baza_de_date.mongo_db import MongoDB
from datetime import datetime
from pytz import country_timezones, timezone
from common.utils import genereaza_id
from baza_de_date.mongo_models.products_mongo_db_model import ProductsMongoDBModel


def listeaza_produs_flask_mongo(id_produs):
    db = MongoDB()
    product = db.get_product_by_id(id_produs)
    if not product:
        return 404, f"Produs-ul {id_produs} nu se afla in baza de date"
    return 200, product


def adauga_un_produs_flask_mongo(request_body):
    db = MongoDB()
    if db.get_product_by_name(request_body["product_name"]):
        return 400, f"Produs-ul cu numele {request_body['product_name']} deja exista in baza de date"
    id_produs = genereaza_id({request_body["product_name"]: request_body["product_quantity"]})
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0])).isoformat()
    request_body["id_produs"] = id_produs
    request_body["data_inregistrare"] = data_inregistrare
    product_model = ProductsMongoDBModel(**request_body)
    id_produs = db.create_product(product_model)
    return 201, f"Order: {id_produs} has been successfully added"


def listeaza_toate_produsele_flask_mongo():
    db = MongoDB()
    product_list = db.list_all_products()
    if not product_list:
        return 404, "Nu exista produse"
    return 200, product_list


def sterge_un_produs_flask_mongo(id_produs):
    db = MongoDB()
    if not db.get_user_by_id(id_produs):
        return 404, f"Produs-ul {id_produs} nu se afla in baza de date"
    db.delete_product_by_id(id_produs)
    return 200, f"Successfully deleted product {id_produs}"
