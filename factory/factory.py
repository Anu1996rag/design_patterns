from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self):
        self.name = "Mike"

    def __str__(self):
        return self.name

    @property
    def make_sound(self):
        return "bow wow"


class Cat(Animal):
    def __init__(self):
        self.name = "Alexa"

    def __str__(self):
        return self.name

    @property
    def make_sound(self):
        return "meow"


def animal_invoke_factory(animal: str) -> Animal:
    animal_type = animal.lower().strip()

    if animal_type == "cat":
        result = Cat
    elif animal_type == "dog":
        result = Dog
    else:
        raise ValueError(f"Unable to find {animal}")

    return result()


def get_animal(animal: str) -> Animal:
    factory_obj = None

    try:
        factory_obj = animal_invoke_factory(animal)
    except ValueError as error:
        print(error)

    return factory_obj


def main():
    animal = get_animal("cat")
    print(f"{animal} says {animal.make_sound}")


if __name__ == "__main__":
    main()
