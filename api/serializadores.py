import json
from models import (
    Pokemon,
    Pokebola,
    Mochila
)


class Serializador(object):

    def __init__(self, obj=None, attrs={}, many=False):
        self.obj = obj
        self.many = many
        self.attrs = attrs

    def save(self):
        if hasattr(self.obj, "id"):
            query = self.model.update(**self.attrs).where(self.model.id == self.obj.id)
            query.execute()
            self.obj = self.model.get(self.model.id == self.obj.id)
        else:
            self.obj = self.model.create(**self.attrs)

    @property
    def data(self):
        assert self.obj is not None
        if self.many:
            self.obj = [item.uri for item in self.obj]
        else:
            self.obj = self.serializar(self.obj)

        return json.dumps(self.obj)


class SerializadorMochila(Serializador):
    model = Mochila

    def serializar(self, obj):
        return {
            "id": obj.id,
            "capacidad": obj.capacidad
        }


class SerializadorPokebola(Serializador):
    model = Pokebola

    def serializar(self, obj):
        data = {"id": obj.id}
        if obj.pokemon:
            data.update({"pokemon": obj.pokemon.uri})
        return data


class SerializadorPokemon(Serializador):
    model = Pokemon

    def serializar(self, obj):
        data = {
            "id": obj.id,
            "vida": obj.vida,
            "nombre": obj.nombre
        }

        return data
