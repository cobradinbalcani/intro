import json
from flask import Flask, Response, request
from utilizatori.utilizatori_mongodb import (adauga_un_utilizator_flask_mongo, listeaza_utilizator_flask_mongo,
                                             listeaza_toti_utilizatorii_flask_mongo, sterge_un_utilizator_flask_mongo)
from produse.produse_mongodb import (adauga_un_produs_flask_mongo, listeaza_produs_flask_mongo,
                                     listeaza_toate_produsele_flask_mongo, sterge_un_produs_flask_mongo)
from comenzi.comenzi_mongodb import (adauga_o_comanda_flask_mongo, listeaza_comanda_flask_mongo,
                                     listeaza_toate_comenzile_flask_mongo, sterge_o_comanda_flask_mongo)


app = Flask("Marketplace API")


@app.route("/get_user/<string:user_id>", methods=["GET"])
def get_user(user_id):
    status, message = listeaza_utilizator_flask_mongo(user_id)
    print(type(message))
    print(message)
    return Response(status=status, response=json.dumps(message))


@app.route("/get_product/<string:id_produs>", methods=["GET"])
def get_product(id_produs):
    status, message = listeaza_produs_flask_mongo(id_produs)
    print(type(message))
    print(message)
    return Response(status=status, response=json.dumps(message))



@app.route("/get_order/<string:id_comanda>", methods=["GET"])
def get_order(id_comanda):
    status, message = listeaza_comanda_flask_mongo(id_comanda)
    print(type(message))
    print(message)
    return Response(status=status, response=json.dumps(message))




@app.route("/put_user", methods=["POST"])
def put_user():
    request_body = json.loads(request.data)
    user_name = request_body.get("user_name")
    email_address = request_body.get("email_address")
    if not user_name or not email_address:
        return Response(status=500, response=json.dumps("user_name or email_address is missing"))
    if len(user_name) < 1 or len(user_name) > 50:
        return Response(status=500,
                        response=json.dumps("user_name must be longer than 1 character and less than 50 characters"))
    status, message = adauga_un_utilizator_flask_mongo(request_body)
    return Response(status=status, response=json.dumps(message))


@app.route("/put_product", methods=["POST"])
def put_product():
    request_body = json.loads(request.data)
    product_name = request_body.get("product_name")
    product_quantity = request_body.get("product_quantity")
    if not product_name or not product_quantity:
        return Response(status=500, response=json.dumps("product_name or product_quantity is missing"))
    if len(product_name) < 1 or len(product_name) > 50:
        return Response(status=500,
                        response=json.dumps("product_name must be longer than 1 character and less than 50 characters"))
    status, message = adauga_un_produs_flask_mongo(request_body)
    return Response(status=status, response=json.dumps(message))


@app.route("/put_order", methods=["POST"])
def put_order():
    request_body = json.loads(request.data)
    order_name = request_body.get("order_name")
    order_quantity = request_body.get("order_quantity")
    if not order_name or not order_quantity:
        return Response(status=500, response=json.dumps("order_name or order_quantity is missing"))
    if len(order_name) < 1 or len(order_name) > 50:
        return Response(status=500,
                        response=json.dumps("order_name must be longer than 1 character and less than 50 characters"))
    status, message = adauga_o_comanda_flask_mongo(request_body)
    return Response(status=status, response=json.dumps(message))


@app.route("/list_users", methods=["GET"])
def list_users():
    status, message = listeaza_toti_utilizatorii_flask_mongo()
    return Response(status=status, response=json.dumps(message))


@app.route("/list_products", methods=["GET"])
def list_products():
    status, message = listeaza_toate_produsele_flask_mongo()
    return Response(status=status, response=json.dumps(message))


@app.route("/list_orders", methods=["GET"])
def list_orders():
    status, message = listeaza_toate_comenzile_flask_mongo()
    return Response(status=status, response=json.dumps(message))


@app.route("/delete_user/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    status, message = sterge_un_utilizator_flask_mongo(user_id)
    return Response(status=status, response=json.dumps({"message": message}))


@app.route("/delete_product/<string:id_produs>", methods=["DELETE"])
def delete_product(id_produs):
    status, message = sterge_un_produs_flask_mongo(id_produs)
    return Response(status=status, response=json.dumps({"message": message}))


@app.route("/delete_order/<string:id_comanda>", methods=["DELETE"])
def delete_order(id_comanda):
    status, message = sterge_o_comanda_flask_mongo(id_comanda)
    return Response(status=status, response=json.dumps({"message": message}))


if __name__ == "__main__":
    app.run()
