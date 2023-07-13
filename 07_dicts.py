# Dictionaries

my_dict = dict()
my_other_dict = {}

print(type(my_dict))


my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

my_other_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}


print(my_dict)
print(my_other_dict)

print(len(my_other_dict))

print(my_other_dict["Nombre"])

my_other_dict["Nombre"] = "Pedro"

print(my_other_dict["Nombre"])

print(my_other_dict[1])

del my_other_dict["Nombre"]

print(my_other_dict)

print("Moure" in my_other_dict)

print("Apellido" in my_other_dict)

print(my_other_dict["Apellido"])


print("--------")
print(my_other_dict)
print(my_other_dict.items())
print(my_other_dict.keys())
print(my_other_dict.values())

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
print(my_new_dict["Piso"])

my_another_dict = dict.fromkeys(my_other_dict)

print(my_another_dict)

