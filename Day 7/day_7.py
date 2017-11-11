class Animal:
    name = None
    noise = None
    size = None
    color = None
    hair = None

    def __init__(self, name, noise, size, color, hair):
        self.name = name
        self.noise = noise
        self.size = size
        self.color = color
        self.hair = hair

    def get_name(self):
        return self.name


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age


dog = Dog("John", 2)
print dog.name, dog.age
dog.size = "large"
print dog.name, dog.age, dog.size
