from models.AnimalClass import Animals
from models.MammalsClass import Mammals


class Human(Mammals):
    def __init__(self, name, color, weight, is_warm_bloodedness=True, has_wool=True, can_speak=True, bipedal=True):
        super().__init__(name, color, weight, is_warm_bloodedness, has_wool)
        self._can_speak = can_speak
        self._bipedal = bipedal

    # getters method
    def can_speak(self):
        return self._can_speak

    def bipedal(self):
        return self._bipedal

    # property
    # приходится прописывать через Animals, ибо не могу получить доступ к полю name у Mammals
    Name = property(Animals.get_name)
    Color = property(Animals.get_color)
    Weight = property(Animals.get_weight, Animals.set_weight)
    Wool = property(Mammals.is_has_wool)
    Warm_blood = property(Mammals.is_warm_blood)
    Speaking = property(can_speak)
    Bipedal = property(bipedal)

    # method
    def speak(self):
        if self.Speaking:
            print(f"{self.Name} говорит")

    def walking(self):
        if self.Bipedal:
            print(f'{self.Name} ходит')
