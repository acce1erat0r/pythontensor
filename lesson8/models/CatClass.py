from models.AnimalClass import Animals
from models.MammalsClass import Mammals


class Cat(Mammals):
    def __init__(self, name, color, weight, is_warm_bloodedness=True, has_wool=True, lives_in_flock=False):
        super().__init__(name, color, weight, is_warm_bloodedness, has_wool)
        self._lives_in_flock = lives_in_flock

    # getters method
    def get_lives_in_flock(self):
        return self._lives_in_flock

    # property
    Name = property(Animals.get_name)
    Color = property(Animals.get_color)
    Weight = property(Animals.get_weight, Animals.set_weight)
    Wool = property(Mammals.is_has_wool)
    Warm_blood = property(Mammals.is_warm_blood)
    Live_in_flock = property(get_lives_in_flock)

    # method

    def get_purr(self):
        print("кошка мурлычет")
