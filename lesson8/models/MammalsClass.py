from models.AnimalClass import Animals


class Mammals(Animals):
    def __init__(self, name, color, weight, is_warm_bloodedness=True, has_wool=True):
        super().__init__(name, color, weight)
        self._is_warm_blood = is_warm_bloodedness
        self._has_wool = has_wool

    # getters method
    def is_has_wool(self):
        return self._has_wool

    def is_warm_blood(self):
        return self._is_warm_blood()

    # property
    # Я так понимаю в python из класса наследника нельзя получить доступ к свойствам ?
    Name = property(Animals.get_name)
    Color = property(Animals.get_color)
    Weight = property(Animals.get_weight, Animals.set_weight)
    Wool = property(is_has_wool)
    Warm_blood = property(is_warm_blood)

    # method

    def feed_milk(self):
        print(f"{self.Name} вскармливает своих детенышей молоком")

    def get_shed(self):
        if self.Wool:
            print(f'{self.Name} сбросило шерсть')
        else:
            print("У животного нет шерсти, возможно оно сбросило шерсть ранее")
