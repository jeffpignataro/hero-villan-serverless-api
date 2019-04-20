from models.shared.person import Person
from models.villan.villan import Villan


class Hero(object):
    def __init__(self, person: Person, alias, powers, archenemy: Villan):
        self.realname = person.name
        self.age = person.age
        self.alias = alias
        self.powers = powers
        self.archenemy = archenemy
