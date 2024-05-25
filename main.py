class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        return f"{self.name} каже {self.sound}"

    def display_info(self):
        return f"Ім'я: {self.name}, Вік: {self.age}, Звук: {self.sound}"

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "гав-гав")
        self.breed = breed

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Порода: {self.breed}"

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, "мяу")
        self.color = color

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Колір: {self.color}"


dog = Dog("Луна", 2, "Вівчарка")
cat = Cat("Муся", 6, "Білий")

print(dog.display_info())
print(dog.make_sound())

print(cat.display_info())
print(cat.make_sound())
