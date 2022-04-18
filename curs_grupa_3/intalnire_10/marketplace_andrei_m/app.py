import json

from flask import Flask, Response, request
from utilizatori.functii import adauga_un_utilizator_flask, listeaza_toti_utilizatorii_flask, sterge_un_utilizator_flask
from produse.functii import adauga_un_produs_flask, listeaza_toate_produsele_flask, sterge_un_produs_flask
from comenzi.functii import adauga_o_comanda_flask, modifica_o_comanda_flask, listeaza_toate_comenzile_flask, sterge_o_comanda_flask

app = Flask("Marketplace API")


@app.route("/get_user/<string:user_id>", methods=["GET"])
def get_user(user_id):
    return Response(status=200, response=json.dumps({"message": f"Hello, I'm A user: {user_id}"}))


@app.route("/get_utilizator/<string:id_utilizator>", methods=["GET"])
def get_utilizator(id_utilizator):
    return Response(status=200, response=json.dumps({"message": f"Hi, I'm the user: {id_utilizator}"}))


@app.route("/get_product/<string:id_produs>", methods=["GET"])
def get_product(id_produs):
    return Response(status=200, response=json.dumps({"message": f"Hi, this is the product: {id_produs}"}))


@app.route("/get_order/<string:id_cmd>", methods=["GET"])
def get_order(id_cmd):
    return Response(status=200, response=json.dumps({"message": f"Hi, this is the order: {id_cmd}"}))


@app.route("/put_user", methods=["POST"])
def put_user():
    message = json.loads(request.data)
    user_name = message.get("user_name")
    email_address = message.get("email_address")
    if not user_name or not email_address:
        return Response(status=500, response=json.dumps({"message": "user_name or email_address is missing"}))
    if len(user_name) < 1 or len(user_name) > 50:
        return Response(status=500, response=json.dumps(
            {"message": "user_name must be longer than 1 character and less than 50 characters"}))
    id_utilizator = adauga_un_utilizator_flask(user_name, email_address)
    return Response(status=200, response=json.dumps({"message": f"User: {id_utilizator} has been successfully added"}))



@app.route("/put_utilizator", methods=["POST"])
def put_utilizator():
    message = json.loads(request.data)
    user_name = message.get("user_name")
    email_address = message.get("email_address")
    if not user_name or not email_address:
        return Response(status=500, response=json.dumps({"message": "user_name or email_address is missing"}))
    if len(user_name) < 1 or len(user_name) > 50:
        return Response(status=500, response=json.dumps(
            {"message": "user_name must be longer than 1 character and less than 50 characters"}))
    id_utilizator = adauga_un_utilizator_flask(user_name, email_address)
    return Response(status=200, response=json.dumps({"message": f"User: {id_utilizator} has been successfully added"}))


@app.route("/put_product", methods=["POST"])
def put_product():
    message = json.loads(request.data)
    product_name = message.get("product_name")
    price_tag = message.get("price_tag")
    if not product_name or not price_tag:
        return Response(status=500, response=json.dumps({"message": "product_name or price_tag is missing"}))
    if len(product_name) < 1 or len(product_name) > 50:
        return Response(status=500, response=json.dumps(
            {"message": "product_name must be longer than 1 character and less than 50 characters"}))
    id_produs = adauga_un_produs_flask(product_name, price_tag)
    return Response(status=200, response=json.dumps({"message": f"Product: {id_produs} has been successfully added"}))


@app.route("/put_order", methods=["POST"])
def put_order():
    message = json.loads(request.data)
    detalii_cmd = message.get("detalii_cmd")
    print("Introduceti produsele din comanda. Pentru a termina, introduceti 'stop':\n")
    while True:
        id_produs = input(" Produsul: ")
        if id_produs == "stop":
            break
        else:
            CantitateProdus = input(" Cantitatea: ")
            detalii_cmd[id_produs] = CantitateProdus
    id_cmd = adauga_o_comanda_flask()
    return Response(status=200, response=json.dumps({"message": f"Order: {id_cmd} has been successfully added"}))


@app.route("/list_users", methods=["GET"])
def list_users():
    response = listeaza_toti_utilizatorii_flask()
    print(response)
    return Response(status=200, response=json.dumps(listeaza_toti_utilizatorii_flask()))


@app.route("/list_utilizatorii", methods=["GET"])
def list_utilizatorii():
    response = listeaza_toti_utilizatorii_flask()
    print(response)
    return Response(status=200, response=json.dumps(listeaza_toti_utilizatorii_flask()))


@app.route("/list_products", methods=["GET"])
def list_products():
    response = listeaza_toate_produsele_flask()
    print(response)
    return Response(status=200, response=json.dumps(listeaza_toate_produsele_flask()))


@app.route("/list_orders", methods=["GET"])
def list_orders():
    # response = listeaza_toate_comenzile_flask()
    # print(response)
    return Response(status=200, response=json.dumps(listeaza_toate_comenzile_flask()))


@app.route("/delete_user/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    status, message = sterge_un_utilizator_flask(user_id)
    return Response(status=status, response=json.dumps({"message": message}))


@app.route("/delete_product/<string:id_produs>", methods=["DELETE"])
def delete_product(id_produs):
    status, message = sterge_un_produs_flask(id_produs)
    return Response(status=status, response=json.dumps({"message": message}))


@app.route("/delete_order/<string:id_cmd>", methods=["DELETE"])
def delete_order(id_cmd):
    status, message = sterge_o_comanda_flask(id_cmd)
    return Response(status=status, response=json.dumps({"message": message}))


@app.route("/delete_utilizator/<string:id_utilizator>", methods=["DELETE"])
def delete_utilizator(id_utilizator):
    status, message = sterge_un_utilizator_flask(id_utilizator)
    return Response(status=status, response=json.dumps({"message": message}))


if __name__ == "__main__":
    app.run()
