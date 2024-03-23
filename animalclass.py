class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        raise NotImplementedError("subclass must make sound")

    def make_move(self):
        raise NotImplementedError("subclass must move")
