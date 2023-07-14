# Classes

class MyEmptyPerson:
    pass


class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.__name = name  # Propiedad privada
        self.surname = surname
        self.alias = alias

    def walk(self):
        print(f"{self.alias} está caminando")

    def get_name(self):  # Getter
        return self.__name


my_person = Person("Brais", "Moure")

my_person.walk()

my_other_person = Person("Brais", "Moure")

my_other_person.walk()
my_other_person.name = "Héctor de León El loco de los perros"

print(my_person.get_name())
