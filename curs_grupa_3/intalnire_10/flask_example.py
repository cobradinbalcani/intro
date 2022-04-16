from flask import Flask, request
import json
import pprint

app = Flask('FLASK API EXAMPLE')


@app.route("/home_page", methods=["GET"])
def home_page():
    return f"Hello, Welcome to my Homepage"


@app.route("/afisare_mesaj", methods=["POST"])
def afisare_mesaj():
    requested_messsage = json.loads(request.data)   #cu json.loads transformam din bites in format json
    print(request.data, type(request.data))
    #print(request.data.decode(), type(request.data.decode('UTF8')))   #UTF8 se fol pt decodare de simboluri / litere speciale
    return f"Hello, the message you wanted displayed is: {requested_messsage['message']}"


@app.route("/afisare_mesaj_text", methods=["POST"])
def afisare_mesaj_text():
    requested_messsage = request.data.decode()
    print(request.data, type(request.data))
    print(request.data.decode(), type(request.data.decode('UTF8')))   #UTF8 se fol pt decodare de simboluri / litere speciale
    return f"Hello, the message you wanted displayed is: {requested_messsage}"


@app.route("/get_user/<user>", methods=["GET"])
def get_user(user):
    return f"Hello, I'm user {user}"


@app.route("/delete_user/<user>", methods=["DELETE"])
def delete_user(user):
    print(user, type(user))
    return f"{user} has been deleted"


if __name__ == "__main__":
    app.run()                 #app.run(port=8000) se paote face si asa ca sa modificam in loc de 5000 - in acest mod lucram pe alt port
