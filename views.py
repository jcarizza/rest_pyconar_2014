import json
from flask import (
    Flask,
    Response,
    request
)

from models import (
    Mochila,
    Pokebola,
    Pokemon
)
from api.serializadores import (
    SerializadorMochila,
    SerializadorPokebola,
    SerializadorPokemon
)

app = Flask(__name__)

STATUS_NOT_FOUND = 404
STATUS_CREATED = 201
STATUS_OK = 200
STATUS_SERVER_ERROR = 500


@app.route("/api/mochilas", methods=["POST", "GET"])
def mochilas():
    if request.method == "GET":
        return Response(
            SerializadorMochila(Mochila.select(), many=True).data,
            status=STATUS_OK,
            mimetype="application/json"
        )
    elif request.method == "POST":
        attrs = json.loads(request.data.decode("utf8"))
        serializador = SerializadorMochila(attrs=attrs)
        serializador.save()
        return Response(
            serializador.data,
            status=STATUS_CREATED,
            mimetype="application/json"
        )


@app.route("/api/mochilas/<mochila_id>", methods=["PUT", "GET"])
def mochila(mochila_id):
    if request.method == "GET":
        try:
            return SerializadorMochila(Mochila.get(Mochila.id == mochila_id)).data
        except:
            return Response(status=STATUS_NOT_FOUND)
    elif request.method == "PUT":
        attrs = json.loads(request.data.decode("utf8"))
        mochila = Mochila.get(Mochila.id == mochila_id)
        serializador = SerializadorMochila(mochila, attrs=attrs)
        serializador.save()
        return Response(
            serializador.data,
            status=STATUS_CREATED,
            mimetype="application/json"
        )


@app.route("/api/mochilas/<mochila_id>/pokebolas", methods=["GET"])
def pokebolas_en_mochila(mochila_id):
    return SerializadorPokebola(
        Pokebola.filter(Pokebola.mochila == mochila_id),
        many=True
    ).data


@app.route("/api/pokebolas", methods=["POST", "GET"])
def pokebolas():
    if request.method == "GET":
        return Response(
            SerializadorPokebola(Pokebola.select(), many=True).data,
            status=STATUS_OK,
            mimetype="application/json"
        )
    elif request.method == "POST":
        attrs = json.loads(request.data.decode("utf8"))
        serializador = SerializadorPokebola(attrs=attrs)
        serializador.save()
        return Response(
            serializador.data,
            status=STATUS_CREATED,
            mimetype="application/json"
        )

@app.route("/api/pokebolas/<pokebola_id>", methods=["PUT", "GET"])
def pokebola(pokebola_id):
    if request.method == "GET":
        try:
            return SerializadorPokebola(Pokebola.get(Pokebola.id == pokebola_id)).data
        except:
            return Response(status=STATUS_NOT_FOUND)
    elif request.method == "PUT":
        attrs = json.loads(request.data.decode("utf8"))
        pokebola = Pokebola.get(Pokebola.id == pokebola_id)
        serializador = SerializadorPokebola(pokebola, attrs=attrs)
        serializador.save()
        return Response(
            serializador.data,
            status=STATUS_CREATED,
            mimetype="application/json"
        )


@app.route("/api/pokemons", methods=["POST", "GET"])
def pokemons():
    if request.method == "GET":
        return Response(
            SerializadorPokemon(Pokemon.select(), many=True).data,
            status=STATUS_OK,
            mimetype="application/json"
        )
    elif request.method == "POST":
        attrs = json.loads(request.data.decode("utf8"))
        serializador = SerializadorPokemon(attrs=attrs)
        serializador.save()
        return Response(
            serializador.data,
            status=STATUS_CREATED,
            mimetype="application/json"
        )


@app.route("/api/pokemons/<pokemon_id>", methods=["PUT", "GET"])
def pokemon(pokemon_id):
    if request.method == "GET":
        try:
            obj = Pokemon.get(Pokemon.id == pokemon_id)
            return SerializadorPokemon(obj).data
        except Pokemon.DoesNotExist:
            return Response(status=STATUS_NOT_FOUND)

    elif request.method == "PUT":
        attrs = json.loads(request.data.decode("utf8"))
        pokebola = Pokemon.get(Pokemon.id == pokemon_id)
        serializador = SerializadorPokemon(pokebola, attrs=attrs)
        serializador.save()
        return Response(
            serializador.data,
            status=STATUS_CREATED,
            mimetype="application/json"
        )


if __name__ == "__main__":
    app.run(port=3000, debug=True)
