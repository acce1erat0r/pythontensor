from models.AnimalClass import Animals
from models.MammalsClass import Mammals


class Cat(Mammals):
    def __init__(self, name, color, weight, is_warm_bloodedness=True, has_wool=True):
        super().__init__(name, color, weight, is_warm_bloodedness, has_wool)

    # property
    Name = property(Animals.get_name)
    Color = property(Animals.get_color)
    Weight = property(Animals.get_weight, Animals.set_weight)
    Wool = property(Mammals.is_has_wool)
    Warm_blood = property(Mammals.is_warm_blood)

    # method
    def get_bark(self):
        print("Собака лает")
