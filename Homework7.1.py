def say_hi(name: str = "User", age: int = 0) -> str:
    return f"Hi. My name is {name} and I'm {age} years old"
print(say_hi("Vanya",33))
print(say_hi("Olya"))
print(say_hi())