class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} years old"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, rekord_book):
        super().__init__(gender, age, first_name, last_name)
        self.rekord_book = rekord_book
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.rekord_book}"

class GroupOverflowError(Exception):
    def __init__(self,message="Більше 11 не може бути"):
        self.message = message
        super().__init__(self.message)

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()
    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupOverflowError(f"Не додається {student.last_name}. Група {self.number} повна по кількості")
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)
    def __str__(self):
        all_students = "\n".join([str(student) for student in self.group])
        return f"Group Number: {self.number}\n{all_students}"

gr = Group("PD1")

print("Якщо буде 11 студент")
try:
    for  i in range(11):
        new_student = Student("Male", 20 + i, f"Name{i}", f"Lastname{i}", f"Book{i}")
        gr.add_student(new_student)
        print(f"Додано: {new_student.last_name}")
except GroupOverflowError as e:
    print(f"\nПомилка: {e}")

gr.group.clear()

print("\nФінальна кількість:")

st1 = Student("Male", 30, "Steve", "Jobs", "AN142")
st2 = Student("Female", 25, "Liza", "Taylor", "AN145")
gr.add_student(st1)
gr.add_student(st2)

print(gr)

assert str(gr.find_student("Jobs")) == str(st1), "Test1"
assert gr.find_student("Jobs2") is None, "Test2"
assert isinstance(gr.find_student("Jobs"), Student) is True
gr.delete_student("Taylor")
print("\nAfter deletion:")
#print(gr)

gr.delete_student("Taylor")
