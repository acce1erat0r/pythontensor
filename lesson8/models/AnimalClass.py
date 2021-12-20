# Задание 1
class Animals(object):
    def __init__(self, name, color, weight):
        self._color = color
        self._name = name
        self._weight = weight

    # getters method
    def get_color(self):
        return self._color

    def get_name(self):
        return self._name

    def get_weight(self):
        return self._weight

    # setters method

    def set_weight(self, weight):
        self._weight = weight

    # property
    Name = property(get_name)
    Color = property(get_color)
    Weight = property(get_weight, set_weight)

    # animals  method

    def move(self):
        print(f'{self._name} двигается')

    def breathe(self):
        print(f'{self._name} дышит')
