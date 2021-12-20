from models.HumanClass import Human


class Student(Human):
    def __init__(self, name, color, weight, home_work_count, is_warm_bloodedness=True, has_wool=True, can_speak=True,
                 bipedal=True):
        super().__init__(name, color, weight, is_warm_bloodedness, has_wool, can_speak, bipedal)
        self._home_work_count = home_work_count

    # getters method
    def get_homework_count(self):
        return self._home_work_count

    # setters method
    def set_homework_count(self, count):
        self._home_work_count = count

    # property
    Homework_count = property(get_homework_count)

    # methods
    def __lt__(self, student):
        if self.Homework_count < student.Homework_count:
            return self.Name
        else:
            return student.Name

    def __gt__(self, student):
        if self.Homework_count > student.Homework_count:
            return self.Name
        else:
            return student.Name

    def __eq__(self, student):
        if self.Homework_count == student.Homework_count:
            return True
        else:
            return False

