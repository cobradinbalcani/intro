from pymongo import MongoClient
from urllib import parse
from baza_de_date.mongo_models.users_mongo_db_model import UsersMongoDBModel
from baza_de_date.mongo_models.products_mongo_db_model import ProductsMongoDBModel
from baza_de_date.mongo_models.orders_mongo_db_model import OrdersMongoDBModel
from pathlib import Path
import os
with open(Path(os.path.dirname(os.path.abspath(__file__)), "db_pwd_mongo.txt"), "r") as password_file:
    #connection_url = f"mongodb+srv://mongo_test:{parse.quote_plus(password_file.readline())}@itf.x5m6f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    connection_url = f"mongodb+srv://mongo_test:{parse.quote_plus(password_file.readline())}@cluster0.cjqyd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"


class MongoDB:
    client = MongoClient(connection_url, tls=True, tlsAllowInvalidCertificates=True)
    db = client["cluster0"]
    collection = db["cluster0_collection"]

    # -------------------------------------------CREATE--------------------------------------

    def create_user(self, user_model: UsersMongoDBModel):
        print(user_model.__dict__)
        self.collection.insert_one(user_model.__dict__)
        return user_model._id

    def create_product(self, product_model: ProductsMongoDBModel):
        print(product_model.__dict__)
        self.collection.insert_one(product_model.__dict__)
        return product_model._id

    def create_order(self, order_model: OrdersMongoDBModel):
        print(order_model.__dict__)
        self.collection.insert_one(order_model.__dict__)
        return order_model._id

    # -------------------------------------------GET--------------------------------------

    def get_user_by_id(self, user_id):
        result = self.collection.find_one({"_id": user_id})
        return result

    def get_product_by_id(self, id_produs):
        result = self.collection.find_one({"_id": id_produs})
        return result

    def get_order_by_id(self, id_comanda):
        result = self.collection.find_one({"_id": id_comanda})
        return result

    def get_user_by_email(self, email):
        result = self.collection.find(filter={"email_address": email})
        return list(result)

    def get_product_by_name(self, name):
        result = self.collection.find(filter={"product_name": name})
        return list(result)

    def get_order_by_name(self, name):
        result = self.collection.find(filter={"order_name": name})
        return list(result)

    # -------------------------------------------LIST ALL--------------------------------------

    def list_all_users(self):
        result = self.collection.find(filter={"user_name": {"$exists": 1}})
        return list(result)

    def list_all_products(self):
        result = self.collection.find(filter={"product_name": {"$exists": 1}})
        return list(result)

    def list_all_orders(self):
        result = self.collection.find(filter={"order_name": {"$exists": 1}})
        return list(result)

    # -------------------------------------------DELETE--------------------------------------

    def delete_user_by_id(self, user_id):
        self.collection.delete_one({"_id": user_id})

    def delete_product_by_id(self, id_produs):
        self.collection.delete_one({"_id": id_produs})

    def delete_order_by_id(self, id_comanda):
        self.collection.delete_one({"_id": id_comanda})

