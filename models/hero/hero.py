from models.shared.person import Person
from models.villain.villain import Villain


class Hero(object):
    def __init__(self, person: Person, alias, publisher, archenemy: Villain):
        self.realname = person.name
        self.characters = person.characters
        self.alias = alias
        self.publisher = publisher
        self.archenemy = archenemy
