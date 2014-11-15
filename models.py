from peewee import *

db = SqliteDatabase("pokebase.db")


class Mochila(Model):
    capacidad = IntegerField()

    class Meta:
        database = db

    @property
    def uri(self):
        return "/api/mochilas/%d" % (self.id,)


class Pokemon(Model):
    nombre = CharField()
    vida = IntegerField(default=100)

    class Meta:
        database = db

    @property
    def uri(self):
        return "/api/pokemons/%d" % (self.id,)

    @property
    def salvaje(self):
        return True if self.pokebola is None else False


class Pokebola(Model):
    mochila = ForeignKeyField(Mochila)
    pokemon = ForeignKeyField(Pokemon, null=True)

    class Meta:
        database = db

    @property
    def uri(self):
        return "/api/pokebolas/%d" % (self.id,)
