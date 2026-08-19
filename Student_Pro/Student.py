from human import Human

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, rekord_book):
        super().__init__(gender, age, first_name, last_name)
        self.rekord_book = rekord_book
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.rekord_book}"
    def __eg__(self, other):
        if not isinstance(other, Student):
            return False
        return str(self) == str(other)
    def __hash__(self):
        return hash(str(self))