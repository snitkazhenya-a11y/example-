class Restangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Restangle):
            return self.get_square() == other.get_square()
        return False

    def __add__(self, other):
        if isinstance(other, Restangle):
            new_square = self.get_square() + other.get_square()
            new_width = self.width
            new_height = new_square / new_width
            return Restangle(new_width, new_height)
        return NotImplemented

    def __mul__(self, number):
        if isinstance(number, (int, float)):
            new_square = self.get_square() * number
            new_width = self.width
            new_height = new_square / new_width
            return Restangle(new_width, new_height)
        return NotImplemented

    def __str__(self):
        return f"Restangle(width={self.width}, height={self.height}, square={self.get_square()})"

r1 = Restangle(2, 4)
r2 = Restangle(3, 6)

assert r1.get_square() == 8, "Test1"
assert r2.get_square() == 18, "Test2"
r3 = r1 + r2
assert r3.get_square() == 26, "Test3"
r4 = r1 * 4
assert r4.get_square() == 32, "Test4"
assert Restangle(3, 6) == Restangle(2,9), "Test5"

print("Все правильно")
print(f"r1: {r1}")
print(f"r2: {r2}")
print(f"r3 (r1+r2): {r3}")
print(f"r4 (r1*4): {r4}")